import streamlit as st
import plotly.express as px
import pandas as pd


def skill_chart(matched,
                missing):

    df = pd.DataFrame(
        {
            "Category":[
                "Matched",
                "Missing"
            ],
            "Skills":[
                matched,
                missing
            ]
        }
    )

    fig = px.bar(
        df,
        x="Category",
        y="Skills",
        color="Category",
        text="Skills"
    )

    fig.update_layout(
        height=350,
        title="Skill Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )