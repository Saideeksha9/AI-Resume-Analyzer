import streamlit as st


def show_metrics(score,
                 total_skills,
                 matched,
                 missing):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🎯 ATS Score",
            f"{score}%"
        )

    with c2:

        st.metric(
            "🛠 Skills",
            total_skills
        )

    with c3:

        st.metric(
            "✅ Matched",
            matched
        )

    with c4:

        st.metric(
            "❌ Missing",
            missing
        )

    st.progress(
        min(int(score),100)
    )