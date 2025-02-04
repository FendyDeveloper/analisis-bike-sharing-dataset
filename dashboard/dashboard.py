import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("main_hour.csv")
    return data

data = load_data()

# Judul Dashboard
st.title("Dashboard Analisis Penggunaan Sepeda Berbagi 🚴‍♂️")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=data["season"].unique(),
    default=data["season"].unique()
)
weather_filter = st.sidebar.multiselect(
    "Pilih Cuaca",
    options=data["weathersit"].unique(),
    default=data["weathersit"].unique()
)

# Filter data berdasarkan sidebar
filtered_data = data[
    (data["season"].isin(season_filter)) &
    (data["weathersit"].isin(weather_filter))
]

# Visualisasi 1: Distribusi Total Pengguna
st.subheader("Distribusi Total Pengguna Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(filtered_data['cnt'], bins=30, kde=True, color="blue", ax=ax)
ax.set_title("Distribusi Total Pengguna Sepeda", fontsize=14)
ax.set_xlabel("Total Pengguna (cnt)", fontsize=12)
ax.set_ylabel("Frekuensi", fontsize=12)
st.pyplot(fig)

# Visualisasi 2: Pola Penggunaan Sepeda Berdasarkan Musim
st.subheader("Pola Penggunaan Sepeda Berdasarkan Musim")
season_analysis = filtered_data.groupby('season')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=season_analysis, x='season', y='cnt', palette="viridis", ax=ax)
ax.set_title("Rata-Rata Penggunaan Sepeda Berdasarkan Musim", fontsize=14)
ax.set_xlabel("Musim", fontsize=12)
ax.set_ylabel("Rata-Rata Jumlah Pengguna", fontsize=12)
ax.set_xticks(ticks=[0, 1, 2, 3], labels=["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
st.pyplot(fig)

# Visualisasi 3: Hubungan Antara Cuaca dan Jumlah Pengguna
st.subheader("Hubungan Antara Cuaca dan Jumlah Pengguna")
weather_analysis = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=weather_analysis, x='weathersit', y='cnt', palette="coolwarm", ax=ax)
ax.set_title("Rata-Rata Penggunaan Sepeda Berdasarkan Cuaca", fontsize=14)
ax.set_xlabel("Kondisi Cuaca", fontsize=12)
ax.set_ylabel("Rata-Rata Jumlah Pengguna", fontsize=12)
ax.set_xticks(ticks=[0, 1, 2, 3], labels=["Cerah", "Berkabut", "Hujan Ringan", "Cuaca Buruk"])
st.pyplot(fig)


# Visualisasi 4: Clustering Berdasarkan Temperatur
st.subheader("Clustering Berdasarkan Temperatur")
temp_group = filtered_data.groupby('temp_category')['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(data=temp_group, x='temp_category', y='cnt', palette="coolwarm", ax=ax)
ax.set_title("Rata-Rata Penggunaan Sepeda Berdasarkan Kategori Temperatur", fontsize=14)
ax.set_xlabel("Kategori Temperatur", fontsize=12)
ax.set_ylabel("Rata-Rata Jumlah Pengguna", fontsize=12)
st.pyplot(fig)