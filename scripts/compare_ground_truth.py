import pandas as pd
import os

ground_truth_file = "dataset/ground_truth/Ground_Truth_Dataset.xlsx"
benchmark_file = "results/benchmark_results.csv"

gt = pd.read_excel(ground_truth_file)
bench = pd.read_csv(benchmark_file)

gt = gt.dropna(subset=["Filename", "Label"])
gt["Filename_Clean"] = gt["Filename"].astype(str).apply(os.path.basename)
gt["Label"] = gt["Label"].astype(str).str.strip().str.lower()

bench["Filename_Clean"] = bench["Filename"].astype(str).apply(os.path.basename)

tools = ["Semgrep", "Bandit", "CodeQL", "Snyk"]

comparison_rows = []
metrics_rows = []

for tool in tools:
    tool_findings = bench[bench["Tool"] == tool]["Filename_Clean"].unique()

    TP = FP = FN = TN = 0

    for _, row in gt.iterrows():
        filename = row["Filename_Clean"]
        label = row["Label"]

        detected = filename in tool_findings

        if label == "vulnerable" and detected:
            result = "TP"
            TP += 1
        elif label == "vulnerable" and not detected:
            result = "FN"
            FN += 1
        elif label == "safe" and detected:
            result = "FP"
            FP += 1
        elif label == "safe" and not detected:
            result = "TN"
            TN += 1
        else:
            continue

        comparison_rows.append({
            "Tool": tool,
            "Filename": filename,
            "Ground_Truth_Label": label,
            "Detected_By_Tool": detected,
            "Result": result
        })

    metrics_rows.append({
        "Tool": tool,
        "TP": TP,
        "FP": FP,
        "FN": FN,
        "TN": TN
    })

comparison_df = pd.DataFrame(comparison_rows)
metrics_df = pd.DataFrame(metrics_rows)

comparison_df.to_csv("results/comparison_table.csv", index=False)
metrics_df.to_csv("results/final_metrics.csv", index=False)

print("Created results/comparison_table.csv")
print("Created results/final_metrics.csv")
print(metrics_df)
