import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame

st.title("🌸 Iris Flower Classifier with Images")

# Sidebar inputs for features
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

# Train-test split & classifier
X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['target'], random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Prediction
features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(features)[0]
pred_species = iris.target_names[prediction]

st.subheader("🔮 Prediction")
st.write(f"The model predicts this flower is: **{pred_species.capitalize()}**")

# Show corresponding flower image
images = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/5/56/Iris_setosa_2.jpg",
    "versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
}

st.image(images[pred_species], caption=f"Iris {pred_species.capitalize()}", use_column_width=True)
