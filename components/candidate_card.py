import streamlit as st


def show_candidate(name,
                   email,
                   phone):

    st.subheader("👤 Candidate Details")

    st.info(f"**Name:** {name}")

    st.info(f"**Email:** {email}")

    st.info(f"**Phone:** {phone}")