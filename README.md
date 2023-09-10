# README - Aplikasi Adaptable

## Tautan Aplikasi

Anda dapat mengakses aplikasi Adaptable yang sudah di-deploy melalui tautan berikut: [Tautan Aplikasi Adaptable](https://poke-co.adaptable.app/main/)

## Langkah demi Langkah Implementasi

### Implementasi
Berikut adalah langkah-langkah implementasi yang saya lakukan untuk aplikasi Adaptable:

1. **Pengaturan Proyek**: Saya membuat proyek Django menggunakan perintah `django-admin startproject my_project`.

2. **Aplikasi Django**: Selanjutnya, saya membuat aplikasi dalam proyek menggunakan perintah `python manage.py startapp my_project`.

3. **Pengembangan Model**: Saya mendefinisikan model dalam berkas `models.py` yang akan digunakan untuk menyimpan data dalam database.

4. **Membuat Migrasi**: Saya menjalankan perintah `python manage.py makemigrations` untuk membuat file migrasi berdasarkan model yang telah dibuat, lalu `python manage.py migrate` untuk menerapkan perubahan ke database.

5. **Pengembangan Views**: Saya membuat views dalam berkas `views.py` untuk mengatur logika bisnis aplikasi.

6. **Pengaturan URL**: Saya menghubungkan URL dengan views dalam berkas `urls.py`.

7. **Membuat Template HTML**: Saya membuat berkas HTML yang akan digunakan untuk menampilkan konten kepada pengguna.

8. **Menggunakan Virtual Environment**: Saya menggunakan virtual environment untuk mengisolasi dependensi proyek ini.

9. **Deploy Aplikasi**: Terakhir, saya melakukan deploy aplikasi ke platform hosting yang sesuai.

### Bagan Request Client dan Respon

Berikut adalah bagan yang menjelaskan bagaimana request dari client ke aplikasi web berbasis Django diproses, beserta kaitan antara berkas `urls.py`, `views.py`, `models.py`, dan berkas HTML.

[Client Request] -> [urls.py] -> [views.py] -> [models.py] -> [HTML Template] -> [Client Response]


- **urls.py**: Berkas ini menghubungkan URL yang diterima dari client dengan views yang akan menangani request tersebut.

- **views.py**: Berkas ini berisi logika bisnis yang memproses request dari client, seperti mengambil data dari database menggunakan model yang didefinisikan dalam `models.py`.

- **models.py**: Berkas ini berisi definisi model data yang akan disimpan dalam database.

- **HTML Template**: Berkas ini mengatur tampilan halaman web yang akan dikirimkan sebagai respons kepada client.

## Penggunaan Virtual Environment

Virtual environment digunakan untuk mengisolasi dependensi aplikasi sehingga tidak ada konflik antar aplikasi yang berjalan pada server yang sama. Ini membantu dalam menghindari masalah kompatibilitas dan menjaga kebersihan lingkungan pengembangan.

Meskipun mungkin memungkinkan untuk membuat aplikasi Django tanpa menggunakan virtual environment, sangat disarankan untuk menggunakannya agar menghindari potensi masalah.

## MVC, MVT, MVVM - Perbedaan

- **MVC (Model-View-Controller)**: Ini adalah pola desain yang memisahkan aplikasi menjadi tiga komponen utama - Model (data dan logika bisnis), View (tampilan yang mengatur tampilan antarmuka pengguna), dan Controller (mengendalikan alur aplikasi). MVC digunakan terutama dalam pengembangan perangkat lunak berbasis desktop.

- **MVT (Model-View-Template)**: Ini adalah konsep yang mirip dengan MVC tetapi digunakan dalam kerangka kerja Django. Model adalah data dan logika bisnis, View adalah komponen yang mengendalikan tampilan, dan Template adalah file yang digunakan untuk merender tampilan.

- **MVVM (Model-View-ViewModel)**: Ini adalah pola desain yang digunakan dalam pengembangan aplikasi berbasis web. Model adalah data dan logika bisnis, View adalah tampilan antarmuka pengguna, dan ViewModel adalah komponen yang menghubungkan Model dan View.

Perbedaan utamanya adalah dalam bagaimana aliran data dan pengendalian terstruktur. MVC lebih cocok untuk aplikasi desktop, MVT adalah kerangka kerja yang digunakan dalam Django, dan MVVM digunakan dalam pengembangan aplikasi berbasis web modern.