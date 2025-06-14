import requests
from transformers import pipeline, AutoTokenizer
from config import GITLAB_API_TOKEN, PROJECT_ID
from langdetect import detect

# Initialize summarizer and tokenizer
MODEL_NAME = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=MODEL_NAME, framework="pt")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def get_issue_and_comments(issue_iid: int) -> str:
    """
    Fetch issue title, description, and all comments from GitLab.

    Args:
        issue_iid (int): The internal ID of the GitLab issue.

    Returns:
        str: Combined text of title, description, and comments.
    """
    headers = {"PRIVATE-TOKEN": GITLAB_API_TOKEN}
    base_url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/issues/{issue_iid}"

    try:
        issue_res = requests.get(base_url, headers=headers)
        issue_res.raise_for_status()
        issue = issue_res.json()

        comments_url = f"{base_url}/notes"
        comments_res = requests.get(comments_url, headers=headers)
        comments_res.raise_for_status()
        comments = comments_res.json()

        full_text = f"{issue.get('title', '')}. {issue.get('description', '')}"
        for note in comments:
            full_text += f"\n{note.get('body', '')}"

        return full_text.strip()

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch issue/comments: {e}")
        return ""

def summarize_text(text: str, min_len: int = 30, max_len: int = 130) -> str:
    """
    Summarize provided text using Hugging Face summarization model.

    Args:
        text (str): Input text to summarize.
        min_len (int): Minimum length of the summary.
        max_len (int): Maximum length of the summary.

    Returns:
        str: Summarized version of the text.
    """
    if not text.strip():
        return "❌ No content to summarize."

    try:
        # Detect language
        lang = detect(text)
        if lang != "en":
            return f"🌐 Detected language '{lang}' not supported yet."

        text = text.replace("\n", " ").strip()

        # Truncate using tokenizer token limit
        input_ids = tokenizer.encode(text, truncation=True, max_length=1024)
        truncated_text = tokenizer.decode(input_ids, skip_special_tokens=True)

        summary = summarizer(truncated_text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]["summary_text"]

    except Exception as e:
        print(f"[ERROR] Summarization failed: {e}")
        return "⚠️ Summarization failed due to internal error."

def summarize_issue(issue_iid: int, min_len: int = 30, max_len: int = 130) -> str:
    """
    Main function to fetch issue and return summarized content.

    Args:
        issue_iid (int): GitLab issue internal ID.
        min_len (int): Minimum length of the summary.
        max_len (int): Maximum length of the summary.

    Returns:
        str: Final summarized text or error message.
    """
    text = get_issue_and_comments(issue_iid)
    if not text:
        return "❌ Could not fetch issue data from GitLab."
    return summarize_text(text, min_len=min_len, max_len=max_len)
