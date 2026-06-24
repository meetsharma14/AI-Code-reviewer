import streamlit as st
import requests

st.title("AI Code Reviewer")

code = st.text_area("Paste your code here")

if st.button("Review Code"):
    response = requests.post(
        "https://ai-code-reviewer-gscg.onrender.com/review",
        json={"code": code}
    )

   

    if response.status_code == 200:
        result = response.json()

        st.subheader("Syntax Check")
        st.write(result["syntax"])

        st.subheader("Complexity Analysis")
        st.write(result["complexity"])

        st.subheader("Bug Prediction")
        st.write(result["bug_prediction"])
        
        st.subheader("Code Quality Score")
        st.progress(result["quality_score"] / 100)
        st.write(result["quality_score"], "/100")



        st.subheader("Security Scan")
        st.text(result["security"])

        st.subheader("Suggestions")
        for s in result["suggestions"]:
            st.write("-", s)
