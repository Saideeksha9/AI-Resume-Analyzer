import streamlit as st


def show_footer():

    st.markdown("---")

    st.markdown(
        """
        <center>

        <h3>ResumeIQ AI</h3>

        <p>
        Built using Python • Streamlit • NLP • Machine Learning
        </p>

        </center>
        """,
        unsafe_allow_html=True
    )