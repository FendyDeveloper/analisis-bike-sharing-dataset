# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset **Bike Sharing** menggunakan teknik analisis data dan visualisasi. Dashboard interaktif dibuat menggunakan **Streamlit** untuk menyajikan hasil analisis secara visual.

---

## Struktur Folder
```
analisis-bike-sharing-dataset/
├── dashboard/
│   ├── main_data.csv          # Dataset yang sudah diproses
│   └── dashboard.py           # Script untuk menjalankan dashboard Streamlit
├── data/
│   └── hour.csv               # Dataset utama (raw data)
├── notebook.ipynb             # Notebook untuk analisis data
├── README.md                  # Panduan proyek
├── requirements.txt           # Daftar library yang digunakan
└── url.txt                    # Tautan dashboard jika di-deploy (opsional)
```

---

## Cara Menjalankan Dashboard

### 1. Clone Repository
Untuk memulai, clone repository ini menggunakan perintah berikut:
```bash
git clone https://github.com/FendyDeveloper/analisis-bike-sharing-dataset.git
cd analisis-bike-sharing-dataset
```

### 2. Instalasi Dependencies
Sebelum menjalankan dashboard, pastikan semua dependencies sudah terinstal. Jalankan perintah berikut untuk menginstal library yang diperlukan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Dashboard
Setelah semua dependencies terinstal, jalankan dashboard menggunakan perintah berikut:
```bash
streamlit run dashboard.py
```

### 4. Akses Dashboard
Setelah menjalankan perintah di atas, dashboard akan tersedia di browser.  
Buka URL yang muncul di terminal (biasanya `http://localhost:8501`).

---

## Deployment
Jika ingin mendeploy dashboard ke **Streamlit Cloud**:
1. Push folder proyek ke repository GitHub.
2. Hubungkan repository dengan **Streamlit Cloud**.
3. Deploy dashboard dan simpan tautan di file `url.txt`.

---

## Informasi Tambahan

### Dataset
- **Dataset utama (`hour.csv`)** dapat diunduh dari [tautan ini](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/code).
- **Dataset yang sudah diproses** disimpan dalam file `main_data.csv`.

### Tools dan Library
Proyek ini menggunakan tools dan library berikut:
- **Pandas**: Untuk manipulasi dan analisis data.
- **NumPy**: Untuk operasi numerik.
- **Matplotlib & Seaborn**: Untuk visualisasi data.
- **Streamlit**: Untuk membuat dashboard interaktif.

---

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE). Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini sesuai kebutuhan.

---