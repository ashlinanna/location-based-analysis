import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset .csv")

# Remove missing values
df = df.dropna()

# Streamlit Title
st.title("Location-Based Restaurant Analysis")

st.write("Analyze restaurant distribution and ratings by city")

# Top Cities by Restaurant Count
city_counts = df['City'].value_counts().head(10)

st.subheader("Top 10 Cities by Restaurant Count")

fig, ax = plt.subplots(figsize=(10,5))

city_counts.plot(kind='bar', ax=ax)

plt.xlabel("City")
plt.ylabel("Number of Restaurants")

st.pyplot(fig)

# Average Rating by City
avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)

st.subheader("Top Cities by Average Rating")

fig2, ax2 = plt.subplots(figsize=(10,5))

avg_rating.plot(kind='bar', ax=ax2)

plt.xlabel("City")
plt.ylabel("Average Rating")

st.pyplot(fig2)

st.success("Location-Based Analysis Completed Successfully!")
