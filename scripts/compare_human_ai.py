import pandas as pd
import os

ground_truth_file = "dataset/ground_truth/Ground_Truth_Dataset.xlsx"
benchmark_file = "results/benchmark_results.csv"

gt = pd.read_excel(ground_truth_file)
bench = pd.read_csv(benchmark_file)

gt = gt.dropna(subset=["Filename", "Label"])

gt["Filename"] = gt["Filename"].astype(str)
gt["Filename_Clean"] = gt["Filename"].apply(os.path.basename)
gt["Label"] = gt["Label"].astype(str).str.strip().str.lower()

def get_dataset_type(filename):
    filename = filename.lower()
    if "human" in filename:
        return "Human"
    elif "ai" in filename:
        return "AI"
    else:
        return "Unknown"

gt["Dataset"] = gt["Filename"].apply(get_dataset_type)

bench["Filename"] = bench["Filename"].astype(str)
bench["Filename_Clean"] = bench["Filename"].apply(os.path.basename)

tools = ["Semgrep", "Bandit", "CodeQL", "Snyk"]

comparison_rows = []
metrics_rows = []

for tool in tools:
    tool_findings = bench[bench["Tool"] == tool]["Filename_Clean"].unique()

    for dataset_type in ["Human", "AI"]:
        subset = gt[gt["Dataset"] == dataset_type]

        TP = FP = FN = TN = 0

        for _, row in subset.iterrows():
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
                "Dataset": dataset_type,
                "Filename": filename,
                "Ground_Truth_Label": label,
                "Detected_By_Tool": detected,
                "Result": result
            })

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        accuracy = (TP + TN) / (TP + FP + FN + TN) if (TP + FP + FN + TN) > 0 else 0
        fpr = FP / (FP + TN) if (FP + TN) > 0 else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        metrics_rows.append({
            "Tool": tool,
            "Dataset": dataset_type,
            "TP": TP,
            "FP": FP,
            "FN": FN,
            "TN": TN,
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "Accuracy": round(accuracy, 4),
            "False_Positive_Rate": round(fpr, 4),
            "F1_Score": round(f1, 4)
        })

comparison_df = pd.DataFrame(comparison_rows)
metrics_df = pd.DataFrame(metrics_rows)

comparison_df.to_csv("results/human_ai_comparison_table.csv", index=False)
metrics_df.to_csv("results/human_ai_metrics.csv", index=False)

print("Created results/human_ai_comparison_table.csv")
print("Created results/human_ai_metrics.csv")
print(metrics_df)
