import requests

URL = "https://hmdb.ca/metabolites?utf8=%E2%9C%93&query=glucose&search_field=all"
HEADERS = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=HEADERS)
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("First 500 Characters of Response:", response.text[:500])
