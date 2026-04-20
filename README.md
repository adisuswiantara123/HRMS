<div align="center">
  <h1>HRMS - Human Resource Management System</h1>
  <p>Sistem Informasi Manajemen Sumber Daya Manusia Terpadu</p>
</div>

---

> **Dibuat oleh Adi Suswiantara untuk kebutuhan portofolio**

## 📖 Deskripsi Proyek

HRMS (Human Resource Management System) adalah aplikasi web berbasis **Django** yang dirancang untuk mempermudah pengelolaan karyawan, departemen, dan proses pengajuan cuti secara efisien. Proyek ini dikembangkan dengan antarmuka pengguna yang bersih, responsif, dan profesional menggunakan Bootstrap dan modifikasi *CSS modern* (Glassmorphism & typography khusus).

## ✨ Fitur Utama

- **💼 Manajemen Departemen**: Mengelola daftar divisi/departemen perusahaan yang terstruktur.
- **👥 Manajemen Karyawan (Employees)**: Fitur *CRUD (Create, Read, Update, Delete)* komprehensif untuk data profil karyawan dengan dukungan *pagination* data dan pelacakan status.
- **📅 Pengajuan Cuti (Leave Requests)**: Sistem terintegrasi untuk mengajukan, melihat, dan menyetujui permintaan cuti karyawan beserta status persetujuan (*Pending, Approved, Rejected*).
- **📊 Dashboard Interaktif**: Menampilkan ringkasan sistem, metrik karyawan, dan statistik keseluruhan secara langsung.
- **🔐 Sistem Autentikasi**: Panel admin backend bawaan *Django* yang mudah digunakan serta manajemen akses login mandiri bagi karyawan maupun bagian HR.

## 🛠️ Teknologi yang Digunakan

- **Backend:** Python, Django Framework
- **Frontend:** HTML5, CSS3 (*Custom Modern UI*), Bootstrap 5, FontAwesome
- **Database:** SQLite (Mudah dikonfigurasi ke PostgreSQL/MySQL untuk skala besar)

---

## ⚙️ Cara Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek ini pada environment lokal (localhost) Anda:

### 1. Masuk & Aktifkan Virtual Environment
Buka terminal dan navigasi ke folder ini, lalu aktifkan virtual environment bawaan:
```bash
cd c:/HRMS
venv\Scripts\activate
```

### 2. Instalasi Dependensi
Pastikan semua pustaka pihak ketiga telah terinstal:
```bash
pip install -r requirements.txt
```

### 3. Eksekusi Program (Jalankan Server)
Nyalakan *development server* Django:
```bash
python manage.py runserver
```

### 4. Buka di Browser
Akses panel utama aplikasi melalui browser Anda pada link berikut:
[**http://127.0.0.1:8000/**](http://127.0.0.1:8000/)

---

## 🔐 Panel Administrasi

Panel Admin bawaan dapat digunakan untuk mengelola data fundamental (Karyawan, User, Departemen, Grup).
Jika Anda belum memiliki akses admin, buat akun `Superuser` melalui terminal:

```bash
python manage.py createsuperuser
# Isi username, alamat email, dan kata sandi sesuai instruksi shell
```

Setelah berhasil, masuk ke *backend controller*: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## 🔑 Akun Demo (Kredensial Default)

Untuk mempermudah pengujian aplikasi, *database* bawaan telah diisi dengan data dummy (contoh). Anda dapat langsung masuk tanpa repot membuat akun baru dengan data login berikut:

> **Akun Administrator (Superuser)**
> - **Username:** `admin`
> - **Password:** `admin`

> **Akun Karyawan Biasa**
> - **Username:** `budi` (atau `siti`, `andi`, dll. — otomatis dari nama depan karyawan)
> - **Password:** `password123`

*(Anda bisa melihat daftar karyawan lengkap beserta username persis mereka melalui Panel Admin).*

---

## 📂 Struktur Direktori Proyek

```text
c:/HRMS/
├── core/                # Inti Aplikasi: Model Karyawan & Departemen, Views, dan logika dasar
├── leaves/              # Modul fungsional khusus sistem Cuti / Leave Requests
├── hrms/                # Pengaturan utama server Django (Settings, ROOT_URLCONF)
├── templates/           # Berkasi UI HTML (Dashboard, Formulir, Admin overrides)
├── static/              # Aset statis pendukung (Custom CSS Modern, Ikon, dsb)
│
├── manage.py            # Utilitas command-line standard Django
├── requirements.txt     # Daftar modul Python terkait (Dependencies)
└── db.sqlite3           # Arsip Database Development
```

---

<div align="center">
  <br>
  <i>Hak Cipta Terpelihara © Adi Suswiantara</i><br>
  <i>Proyek ini tidak dilisensikan sebagai perangkat keras sumber terbuka (open source). Seluruh repositori dan kode dikhususkan secara eksklusif untuk tujuan demonstrasi dan portofolio profesional pengembang.</i>
</div>
