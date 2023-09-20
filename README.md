> Repositori tugas PBP
```credential
NAMA    : Fadhil Muhammad
NPM     : 2206083464
```

<details>
<summary style="color: white; font-size: 30px">Tugas 2</summary>

## Daftar Isi

- [Pengenalan](#pengenalan)
- [Langkah-Langkah Pengimplementasian](#langkah-langkah-pengimplementasian)
- [Diagram](#diagram)
- [Mengapa Menggunakan Virtual Environment?](#mengapa-menggunakan-virtual-environment)
- [Apa itu MVC, MVT, dan MVVM?](#apa-itu-mvc-mvt-dan-mvvm)

## Pengenalan
Tautan web: https://poke-co.adaptable.app/main

[Poké.co](https://poke-co.adaptable.app/main) merupakan website dengan tema utama pengumpulan atau pengoleksian karakter-karakter Pokémon yang dibangun menggunakan Django untuk tugas kali ini.

## Langkah-Langkah Pengimplementasian
Dalam proses pembuatan website ini, hal pertama yang dilakukan adalah membuat repositori baru di github sebagai tempat penyimpanan hasil pekerjaan.

Setelah itu, *step-step* yang dilakukan antara lain:

1. **Membuat Direktori Lokal Baru untuk Proyek Aplikasi**
 
    Langkah pertama adalah membuat direktori baru pada perangkat lokal sebagai direktori utama untuk pengerjaan proyek
2. **Mengaktifkan *Virtual Environment* pada Direktori**

    Setelah direktori pada langkah pertama berhasil dibuat, selanjutnya menginisialisasi atau mengaktifkan virtual environment untuk proyek.
    ```shell
    python -m venv env
    ```
    Menjalankan perintah di atas pada command prompt untuk menginisialisasi virtual environment pada folder proyek.
3. **Mengaktifkan *Virtual Environment***

    Mengaktifkan virtual environment untuk direktori proyek dengan menjalankan script berikut pada command prompt.
    ```
    env\Scripts\activate.bat
    ```
4. **Menginstall *Dependencies* atau *Requirements***

    Setelah virtual environment berhasil diaktifkan, membuat file baru pada direktori bernama `requirements.txt` dengan isi sebagai berikut:

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

    Setelah file `requirements.txt` berhasil dibuat, lalu install requirements atau dependencies tersebut dengan menjalankan script berikut pada command prompt.

    ```shell
    pip install -r requirements.txt
    ``````
5. **Membuat Proyek Django**

    Setelah semua dependencies terinstall, inisialisasi atau mulai proyek baru dengan menjalankan perintah berikut:
    ```shell
    django-admin startproject poke_co .
    ```
6. **Konfigurasi Proyek**

    Setelah proyek berhasil dibuat, langkah selanjutnya adalah mengkonfigurasi proyek. Hal yang dilakukan pada langkah ini di antaranya:

    1. Menambahkan allowed host pada file `settings.py`
        ```python
        ...
        ALLOWED_HOSTS = ["*"]
        ...
        ``` 
    2. Menambahkan direktori staticfiles dan static root pada `settings.py` untuk file-file statis seperti *image*

        ```python
        ...
        STATICFILES_DIRS = (
            join(BASE_DIR, 'main/static'),
        )

        STATIC_ROOT = join(BASE_DIR, 'staticfiles')
        ...
        ```
    3. Mendaftarkan aplikasi `main` ke dalam proyek dengan menambahkan `"main"` ke dalam daftar aplikasi yang ada pada `settings.py`
        ```python
        INSTALLED_APPS = [
            ...,
            "main",
            ...
        ]
        ```
7. **Membuat *Template* untuk Laman *Website***

    Untuk menampilkan laman *page* yang diinginkan saat website dibuka, tambahkan sebuah folder baru pada direktori `main` bernama `templates`, lalu dalam folder `templates` tambahkan `main.html`. 

    Dalam `main.html`, isi file tersebut dengan HTML yang diinginkan. Dalam proyek ini, contoh dari bagianbody HTML yang digunakan untuk proyek ini adalah sebagai berikut:

    ```html
    ...
    <section>
        <h2>Player Information</h2>
        <h5>Name:</h5>
        <p>{{ name }}</p>
        <h5>Class:</h5>
        <p>{{ class }}</p>
    </section>
    ...
    ```
    Untuk selengkapnya dapat dilihat pada file `main.html`

8. **Konfigurasi untuk Gambar**

    Pada proyek ini, gambar digunakan untuk ditampilkan pada laman web. Agar gambar dapat ditampilkan pada saat *production* atau *deployment*:

    1. Buat folder tempat penyimpanan file statis (untuk gambar). Tempat penyimpanan disesuaikan dengan `path` pengambilan gambar yang ada pada template `main.html` dan konfigurasi yang ada pada `settings.py`

    2. Agar gambar dapat diambil pada saat `deployment`, jalankan perintah berikut.
        ```shell
        python manage.py collectstatic
        ```
        Akan terbentuk sebuah folder baru sebagai direktori file yang bisa diambil kontenya pada saat tahap *deployment*. Jika tidak menjalankan perintah tersebut, maka gambar kemungkinan tidak akan muncul pada saat *deployment* walaupun pada saat *development* secara lokal muncul.
    
    3. Tidak lupa, tambahkan `{% load static %}` pada `main.html` agar file statis dapat di-*load*.

9. **Mengimplementasikan Model**

    pada langkah ini, modifikasi file `models.py` sesuai dengan kriteria soal dan aplikasi yang akan dibuat. Untuk proyek ini, isi dari `models.py` adalah sebagai berikut:
    ```python
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=255, name="name")
        amount = models.IntegerField(name="amount")
        rarity = models.IntegerField(name="rarity", default=0)
        power = models.FloatField(name="power", default=0)
        description = models.TextField(name="description")
    ```

10. **Membuat dan Mengaplikasikan Migrasi Model**

    Lakukan migrasi model dengan menjalankan perintah berikut pada Command Prompt agar Django dapat melacak perubahan pada model *database*.
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

11. **Menghubungkan *View* dengan *Template***

    Menambahkan kode berikut pada `views.py`.
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'name':'Fadhil Muhammad',
            'class':'PBP-B',
            'char_name':'Pikachu',
            'char_description':'This is Pikachu. You know this is Pikachu. Why are you asking me about why i wrote this?',
            'char_amount':'You have Gazillion amount of this character.'
        }

        return render(request, 'main.html', context)
    ```
    Karena proyek aplikasi ini belum sepenuhnya dikembangkan, beberapa *variable* masih digunakan hanya sebagai *place holder* sementara.

12. **Melakukan *Routing* URL**

    Agar aplikasi dapat dijalankan tambahkan kode berikut pada `urls.py` pada direktori proyek
    ```python
    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('main/', include('main.urls')),
        path('admin/', admin.site.urls),
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```

    dan kode berikut pada `urls.py` pada direktori `main`
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ] 
    ```

13. **Menambahkan *Unit Testing***

    Untuk menguji website, dilakukan beberapa *unit testing* dasar untuk menguji apakah website berhasil ter-*load* dengan baik atau tidak dengan menambahkan kode pada *tests.py* sesuai dengan pengujian yang ingin dilakukan. Untuk proyek ini:
    ```python
    from django.test import TestCase
    from django.test import Client

    class mainTest(TestCase):
        def test_main_url_is_exist(self):
            client = Client()
            response = client.get('/main/') 
            self.assertEqual(response.status_code, 200)

        def test_main_using_main_template(self):
            client = Client()
            response = client.get('/main/') 
            self.assertTemplateUsed(response, 'main.html')

        def test_template_rendering(self):
            client = Client()
            response = client.get('/main/')
            self.assertEqual(response.status_code, 200)

            # Cek konten template
            self.assertContains(response, "Welcome to Poké.co")
            self.assertContains(response, "Player Information")
            self.assertContains(response, "Featured Character")
            self.assertContains(response, "Name:")
            self.assertContains(response, "Class:")

            # Cek gambar
            self.assertInHTML("<img alt=\"Pikachu\" src=\"/static/main/assets/Angry-Pikachu-Transparent.png\">", response.content.decode())

            # Cek konten footer
            self.assertContains(response, "Fadhil Muhammad (2206083464). Pemrograman Berbasis Platform Gasal 23/24.")
    ```
    Lalu, jalankan *testing* tersebut dengan menjalankan perintah berikut
    ```shell
    python manage.py test
    ```
14. **Melakukan *Deployment***

    Setelah semua tahap selesai, *deploy* aplikasi ke [Adaptable](https://adaptable.io/).


## Diagram *Framework*
![Alt Text](md_image/diagram.png)

Django adalah sebuah framework web yang memungkinkan pengembang untuk dengan mudah membuat dan mengelola situs web yang responsif dan dinamis. Django berfungsi dengan cara berikut:

1. **Permintaan dari Client**: Ketika seorang pengguna membuka situs web di peramban (browser), peramban akan mengirimkan permintaan HTTP ke server Django.

2. ***Routing* dan *URL Pattern***: Django memiliki sistem routing yang akan memeriksa pola URL pada permintaan dari *client* untuk menentukan tindakan atau *view* apa yang harus diambil untuk menangani permintaan tersebut.

3. **Menghubungkan dengan views.py**: Setelah pola URL cocok dengan permintaan, Django akan memanggil fungsi yang sesuai dalam berkas views.py. Fungsi-fungsi ini berisi program-program untuk menangani permintaan tersebut.

4. **Interaksi dengan models.py**: Untuk mengambil atau memanipulasi data yang diperlukan, views.py akan berinteraksi dengan berkas models.py. Models digunakan untuk mendefinisikan struktur data dan hubungan antar data dalam aplikasi.

5. **Membangun Halaman Web (HTML)**: Setelah data yang diperlukan telah diambil dari models.py, views.py akan menggunakan template HTML yang ada dalam direktori templates untuk merender halaman web. Data yang telah diambil dapat dimasukkan ke dalam template untuk membuat halaman web yang dinamis.

6. **HTTP Response**: Terakhir, views.py akan mengembalikan hasilnya dalam bentuk respons HTTP. Respons ini berisi halaman web yang telah dibuat (dalam bentuk HTML) dan akan dikirimkan kembali kepada *client* yang mengirimkan permintaan awal.


## Mengapa Menggunakan *Virtual Environment*?
Ada beberapa alasan mengapa kita sangat disarankan atau diharuskan menggunakan virtual environment saat memulai proyek Django, di antaranya:
1. **Dependensi Tertutup**

    Virtual environment memungkinkan kita untuk membuat lingkungan Python yang terisolasi secara mandiri dari instalasi Python global di sistem. Ini berarti kita dapat memiliki versi Python dan paket dependensi yang berbeda untuk setiap proyek, tanpa khawatir konflik antara versi atau paket yang digunakan oleh proyek yang berbeda.

2. ***Cleanliness* dan Pengelolaan Dependensi**

    Dengan menggunakan virtual environment, kita dapat mengelola dependensi proyek kita dengan lebih mudah. Kita dapat menginstal modul-modul Python yang diperlukan secara terpisah untuk setiap proyek. Selain itu, kita dapat dengan mudah membuat daftar dependensi proyek (biasanya disimpan dalam berkas `requirements.txt`) untuk mengulangi pengaturan proyek di *environment* lain atau bagi orang lain yang ingin bekerja pada proyek tersebut.

3. **Keamanan**

    *Virtual environment* dapat membantu mencegah terjadinya masalah jika ada pembaruan atau perubahan yang perlu kita lakukan pada sebuah proyek, tanpa memengaruhi proyek lain yang menggunakan versi Python atau paket yang berbeda.

Pengerjaan proyek Django tanpa menggunakan *virtual environment* tetap dapat dilaksanakan. Meskipun demikian, poin-poin di atas menjelaskan mengapa *virtual environment* sangat penting digunakan.

## Apa itu MVC, MVT, dan MVVM?

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga kerangka arsitektur yang umum digunakan dalam pengembangan perangkat lunak. Tujuan utamanya adalah membagi komponen-komponen inti dalam aplikasi dan mempermudah manajemen kode. Meskipun ketiganya memiliki kesamaan dalam pemisahan peran, terdapat perbedaan signifikan dalam bagaimana mereka mengatur dan berinteraksi antara satu sama lain.

MVC adalah pendekatan yang pertama kali muncul dalam pengembangan perangkat lunak. Dalam MVC, aplikasi dibagi menjadi tiga komponen utama: Model, View, dan Controller. Model bertanggung jawab atas manajemen data dan logika bisnis, View bertanggung jawab untuk menampilkan data kepada pengguna, sementara Controller bertindak sebagai perantara yang mengoordinasikan aliran data dan tindakan yang dilakukan pengguna.

MVT, atau Model-View-Template, adalah varian dari MVC yang sering digunakan dalam kerangka kerja web seperti Django. Dalam MVT, Model tetap mengelola data dan logika bisnis, sedangkan Template mengambil peran View dalam menampilkan data kepada pengguna. Controller pada dasarnya terintegrasi dalam kerangka kerja Django, sehingga pengembang tidak perlu membuatnya secara eksplisit.

Sementara itu, MVVM adalah arsitektur yang lebih modern, sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna, seperti aplikasi seluler atau desktop. Dalam MVVM, Model tetap mengelola data dan logika bisnis, tetapi ada tambahan komponen yang disebut ViewModel. ViewModel bertindak sebagai perantara antara Model dan View, mengubah data Model agar sesuai dengan tampilan yang diinginkan oleh View, dan mengelola tindakan yang dilakukan oleh pengguna.

Perbedaan utama antara ketiga pendekatan ini terletak pada cara mereka mengatur peran dan tanggung jawab komponen-komponen utama dalam aplikasi. MVC dan MVT umumnya digunakan dalam konteks aplikasi web tradisional, sementara MVVM lebih sering diterapkan dalam aplikasi modern berbasis antarmuka pengguna. Semua arsitektur ini bertujuan untuk memudahkan pemeliharaan kode, meningkatkan skalabilitas, dan memahami konsep dalam pengembangan perangkat lunak, dengan pilihan tergantung pada jenis aplikasi yang dikembangkan dan preferensi pengembangnya.

</details>

<details>
<summary style="color: white; font-size: 30px">Tugas 3</summary>

## Daftar Isi
- [Langkah-Langkah Pengimplementasian](#langkah-langkah-pengimplementasian-1)
- [Apa perbedaan antara form POST dan form GET dalam Django?](#apa-perbedaan-antara-form-POST-dan-form-GET=dalam-Django?)
- [Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?](#apa-perbedaan-utama-antara-xml-json-dan-html-dalam-konteks-pengiriman-data)
- [Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?](#mengapa-json-sering-digunakan-dalam-pertukaran-data-antara-aplikasi-web-modern)
- [Postman](#postman)

## Langkah-Langkah Pengimplementasian
### Membuat `forms.py`
File `forms.py` dalam proyek Django digunakan untuk mendefinisikan formulir yang akan digunakan dalam aplikasi web. Formulir dapat dihubungkan dengan model Django untuk membuat, mengubah, atau menghapus objek model berdasarkan input dari pengguna. 

Isi `forms.py`:
```python
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "rarity", "power", "description"]
```

### Mengubah Isi File `views.py`
Untuk menampilkan jumlah item yang ada pada models, tambahkan kode pada `views.py`agar jumlah item pada models dapat diakses.

*Update* fungsi `show_main()` menjadi:
```python
def show_main(request):
    total_characters = Item.objects.count()
    items = Item.objects.all()
    context = {
        'name':'Fadhil Muhammad',
        'class':'PBP-B',
        'char_name':'Pikachu',
        'char_description':'Pikachu, the most popular character.',
        'char_rarity':'Rare',
        'total_characters':total_characters,
        'items':items
    }

    return render(request, 'main.html', context)
```

### Membuat HTML untuk Form

Menambahkan `create_item.html` untuk tampilan form yang akan ditampilkan kepada user saat diakses. Untuk ini, django telah menyediakan opsi yang memudahkan kita dalam pembuatan laman formulir.

Isi `create_item.html`:
```html
{% extends 'base.html' %}
{% block content %}
<h1>Add New Character to Your List</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Character"/>
            </td>
        </tr>
    </table>
</form>


{% endblock %}
```

### Menambahkan `templates\base.html`
Buat folder baru pada root directory bernama `templates` dan tambahkan file `base.html` di dalamnya. 

Isi dari `base.html`:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
### Meng-*update* `main.html` pada Direktori `main\templates\`
Untuk menampilkan data yang telah disubmit pada form, perlu dilakukan penambahan pada `main.html`. 

Kode yang ditambahkan:
```html
...
    ...
        <section>
            <h2>Your Collections</h2>

            <div style="overflow-y: auto;">
                <table>
                    <tr>
                        <th>Timestamp (UTC+7)</th>
                        <th>Name</th>
                        <th>Amount</th>
                        <th>Rarity</th>
                        <th>Power</th>
                        <th>Description</th>
                    </tr>
                
                    {% for item in items %}
                    <tr>
                        <td>{{item.date_added}}</td>
                        <td>{{item.name}}</td>
                        <td>{{item.amount}}</td>
                        <td>{{item.rarity}}</td>
                        <td>{{item.power}}</td>
                        <td style="min-width: 500px;">{{item.description}}</td>
                    </tr>
                    {% endfor %}
                </table>
                <br />
            </div>
        
            <a href="{% url 'main:create_item' %}">
                <button>
                    Add New Character
                </button>
            </a>
        </section>
    ...
...
```
### Menambahkan View untuk XML dan JSON Serializer
Untuk melihat data-data yang disimpan dalam bentuk XML atau JSOn, digunakan serializer. Untuk melihat hasil serializer dari XML atau JSON, tambahkan dua fungsi berikut pada `views.py`:
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
dan tambahkan path berikut pada `urls.py` direktori aplikasi:
```python
...
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ...
]
...
```
Untuk menampilkan views dari `id` masing-masing data, tambahkan fungsi berikut pada `views.py`:
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
dan path berikut pada `urls.py` aplikasi:
```python
...
urlpatterns = [
    ...
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id') 
]
...
```


## Apa perbedaan antara form POST dan form GET dalam Django?
Dalam Django, form POST dan form GET memiliki beberapa perbedaan utama:

1. **Form POST**: Form POST dalam Django dikembalikan menggunakan metode POST, di mana browser mengumpulkan data formulir, meng-*encode*-nya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya1. Metode POST akan mengirimkan data atau nilai langsung ke file lain2. Pemakaian metode POST ini digunakan untuk mengirimkan data yang penting / kredensial dan data yang orang lain tidak boleh tau / *secret data*, seperti password, dan sebagainya2.

2. **Form GET**: Sebaliknya, GET mengumpulkan data yang dikirimkan menjadi sebuah string, dan menggunakan ini untuk menyusun URL1. Metode GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action3.

Secara umum, metode POST digunakan saat kita ingin mengirimkan data yang tidak boleh dilihat oleh pengguna lain (misalnya password), sedangkan metode GET digunakan saat kita ingin pengguna dapat melihat data yang dikirimkan (misalnya dalam pencarian).

referensi: [Django - Working with forms](https://docs.djangoproject.com/en/4.2/topics/forms/)

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML adalah tiga format yang sering digunakan dalam pengiriman data di web. Berikut adalah perbedaan utama antara ketiganya:

1. XML (eXtensible Markup Language):

    - XML adalah bahasa markup yang menyediakan aturan untuk menentukan data apa pun.
    - XML menggunakan tanda untuk membedakan antara atribut data dan data aktual.
    - XML merepresentasikan data dalam pola struktur *tree*.
    - XML memisahkan data dari HTML.
    - XML menyederhanakan proses perubahan platform.

2. JSON (JavaScript Object Notation):
    - JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin
    - JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi
    - JSON menggunakan pasangan key-value untuk merepresentasikan data
    - JSON mendukung dan didukung semua browser.

3. HTML (HyperText Markup Language):

    - HTML adalah bahasa markup standar untuk dokumen yang dirancang untuk ditampilkan di browser web.
    HTML tidak dirancang sebagai format pertukaran data, tetapi sebagai format untuk menampilkan data, dengan fokus pada bagaimana data tampak bagi pengguna akhir.
    - HTML menggunakan tag yang dikelilingi oleh tanda kurung sudut (< dan >) untuk membuat elemen.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Dalam konteks pengiriman data, baik XML dan JSON digunakan secara luas. Namun, JSON dianggap lebih efisien karena data direpresentasikan sebagai objek JavaScript, dan dengan demikian beberapa bit dilewatkan melalui kabel. Lebih sedikit waktu mesin diperlukan untuk pemrosesan data.

Singkatnya, JSON adalah format pertukaran data yang lebih baik, sedangkan XML adalah format pertukaran dokumen yang lebih baik. HTML biasanya tidak digunakan untuk pertukaran data, tetapi lebih fokus pada menampilkan data ke pengguna.

### Postman

HTML

![Alt Text](md_image/HTML.png)

XML

![Alt Text](md_image/XML.png)

JSON

![Alt Text](md_image/JSON.png)

XML by ID
![Alt text](md_image/XML_ID.png)

JSON by ID
![Alt text](md_image/JSON_ID.png)
</details>