from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="SAST Benchmark Dashboard",
    page_icon="🛡️",
    layout="wide",
)


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

PERFORMANCE_FILE = PROJECT_ROOT / "results" / "performance_metrics.csv"
HUMAN_AI_FILE = PROJECT_ROOT / "results" / "human_ai_metrics.csv"


# ---------------------------------------------------------
# Data loading
# ---------------------------------------------------------
@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    if not PERFORMANCE_FILE.exists():
        raise FileNotFoundError(
            f"Missing file: {PERFORMANCE_FILE}"
        )

    if not HUMAN_AI_FILE.exists():
        raise FileNotFoundError(
            f"Missing file: {HUMAN_AI_FILE}"
        )

    performance_df = pd.read_csv(PERFORMANCE_FILE)
    human_ai_df = pd.read_csv(HUMAN_AI_FILE)

    return performance_df, human_ai_df


try:
    performance_df, human_ai_df = load_data()
except Exception as error:
    st.error(f"Unable to load the benchmark data: {error}")
    st.stop()


# ---------------------------------------------------------
# Display labels
# ---------------------------------------------------------
METRIC_LABELS = {
    "Accuracy": "Accuracy",
    "Precision": "Precision",
    "Recall": "Recall",
    "False_Positive_Rate": "False Positive Rate",
    "F1_Score": "F1 Score",
}

METRICS = list(METRIC_LABELS.keys())


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.title("🛡️ SAST Tool Benchmark Dashboard")

st.write(
    "This dashboard compares Semgrep, Bandit, CodeQL, and Snyk using a labelled "
    "dataset of human-written and AI-generated Python code."
)

st.markdown("---")


# ---------------------------------------------------------
# Summary cards
# ---------------------------------------------------------
best_accuracy = performance_df.loc[
    performance_df["Accuracy"].idxmax()
]

best_f1 = performance_df.loc[
    performance_df["F1_Score"].idxmax()
]

lowest_fpr = performance_df.loc[
    performance_df["False_Positive_Rate"].idxmin()
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Best Accuracy",
        value=str(best_accuracy["Tool"]),
        delta=f"{best_accuracy['Accuracy']:.3f}",
    )

with col2:
    st.metric(
        label="Best F1 Score",
        value=str(best_f1["Tool"]),
        delta=f"{best_f1['F1_Score']:.3f}",
    )

with col3:
    st.metric(
        label="Lowest False Positive Rate",
        value=str(lowest_fpr["Tool"]),
        delta=f"{lowest_fpr['False_Positive_Rate']:.3f}",
    )

st.markdown("---")


# ---------------------------------------------------------
# Overall tool performance
# ---------------------------------------------------------
st.subheader("Overall Tool Performance")

st.caption(
    "This section compares the four SAST tools across the complete dataset."
)

st.dataframe(
    performance_df,
    use_container_width=True,
    hide_index=True,
)

selected_metric = st.selectbox(
    "Select a metric to compare:",
    options=METRICS,
    format_func=lambda metric: METRIC_LABELS[metric],
)

selected_metric_label = METRIC_LABELS[selected_metric]

fig = px.bar(
    performance_df,
    x="Tool",
    y=selected_metric,
    text=selected_metric,
    title=f"{selected_metric_label} Comparison Across SAST Tools",
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside",
)

fig.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title=selected_metric_label,
    title_x=0.5,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.markdown("---")


# ---------------------------------------------------------
# All metrics comparison
# ---------------------------------------------------------
st.subheader("All Metrics Comparison")

st.caption(
    "This chart gives an overall view of the main evaluation metrics for each tool."
)

long_df = performance_df.melt(
    id_vars=["Tool"],
    value_vars=METRICS,
    var_name="Metric",
    value_name="Score",
)

long_df["Metric"] = long_df["Metric"].map(METRIC_LABELS)

fig_all = px.bar(
    long_df,
    x="Tool",
    y="Score",
    color="Metric",
    barmode="group",
    title="Overall Performance Metrics",
)

fig_all.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title="Score",
    title_x=0.5,
)

st.plotly_chart(
    fig_all,
    use_container_width=True,
)

st.markdown("---")


# ---------------------------------------------------------
# Human vs AI comparison
# ---------------------------------------------------------
st.subheader("Human-Written vs AI-Generated Code Comparison")

st.caption(
    "This section compares each tool's performance on human-written and "
    "AI-generated code."
)

st.dataframe(
    human_ai_df,
    use_container_width=True,
    hide_index=True,
)

human_ai_metric = st.selectbox(
    "Select a Human vs AI metric:",
    options=METRICS,
    format_func=lambda metric: METRIC_LABELS[metric],
    key="human_ai_metric",
)

human_ai_metric_label = METRIC_LABELS[human_ai_metric]

fig_human_ai = px.bar(
    human_ai_df,
    x="Tool",
    y=human_ai_metric,
    color="Dataset",
    barmode="group",
    text=human_ai_metric,
    title=f"Human vs AI Comparison — {human_ai_metric_label}",
)

fig_human_ai.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside",
)

fig_human_ai.update_layout(
    yaxis_range=[0, 1.1],
    xaxis_title="SAST Tool",
    yaxis_title=human_ai_metric_label,
    title_x=0.5,
)

st.plotly_chart(
    fig_human_ai,
    use_container_width=True,
)

st.markdown("---")


# ---------------------------------------------------------
# Key findings
# ---------------------------------------------------------
st.subheader("Key Findings")

st.markdown(
    """
- **Snyk** achieved the strongest overall performance, with the highest Accuracy and F1 Score.

- **Bandit** showed good overall detection performance but produced more false positives than Snyk.

- **Semgrep** produced no false positives, but its lower Recall shows that it missed more vulnerabilities.

- **CodeQL** had the weakest overall performance, with the lowest Accuracy and Recall in this benchmark.

- Only small differences were found between **human-written** and **AI-generated** code, suggesting that code origin had a limited effect on SAST tool performance in this experiment.
"""
)

st.info(
    "Overall, Snyk provided the best balance between vulnerability detection "
    "and false-positive reduction, while human-written and AI-generated code "
    "produced broadly similar results."
)
