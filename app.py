import streamlit as st
from bots.issue_summarizer import summarize_issue
from bots.test_generator import generate_tests
from bots.code_reviewer import review_code

st.set_page_config(page_title="AI DevOps Bot", layout="centered")

st.title("🤖 AI DevOps Assistant")
st.markdown("Build Software. Faster. Using AI for summarization, test generation, and code review.")

# --- Tabs for different tools ---
tab1, tab2, tab3 = st.tabs(["📝 Issue Summarizer", "✅ Test Generator", "🔍 Code Reviewer"])


# ========== TAB 1: ISSUE SUMMARIZER ==========
with tab1:
    st.subheader("Summarize GitLab Issues or Tasks")

    issue_text = st.text_area("Paste the issue description here:", height=200)

    col1, col2 = st.columns(2)
    min_len = col1.slider("Minimum Summary Length", 10, 100, 30)
    max_len = col2.slider("Maximum Summary Length", 50, 300, 130)

    if st.button("Summarize"):
        if issue_text.strip():
            summary = summarize_issue(issue_text, min_len=min_len, max_len=max_len)
            st.success("📝 Summary:")
            st.write(summary)
        else:
            st.warning("Please enter an issue description.")


# ========== TAB 2: TEST GENERATOR ==========
with tab2:
    st.subheader("Generate Unit Test Template")

    code_input = st.text_area("Paste a Python function here:", height=200)

    if st.button("Generate Tests"):
        if code_input.strip():
            test_stub = generate_tests(code_input)
            st.success("✅ Test Stub:")
            st.code(test_stub, language='python')
        else:
            st.warning("Please paste a Python function to generate tests.")


# ========== TAB 3: CODE REVIEW ==========
with tab3:
    st.subheader("Code Quality Review (pylint based)")

    uploaded_file = st.file_uploader("Upload a Python (.py) file for review", type=["py"])

    if uploaded_file is not None:
        code = uploaded_file.read().decode("utf-8")

        # Save to temp file
        with open("temp_uploaded.py", "w") as f:
            f.write(code)

        if st.button("Review Code"):
            st.info("Running code review using pylint...")
            result = review_code("temp_uploaded.py")
            st.success("🔍 Review Result:")
            st.text(result)
    else:
        st.markdown("⚠️ Please upload a `.py` file to perform code review.")
