# Principal Component Analysis (PCA) Implementation

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Create Dataset (Students S1–S5)
data = {
    'Internal (X)': [70, 60, 85, 75, 90],
    'Final Exam (Y)': [75, 68, 92, 80, 94]
}

df = pd.DataFrame(
    data,
    index=['S1', 'S2', 'S3', 'S4', 'S5']
)

print("Original Dataset:\n")
print(df)

# Step 2: Standardize the Data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

print("\nStandardized Data:\n")
print(scaled_data)

# Step 3: Apply PCA (2 components since 2 features)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Step 4: Create DataFrame for Principal Components
pca_df = pd.DataFrame(
    data=principal_components,
    columns=['Principal Component 1', 'Principal Component 2'],
    index=['S1', 'S2', 'S3', 'S4', 'S5']
)

print("\nPrincipal Components:\n")
print(pca_df)

# Step 5: Display Explained Variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Retained:")
print(np.sum(pca.explained_variance_ratio_))
