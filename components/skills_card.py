import streamlit as st


def show_skills(title,
                skills):

    st.subheader(title)

    if len(skills)==0:

        st.warning("No Skills Found")

        return

    cols = st.columns(2)

    for i,skill in enumerate(skills):

        cols[i%2].success(skill)