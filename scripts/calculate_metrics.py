import pandas as pd

df = pd.read_csv("results/final_metrics.csv")

df["Precision"] = df["TP"] / (df["TP"] + df["FP"])

df["Recall"] = df["TP"] / (df["TP"] + df["FN"])

df["Accuracy"] = (
    (df["TP"] + df["TN"]) /
    (df["TP"] + df["FP"] + df["FN"] + df["TN"])
)

df["False_Positive_Rate"] = (
    df["FP"] /
    (df["FP"] + df["TN"])
)

df["F1_Score"] = (
    2 * df["Precision"] * df["Recall"]
) / (
    df["Precision"] + df["Recall"]
)

df = df.round(4)

df.to_csv(
    "results/performance_metrics.csv",
    index=False
)

print(df)

print("\nCreated results/performance_metrics.csv")
