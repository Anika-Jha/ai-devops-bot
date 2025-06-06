import requests
from config import GITLAB_API_TOKEN, GITLAB_API_URL, PROJECT_ID

issue_iid = 1  # change this to an existing issue IID in your project

headers = {"PRIVATE-TOKEN": GITLAB_API_TOKEN}
url = f"{GITLAB_API_URL}/projects/{PROJECT_ID}/issues/{issue_iid}/notes"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
try:
    print("Response:", response.json())
except Exception as e:
    print("Failed to parse JSON:", e)
