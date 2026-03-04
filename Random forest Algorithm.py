# ==========================================
# Random Forest with Tree Visualization
# Breast Cancer Dataset
# ==========================================

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

# ------------------------------------------
# 1️⃣ Load Dataset
# ------------------------------------------
data = load_breast_cancer()

X = data.data
y = data.target
feature_names = data.feature_names
class_names = data.target_names

# Create DataFrame and Save as CSV
df = pd.DataFrame(X, columns=feature_names)
df["target"] = y
df["target"] = df["target"].map({0: "malignant", 1: "benign"})
df.to_csv("breast_cancer_dataset.csv", index=False)

print("Dataset saved as breast_cancer_dataset.csv")
print("\nDataset Loaded Successfully")
print("Classes:", class_names)

# ------------------------------------------
# 2️⃣ Build Random Forest Model
# ------------------------------------------
model = RandomForestClassifier(
    n_estimators=5,
    criterion="entropy",
    max_depth=3,
    random_state=42
)

model.fit(X, y)

print("\nRandom Forest built using ENTROPY")

# ------------------------------------------
# 3️⃣ Save All Decision Trees to PDF
# ------------------------------------------
with PdfPages("RandomForest_Trees.pdf") as pdf:
    for i, tree in enumerate(model.estimators_):
        plt.figure(figsize=(15, 8))
        plot_tree(
            tree,
            feature_names=feature_names,
            class_names=class_names,
            filled=True
        )
        plt.title(f"Decision Tree {i+1}")
        pdf.savefig()
        plt.close()

print("All trees saved in RandomForest_Trees.pdf")

# ------------------------------------------
# 4️⃣ Tree-wise Prediction (Majority Voting)
# ------------------------------------------
new_sample = X[0].reshape(1, -1)

print("\nTree-wise Predictions:\n")

tree_predictions = []

for i, tree in enumerate(model.estimators_):
    pred = int(tree.predict(new_sample)[0])   # FIXED HERE
    decoded = class_names[pred]
    tree_predictions.append(decoded)
    print(f"Tree {i+1} Prediction: {decoded}")

# Majority Voting
final_vote = max(set(tree_predictions), key=tree_predictions.count)

print("\nFinal Prediction (Majority Voting):", final_vote)

print("\nProgram Completed Successfully ✅")
