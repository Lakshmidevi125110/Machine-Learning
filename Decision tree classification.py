import pandas as pd
import matplotlib.pyplot as plt
import argparse
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# -------------------------------
# Load Iris Dataset
# -------------------------------
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# Convert numeric target to class names
df["target"] = df["target"].map({
    0: iris.target_names[0],
    1: iris.target_names[1],
    2: iris.target_names[2]
})

# Save dataset to CSV
df.to_csv("iris_dataset.csv", index=False)

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# -------------------------------
# Train Decision Tree Model
# -------------------------------
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X, y)

print("Lakshmi Devi - 2303717710422024")

# -------------------------------
# Function to parse input values
# -------------------------------
def parse_input_values(raw: str):
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    if len(parts) != X.shape[1]:
        raise ValueError(f"Expected {X.shape[1]} values, got {len(parts)}")
    return [float(p) for p in parts]

# -------------------------------
# Function to get user input
# -------------------------------
def get_user_input(args):

    if args.input:
        return parse_input_values(args.input)

    if args.interactive:
        vals = []
        print("Enter feature values for a single sample:")
        for col in X.columns:
            while True:
                try:
                    v = input(f"{col}: ")
                    vals.append(float(v))
                    break
                except ValueError:
                    print("Please enter a valid number.")
        return vals

    # Default sample (Setosa)
    return [5.1, 3.5, 1.4, 0.2]

# -------------------------------
# Main Function
# -------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Train a Decision Tree on Iris and predict a single sample."
    )
    parser.add_argument("--input", type=str,
                        help="Comma-separated feature values (e.g. 5.1,3.5,1.4,0.2)")
    parser.add_argument("--interactive", action="store_true",
                        help="Prompt interactively for feature values")

    args = parser.parse_args()

    sample = get_user_input(args)

    prediction = model.predict(pd.DataFrame([sample], columns=X.columns))
    print("Predicted Class:", prediction[0])


if __name__ == "__main__":
    main()

# -------------------------------
# Plot Decision Tree
# -------------------------------
plt.figure(figsize=(20, 10))
plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    fontsize=12
)
plt.title("Decision Tree - Iris Dataset")
plt.savefig("iris_decision_tree.pdf", bbox_inches="tight")
plt.show()
