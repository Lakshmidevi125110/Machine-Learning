from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -----------------------------
# Dataset (10 samples)
# -----------------------------
reviews = [
    "good movie nice",
    "excellent movie",
    "good acting movie",
    "nice acting",
    "good excellent movie",
    "bad movie boring",
    "boring acting",
    "bad acting",
    "boring movie",
    "bad boring movie"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative",
    "Negative",
    "Negative"
]

# -----------------------------
# Step 1: Convert text to numerical features
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# -----------------------------
# Step 2: Split dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

# -----------------------------
# Step 3: Train Naive Bayes model
# -----------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# Step 4: Test the model
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Step 5: Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# -----------------------------
# Step 6: Test with new review
# -----------------------------
test_review = ["good movie"]
test_vector = vectorizer.transform(test_review)
prediction = model.predict(test_vector)

print("Test Review:", test_review[0])
print("Predicted Sentiment:", prediction[0])
