import subprocess

def review_code(file_path):
    try:
        result = subprocess.run(
            ["pylint", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error running pylint: {e}"
