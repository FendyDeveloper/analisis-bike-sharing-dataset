import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Analysis",
    page_icon="🚲",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("dashboard\main_hour.csv")
    return data

data = load_data()

# Judul Dashboard
st.title("Dashboard Analisis Penggunaan Sepeda Berbagi 🚲")
st.write("Dashboard ini menampilkan analisis pola penggunaan sepeda berbagi berdasarkan musim, cuaca, dan temperatur.")

# Sidebar untuk filter
st.sidebar.header("📊 Filter Data")

# Mapping untuk label yang lebih jelas
season_labels = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}

weather_labels = {
    1: "Cerah ☀️",
    2: "Berkabut 🌫️",
    3: "Hujan Ringan 🌧️",
    4: "Cuaca Buruk ⛈️"
}

season_filter = st.sidebar.multiselect(
    "Pilih Musim:",
    options=list(season_labels.keys()),
    default=list(season_labels.keys()),
    format_func=lambda x: season_labels[x]
)

weather_filter = st.sidebar.multiselect(
    "Pilih Cuaca:",
    options=list(weather_labels.keys()),
    default=list(weather_labels.keys()),
    format_func=lambda x: weather_labels[x]
)

# Filter data
filtered_data = data[
    (data["season"].isin(season_filter)) &
    (data["weathersit"].isin(weather_filter))
]

# Tampilkan ringkasan statistik sederhana
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pengguna", f"{filtered_data['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata Per Jam", f"{filtered_data['cnt'].mean():.0f}")
with col3:
    st.metric("Maksimum Per Jam", f"{filtered_data['cnt'].max():,}")

# Buat dua kolom untuk visualisasi
left_column, right_column = st.columns(2)

with left_column:
    # Visualisasi 1: Pola Penggunaan Berdasarkan Musim
    st.subheader("📊 Penggunaan Berdasarkan Musim")
    season_analysis = filtered_data.groupby('season')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=season_analysis, x='season', y='cnt', palette="viridis", ax=ax)
    ax.set_title("Rata-Rata Penggunaan per Musim")
    ax.set_xlabel("")
    ax.set_ylabel("Rata-Rata Jumlah Pengguna")
    ax.set_xticks(range(len(season_labels)))
    ax.set_xticklabels([season_labels[i] for i in sorted(season_labels.keys())], rotation=45)
    st.pyplot(fig)

with right_column:
    # Visualisasi 2: Penggunaan Berdasarkan Cuaca
    st.subheader("🌤️ Penggunaan Berdasarkan Cuaca")
    weather_analysis = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=weather_analysis, x='weathersit', y='cnt', palette="coolwarm", ax=ax)
    ax.set_title("Rata-Rata Penggunaan per Kondisi Cuaca")
    ax.set_xlabel("")
    ax.set_ylabel("Rata-Rata Jumlah Pengguna")
    ax.set_xticks(range(len(weather_labels)))
    ax.set_xticklabels([weather_labels[i] for i in sorted(weather_labels.keys())], rotation=45)
    st.pyplot(fig)

# Tampilkan tabel ringkasan untuk musim dan cuaca
st.subheader("📋 Ringkasan Data")

# Tabel ringkasan untuk musim
st.write("**Ringkasan Berdasarkan Musim:**")
summary_season = filtered_data.groupby('season')['cnt'].agg(['mean', 'count', 'min', 'max']).round(2)
summary_season.index = [season_labels[i] for i in summary_season.index]
summary_season.columns = ['Rata-rata Pengguna', 'Jumlah Data', 'Minimum', 'Maksimum']
st.dataframe(summary_season, use_container_width=True)

# Tabel ringkasan untuk cuaca
st.write("**Ringkasan Berdasarkan Cuaca:**")
summary_weather = filtered_data.groupby('weathersit')['cnt'].agg(['mean', 'count', 'min', 'max']).round(2)
summary_weather.index = [weather_labels[i] for i in summary_weather.index]
summary_weather.columns = ['Rata-rata Pengguna', 'Jumlah Data', 'Minimum', 'Maksimum']
st.dataframe(summary_weather, use_container_width=True)


# Tombol unduh data
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Unduh Data Hasil Filter (CSV)",
    data=filtered_data.to_csv(index=False),
    file_name="bike_sharing_data.csv",
    mime="text/csv"
)

# Menghitung rata-rata penggunaan berdasarkan musim
season_avg = filtered_data.groupby('season')['cnt'].mean().round(0)
season_max = season_avg.max()
season_min = season_avg.min()
season_max_name = season_labels[season_avg.idxmax()]
season_min_name = season_labels[season_avg.idxmin()]

# Menghitung rata-rata penggunaan berdasarkan cuaca
weather_avg = filtered_data.groupby('weathersit')['cnt'].mean().round(0)
weather_max = weather_avg.max()
weather_min = weather_avg.min()
weather_max_name = weather_labels[weather_avg.idxmax()]
weather_min_name = weather_labels[weather_avg.idxmin()]

# Menampilkan kesimpulan
st.subheader('📝 Kesimpulan Analisis')

st.markdown("""
#### 🌍 Pola Penggunaan Sepeda Berdasarkan Musim:
- **{}** merupakan musim dengan jumlah pengguna tertinggi, dengan rata-rata **{:,.0f}** pengguna per jam.
  Hal ini kemungkinan disebabkan oleh cuaca yang nyaman dan kondisi lingkungan yang mendukung untuk bersepeda.
- Sebaliknya, **{}** mencatat jumlah pengguna terendah dengan rata-rata **{:,.0f}** pengguna per jam.
  Ini mungkin dipengaruhi oleh kondisi cuaca yang kurang mendukung untuk aktivitas bersepeda.

#### ☁️ Pengaruh Cuaca terhadap Penggunaan Sepeda:
- Kondisi cuaca memiliki dampak signifikan terhadap jumlah pengguna sepeda:
  - Pada kondisi **{}**, rata-rata pengguna mencapai **{:,.0f}** orang per jam
  - Sementara pada kondisi **{}**, jumlah pengguna turun menjadi **{:,.0f}** orang per jam
- Perbedaan ini menunjukkan bahwa cuaca menjadi faktor penting dalam keputusan pengguna untuk memilih sepeda sebagai moda transportasi.

#### 💡 Rekomendasi:
- Layanan sepeda berbagi sebaiknya menyediakan unit lebih banyak pada **{}** dan saat cuaca **{}**
- Pertimbangkan untuk memberikan insentif khusus pada **{}** atau saat cuaca **{}** untuk mendorong penggunaan
- Pastikan perawatan sepeda lebih intensif dilakukan menjelang **{}** untuk mengoptimalkan ketersediaan
""".format(
    season_max_name, season_max,
    season_min_name, season_min,
    weather_max_name, weather_max,
    weather_min_name, weather_min,
    season_max_name, weather_max_name,
    season_min_name, weather_min_name,
    season_max_name
))

# Menambahkan catatan tambahan
st.info("""
ℹ️ **Catatan:** Analisis ini didasarkan pada data yang difilter sesuai dengan pemilihan musim dan cuaca pada panel filter.
Hasil mungkin berbeda jika menggunakan filter yang berbeda.
""")

st.write("Copyright 2025. Fendy Rahmat Semua hak cipta dilindungi.")