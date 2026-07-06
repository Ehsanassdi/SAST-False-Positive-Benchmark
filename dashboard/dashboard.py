import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SAST Benchmark Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SAST False-Positive Benchmark Dashboard")

st.write(
    "This dashboard compares the performance of Semgrep, Bandit, CodeQL, and Snyk "
    "using the benchmark results generated from the labelled Python dataset."
)

df = pd.read_csv("results/performance_metrics.csv")

st.subheader("Performance Metrics Table")
st.dataframe(df, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    best_accuracy = df.loc[df["Accuracy"].idxmax()]
    st.metric("Best Accuracy", best_accuracy["Tool"], round(best_accuracy["Accuracy"], 4))

with col2:
    best_f1 = df.loc[df["F1_Score"].idxmax()]
    st.metric("Best F1 Score", best_f1["Tool"], round(best_f1["F1_Score"], 4))

with col3:
    lowest_fpr = df.loc[df["False_Positive_Rate"].idxmin()]
    st.metric("Lowest FPR", lowest_fpr["Tool"], round(lowest_fpr["False_Positive_Rate"], 4))

st.divider()

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "False_Positive_Rate",
    "F1_Score"
]

selected_metric = st.selectbox("Select metric to compare:", metrics)

fig = px.bar(
    df,
    x="Tool",
    y=selected_metric,
    title=f"{selected_metric} Comparison",
    text=selected_metric
)

fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")
fig.update_layout(yaxis_range=[0, 1.1])

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("All Metrics Comparison")

long_df = df.melt(
    id_vars=["Tool"],
    value_vars=metrics,
    var_name="Metric",
    value_name="Score"
)

fig2 = px.bar(
    long_df,
    x="Tool",
    y="Score",
    color="Metric",
    barmode="group",
    title="Overall Tool Performance Comparison"
)

fig2.update_layout(yaxis_range=[0, 1.1])
st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Human vs AI Comparison")

st.info(
    "Human vs AI comparison will be added after separate metrics are calculated "
    "for human-written and AI-generated code samples."
)
