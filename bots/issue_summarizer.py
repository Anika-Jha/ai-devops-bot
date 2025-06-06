import requests
from transformers import pipeline
from config import GITLAB_API_TOKEN, PROJECT_ID

# Initialize the summarization pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def get_issue_and_comments(issue_iid: int) -> str:
    """
    Fetches the issue title, description, and all comments from GitLab.

    Args:
        issue_iid (int): The internal ID of the issue.

    Returns:
        str: Concatenated text of the issue title, description, and comments.
    """
    headers = {"PRIVATE-TOKEN": GITLAB_API_TOKEN}
    base_url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/issues/{issue_iid}"

    try:
        # Fetch issue details
        issue_res = requests.get(base_url, headers=headers)
        issue_res.raise_for_status()
        issue = issue_res.json()

        # Fetch issue comments (notes)
        comments_url = f"{base_url}/notes"
        comments_res = requests.get(comments_url, headers=headers)
        comments_res.raise_for_status()
        comments = comments_res.json()

        # Combine title, description, and comments
        full_text = f"{issue.get('title', '')}. {issue.get('description', '')}"
        for note in comments:
            full_text += f"\n{note.get('body', '')}"

        return full_text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching issue data: {e}")
        return ""

def summarize_text(text: str) -> str:
    """
    Summarizes the provided text using Hugging Face's Transformers pipeline.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """
    # Replace newlines with spaces for better summarization
    text = text.replace("\n", " ")

    # Hugging Face models have max token limits; truncate if too long
    max_chunk = 1000
    if len(text) > max_chunk:
        text = text[:max_chunk]

    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Summarization failed."

def summarize_issue(issue_iid: int) -> str:
    """
    Wrapper that fetches issue data and returns its summary.

    Args:
        issue_iid (int): The internal ID of the issue.

    Returns:
        str: Summarized issue content.
    """
    text = get_issue_and_comments(issue_iid)
    if not text:
        return "Failed to fetch issue or comments."
    return summarize_text(text)

