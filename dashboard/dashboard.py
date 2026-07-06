import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SAST Benchmark Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SAST Tool Benchmark Dashboard")
st.write(
    "Comparison of Semgrep, Bandit, CodeQL, and Snyk using a labelled dataset of "
    "human-written and AI-generated Python code."
)

performance_df = pd.read_csv("results/performance_metrics.csv")
human_ai_df = pd.read_csv("results/human_ai_metrics.csv")

st.markdown("---")

# Top summary cards
best_accuracy = performance_df.loc[performance_df["Accuracy"].idxmax()]
best_f1 = performance_df.loc[performance_df["F1_Score"].idxmax()]
lowest_fpr = performance_df.loc[performance_df["False_Positive_Rate"].idxmin()]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Best Accuracy", best_accuracy["Tool"], f"{best_accuracy['Accuracy']:.3f}")

with col2:
    st.metric("Best F1 Score", best_f1["Tool"], f"{best_f1['F1_Score']:.3f}")

with col3:
    st.metric("Lowest False Positive Rate", lowest_fpr["Tool"], f"{lowest_fpr['False_Positive_Rate']:.3f}")

st.markdown("---")

# Overall metrics table
st.subheader("Overall Tool Performance")
st.dataframe(performance_df, use_container_width=True)

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "False_Positive_Rate",
    "F1_Score"
]

selected_metric = st.selectbox(
    "Select metric to compare:",
    metrics
)

fig = px.bar(
    performance_df,
    x="Tool",
    y=selected_metric,
    text=selected_metric,
    title=f"{selected_metric} Comparison Across SAST Tools"
)

fig.update_traces(texttemplate="%{text:.3f}", textposition="outside")
fig.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title=selected_metric,
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# All metrics chart
st.subheader("All Metrics Comparison")

long_df = performance_df.melt(
    id_vars=["Tool"],
    value_vars=metrics,
    var_name="Metric",
    value_name="Score"
)

fig_all = px.bar(
    long_df,
    x="Tool",
    y="Score",
    color="Metric",
    barmode="group",
    title="Overall Performance Metrics"
)

fig_all.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title="Score",
    title_x=0.5
)

st.plotly_chart(fig_all, use_container_width=True)

st.markdown("---")

# Human vs AI section
st.subheader("Human-Written vs AI-Generated Code Comparison")

st.dataframe(human_ai_df, use_container_width=True)

human_ai_metric = st.selectbox(
    "Select Human vs AI metric:",
    metrics,
    key="human_ai_metric"
)

fig_human_ai = px.bar(
    human_ai_df,
    x="Tool",
    y=human_ai_metric,
    color="Dataset",
    barmode="group",
    text=human_ai_metric,
    title=f"Human vs AI Comparison — {human_ai_metric}"
)

fig_human_ai.update_traces(texttemplate="%{text:.3f}", textposition="outside")
fig_human_ai.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title=human_ai_metric,
    title_x=0.5
)

st.plotly_chart(fig_human_ai, use_container_width=True)

st.markdown("---")

# Short conclusion
st.subheader("Summary")
st.write(
    "Based on the benchmark results, Snyk achieved the strongest overall performance "
    "on this dataset, with the highest Accuracy and F1 Score. Semgrep produced very low "
    "false positives, while CodeQL showed the weakest detection performance in this experiment."
)
