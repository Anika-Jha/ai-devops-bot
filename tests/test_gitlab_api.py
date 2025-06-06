import requests
from config import GITLAB_API_TOKEN, GITLAB_API_URL, PROJECT_ID

headers = {"PRIVATE-TOKEN": GITLAB_API_TOKEN}
url = f"{GITLAB_API_URL}/projects/{PROJECT_ID}"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())
