from bots.issue_summarizer import summarize_issue
from bots.test_generator import generate_tests
from bots.code_reviewer import review_code
import os

# -------------------------------
# 1. Issue Summarization
# -------------------------------
issue_iid = 1  # Replace with actual issue ID
summary = summarize_issue(issue_iid)
print("📝 Summary:\n", summary)

# -------------------------------
# 2. Test Generator
# -------------------------------
sample_func = '''
def add(a, b):
    """Returns sum of a and b"""
    return a + b
'''
test_stub = generate_tests(sample_func)
print("✅ Test Stub:\n", test_stub)

# -------------------------------
# 3. Code Reviewer
# -------------------------------
temp_file_path = "temp_sample.py"

# Save sample_func to a temporary file
with open(temp_file_path, "w") as f:
    f.write(sample_func)

# Run review
review = review_code(temp_file_path)
print("🔍 Code Review:\n", review)

# Optional: Clean up the temp file
os.remove(temp_file_path)
