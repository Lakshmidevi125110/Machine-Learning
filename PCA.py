# ==========================================
# PCA Implementation on Breast Cancer Dataset
# ==========================================

# 1️⃣ Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_breast_cancer

# ------------------------------------------
# 2️⃣ Load Dataset (Built-in from sklearn)
# ------------------------------------------
print("Loading dataset...")

data = load_breast_cancer()
X = data.data
y = data.target

print("Feature Shape:", X.shape)
print("Target Shape:", y.shape)

# ------------------------------------------
# 3️⃣ Standardization (Important for PCA)
# ------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nData Standardized Successfully.")

# ------------------------------------------
# 4️⃣ Apply PCA (All Components)
# ------------------------------------------
pca_full = PCA()
X_pca_full = pca_full.fit_transform(X_scaled)

# Plot Cumulative Explained Variance
plt.figure()
plt.plot(np.cumsum(pca_full.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance by PCA Components')
plt.grid()
plt.show()

print("\nExplained Variance Ratio:")
print(pca_full.explained_variance_ratio_)

# ------------------------------------------
# 5️⃣ Reduce to 95% Variance
# ------------------------------------------
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

print("\nOriginal Shape:", X_scaled.shape)
print("Reduced Shape after PCA:", X_pca.shape)

# ------------------------------------------
# 6️⃣ 2D Visualization
# ------------------------------------------
pca_2d = PCA(n_components=2)
X_2d = pca_2d.fit_transform(X_scaled)

plt.figure()
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("2D PCA Visualization")
plt.show()

# ------------------------------------------
# 7️⃣ Model WITHOUT PCA
# ------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n==============================")
print("Results WITHOUT PCA")
print("==============================")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ------------------------------------------
# 8️⃣ Model WITH PCA
# ------------------------------------------
X_train_pca, X_test_pca, y_train, y_test = train_test_split(
    X_pca, y, test_size=0.2, random_state=42)

model_pca = RandomForestClassifier(random_state=42)
model_pca.fit(X_train_pca, y_train)

y_pred_pca = model_pca.predict(X_test_pca)

print("\n==============================")
print("Results WITH PCA")
print("==============================")
print("Accuracy:", accuracy_score(y_test, y_pred_pca))
print(classification_report(y_test, y_pred_pca))

print("\nProgram Completed Successfully ✅")
