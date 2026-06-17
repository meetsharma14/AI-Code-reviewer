# Import CountVectorizer for text feature extraction
from sklearn.feature_extraction.text import CountVectorizer
# Import Logistic Regression model
from sklearn.linear_model import LogisticRegression
# Import Joblib for saving trained models
import joblib
# Training dataset containing safe and risky code snippets
codes = [
    "print('hello')",
    "a,b=map(int,input().split())",
    "x=int(input())",
    "for x in arr: print(x)",
    # Risky examples

    "eval(user_input)",
    "os.system(user_input)",
    "x=None\nif x==None: print(x)",
    "for i in range(len(arr)): print(arr[i])"
]

labels = [
    0,  # safe
    0,  # safe
    0,  # safe
    0,  # safe

    1,  # risky
    1,  # risky
    1,  # bad style
    1   # bad style
]
# Convert text code into numerical features

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(codes)
# Train Logistic Regression model

model = LogisticRegression()
model.fit(X, labels)
# Save trained model
joblib.dump(model, "models/bug_classifier.pkl")
# Save vectorizer
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully")