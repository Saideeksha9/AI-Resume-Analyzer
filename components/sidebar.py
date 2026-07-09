import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/artificial-intelligence.png",
            width=90
        )

        st.title("ResumeIQ AI")

        st.caption(
            "Smart Resume Analysis Powered by AI"
        )

        st.markdown("---")

        st.subheader("✨ Features")

        features = [
            "ATS Score",
            "Resume Parsing",
            "Skill Extraction",
            "Keyword Matching",
            "Resume Summary",
            "Interview Questions",
            "Learning Roadmap",
            "PDF Report"
        ]

        for feature in features:
            st.write(f"✅ {feature}")

        st.markdown("---")

        st.success("Version 2.0")

        st.info(
            "Upload your Resume and compare it with any Job Description."
        )

        st.markdown("---")

        st.caption("Developed using ❤️ Python + Streamlit")