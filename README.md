# 🏥 Pengembangan Web Service Untuk Deteksi Dini Penyakit

![API](https://img.shields.io/badge/API-Online-brightgreen) ![Flask](https://img.shields.io/badge/Flask-2.3.x-blue) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![MySQL](https://img.shields.io/badge/MySQL-8.0-orange) ![JWT](https://img.shields.io/badge/JWT-Auth-green) ![Fuzzy Logic](https://img.shields.io/badge/Fuzzy-Logic-yellowgreen)

REST API untuk sistem deteksi dini penyakit menggunakan metode fuzzy logic dan certainty factor dengan autentikasi JWT

[Dokumentasi API](https://documenter.getpostman.com/view/50431911/2sBXVig9e9) · [Report Bug](https://github.com/tembokbaleko123/Pengembangan-Web-Service-Untuk-Deteksi-Dini-Penyakit/issues) · [Request Feature](https://github.com/tembokbaleko123/Pengembangan-Web-Service-Untuk-Deteksi-Dini-Penyakit/issues)

---

## 📋 Daftar Isi
- [Tentang Project](#tentang-project)
  - [Fitur Utama](#fitur-utama)
  - [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Arsitektur Sistem](#arsitektur-sistem)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Instalasi](#instalasi)
  - [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Struktur Proyek](#struktur-proyek)
- [Dokumentasi API](#dokumentasi-api)
- [Kontribusi](#kontribusi)

---

## 📖 Tentang Project

Proyek ini adalah sebuah **REST API** yang dirancang untuk mendeteksi dini penyakit menggunakan metode **Fuzzy Logic** dan **Certainty Factor**. Aplikasi ini memungkinkan pengguna untuk melakukan diagnosis penyakit berdasarkan gejala yang mereka alami dengan dukungan autentikasi JWT.

### Fitur Utama
- ✅ **User Authentication** - Registrasi dan login dengan autentikasi JWT
- ✅ **Diagnosis Penyakit** - Diagnosis berbasis fuzzy logic dan certainty factor
- ✅ **Riwayat Diagnosis** - Pengguna dapat melihat riwayat diagnosis yang telah dilakukan
- ✅ **Profile Management** - Edit dan kelola profil pengguna
- ✅ **Activity Log** - Pencatatan aktivitas pengguna
- ✅ **RESTful API** - API yang lengkap dan terstruktur dengan baik

### Teknologi yang Digunakan
- **Backend Framework**: Flask 2.3.x
- **Database**: MySQL 8.0
- **Authentication**: JWT (Flask-JWT-Extended)
- **ORM**: SQLAlchemy
- **Fuzzy Logic**: scikit-fuzzy
- **Data Processing**: Pandas, NumPy, SciPy
- **Language**: Python 3.8+

---

## 🏗️ Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────┐
│                   Web Interface                         │
│                  (Templates/HTML)                       │
└────────────────┬────────────────────────────────────────┘
                 │
         ┌───────▼────────────┐
         │    Flask Routes    │
         │  (API Endpoints)   │
         └───────┬────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼────────┐         ┌──────▼──────┐
│  Services  │         │   Models    │
│ - Diagnosis│         │ - User      │
│ - Activity │         │ - Diagnosis │
└───┬────────┘         │ - Activity  │
    │                  └──────┬──────┘
    │                         │
    └────────────┬────────────┘
                 │
         ┌───────▼────────┐
         │  Fuzzy Engine  │
         │ - CF Engine    │
         │ - Inference    │
         │ - Membership   │
         └───────┬────────┘
                 │
         ┌───────▼────────┐
         │    Database    │
         │    (MySQL)     │
         └────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
Sebelum memulai, pastikan Anda telah menginstall:
- Python 3.8 atau lebih tinggi
- MySQL 8.0 atau lebih tinggi
- pip (Python package manager)
- Git

### Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/tembokbaleko123/Pengembangan-Web-Service-Untuk-Deteksi-Dini-Penyakit.git
   cd Pengembangan-Web-Service-Untuk-Deteksi-Dini-Penyakit
   ```

2. **Buat Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Aktifkan Virtual Environment**
   - Pada Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Pada macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Konfigurasi Database**
   - Buat database MySQL baru:
     ```sql
     CREATE DATABASE sistem_pakar_cp;
     ```
   - Update konfigurasi di `config.py` sesuai dengan kredensial MySQL Anda

### Menjalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

---

## 📁 Struktur Proyek

```
.
├── app.py                    # File utama aplikasi Flask
├── config.py                 # Konfigurasi aplikasi
├── extensions.py             # Inisialisasi ekstenssi (SQLAlchemy, JWT)
├── requirements.txt          # Daftar dependencies
│
├── cf/                       # Certainty Factor Engine
│   ├── __init__.py
│   ├── cf_engine.py          # Logika CF
│   └── cf_rules.py           # Rules untuk CF
│
├── fuzzy/                    # Fuzzy Logic Engine
│   ├── __init__.py
│   ├── fuzzification.py      # Proses fuzzifikasi
│   ├── defuzzification.py    # Proses defuzzifikasi
│   ├── inference.py          # Mesin inferensi fuzzy
│   └── membership.py         # Fungsi keanggotaan
│
├── models/                   # Database Models
│   ├── __init__.py
│   ├── user.py               # Model User
│   ├── diagnosis_history.py  # Model Diagnosis History
│   └── activity_log.py       # Model Activity Log
│
├── routes/                   # API Routes
│   ├── __init__.py
│   ├── auth.py               # Authentication routes
│   └── diagnosis.py          # Diagnosis routes
│
├── services/                 # Business Logic
│   ├── __init__.py
│   └── diagnosis_service.py  # Service untuk diagnosis
│
├── utils/                    # Utilities
│   ├── __init__.py
│   ├── excel_loader.py       # Excel data loader
│   └── log_decorator.py      # Decorator untuk logging
│
├── templates/                # HTML Templates
│   ├── index.html
│   ├── auth/
│   ├── diagnosa/
│   └── profile/
│
├── static/                   # Static Files
│   ├── css/
│   ├── asset/
│   └── uploads/
│
└── dataset/                  # Data Files
```

---

## 📚 Dokumentasi API

Dokumentasi lengkap API dapat diakses melalui **Postman**:

👉 [**Buka Dokumentasi API**](https://documenter.getpostman.com/view/50431911/2sBXVig9e9)

### Endpoint Utama

- **Authentication**
  - `POST /api/auth/register` - Registrasi user baru
  - `POST /api/auth/login` - Login user
  - `POST /api/auth/logout` - Logout user

- **Diagnosis**
  - `POST /api/diagnosis` - Lakukan diagnosis
  - `GET /api/diagnosis/history` - Lihat riwayat diagnosis
  - `GET /api/diagnosis/:id` - Lihat detail diagnosis

- **Profile**
  - `GET /api/profile` - Lihat profil
  - `PUT /api/profile` - Update profil

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request
