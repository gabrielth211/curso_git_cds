import pandas as pd 
import plotly.express as px
import streamlit as st

def rd1_question_9(df):
    df_grouped = df[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    fig = px.bar(
        df_grouped,
        x="seller_type",
        y="count",
        labels={"seller_type": "Seller Type", "count": "Quantity"},
        color= "seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    return None