import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load your local dataset
df = pd.read_csv("auto-mpg.csv")

# Clean the dataset
df = df.replace("?", None)
df = df.dropna()
df["horsepower"] = df["horsepower"].astype(float)

# Features and target
X = df[["cylinders", "displacement", "horsepower", "weight"]]
y = df["mpg"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model
pickle.dump(model, open("car_model.pkl", "wb"))

print("Model trained successfully! File saved as car_model.pkl")
