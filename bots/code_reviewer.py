import subprocess
import os
import re

def review_code(file_path: str) -> str:
    """
    Reviews the given Python file using pylint and returns a readable report.

    Args:
        file_path (str): Path to the Python source file.

    Returns:
        str: Formatted pylint report with score and key messages.
    """
    if not file_path or not os.path.isfile(file_path):
        return "❌ Invalid or missing file. Please upload a valid Python file."

    try:
        result = subprocess.run(
            ["pylint", file_path],
            capture_output=True,
            text=True
        )

        output = result.stdout

        # Extract the score from output
        score_match = re.search(r'Your code has been rated at ([\d\.]+)/10', output)
        score = score_match.group(1) if score_match else "N/A"

        # Optionally extract top-level messages
        lines = output.splitlines()
        important_msgs = "\n".join(line for line in lines if ": " in line and "convention" not in line.lower())

        return f"📊 Pylint Score: {score}/10\n\n🔍 Key Feedback:\n{important_msgs or 'No major issues found.'}"

    except FileNotFoundError:
        return "❌ Pylint not found. Please install it using `pip install pylint`."
    except Exception as e:
        return f"⚠️ Error during code review: {e}"
