# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset Bike Sharing menggunakan teknik analisis data dan visualisasi. Dashboard interaktif dibuat menggunakan Streamlit untuk menyajikan hasil analisis secara visual.
___
## Struktur Folder
```aiignore
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt (jika di-deploy)
```

___
## Cara Menjalankan Dashboard

### 1. Instalasi Dependencies
Sebelum menjalankan dashboard, pastikan semua dependencies sudah terinstal. Jalankan perintah berikut untuk menginstal library yang diperlukan:
```
pip install -r requirements.txt
```

### 2. Jalankan Dashboard
Setelah semua dependencies terinstal, jalankan dashboard menggunakan perintah berikut:
```
streamlit run dashboard.py
```

### 3. Akses Dashboard
Setelah menjalankan perintah di atas, dashboard akan tersedia di browser.
Buka URL yang muncul di terminal (biasanya http://localhost:8501).
___

## Informasi Tambahan
Dataset utama (hour.csv) dapat diunduh dari [tautan](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/code) ini .
Dataset yang sudah diproses disimpan dalam file main_data.csv.