import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("sleep_dataset.csv")

df["Sleep_Quality"] = df["Quality of Sleep"].apply(
    lambda x: "Good" if x >= 7 else "Poor"
)

X = df[["Age", "Sleep Duration", "Stress Level"]]
y = df["Sleep_Quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Saved")
