# Pretty Little Things 
### by Georgina Elena Shinta Dewi Achti - 2206810995

Projek ini dibuat dengan tujuan memenuhi Tugas 2 Pemrograman Berbasis Platform. Link app dapat di akses [di sini](https://prettylittlethings-co.adaptable.app).

Saya akan menjelaskan beberapa poin-poin berikut:
1. Implementasi dalam proses pembuatan proyek Django: PrettyLittleThings-Co
2. Bagan request client ke web aplikasi berbasis Django beserta responnya
3. Alasan penggunaan Virtual Environment
4. Penjelasan terkait MVC, MVT, MVVM serta perbedaan dari ketiganya

# Implementasi dalam proses pembuatan proyek Django: PrettyLittleThings-Co
<details>
<summary>Pembuatan Projek Django</summary> 
Membuat suatu repository baru di GitHub dengan nama "PrettyLittleThings-Co" lalu diclone di local. Kemudian saya membuat file `requirements.txt` pada folder direktori local saya dan menuliskan requirements yang diperlukan dari tutorial, yaitu:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Setelah itu, saya lanjut untuk mendownload dengan menjalankan command:
1. `python3 -m venv env ` -> untuk membuat virtual environment
2. `source env/bin/activate` -> mengaktifasi virtual environment
3. `pip3 install -r requirements.txt` -> menginstall module Django di virtual environment.
4. `django-admin startproject inventory_co .` -> membuat proyek Django

Pada poin terakhir, command tersebut nantinya akan berisi file-file pendukung proyek.

Setelah itu saya menguji deploy di localhost dengan melakukan command`./manage.py runserver` lalu klik `http://localhost:8000`. Jika terlihat ada roket dengan tulisan succesful, maka deploy berhasil🤩
</details>
<details>
<summary>Membuat dan Menjalankan Aplikasi</summary> 
Selanjutnya, saya mengubah `ALLOWED_HOSTS` di file `settings.py` dengan menambahkan `"*"` agar proyek ini bisa dijalankan di domain apapun:

```
ALLOWED_HOSTS = ["*"]
```

jalankan command:

```
python3 manage.py startapp main
```

sehingga terbentuk folder `main` di root repository. Tambahkan nama aplikasi di folder `inventory_co` di file `settings.py` pada bagian `INSTALLED_APPS`, seperti berikut:

```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
</details>
<details>
<summary>Membuat Model Aplikasi Main</summary> 
Saya melakukan modifikasi pada file `models.py` di folder `main` dengan menambahkan kode;

```
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

Kemudian, agar Django dapat menyesuaikan struktur basis data dengan model yang baru dibuat, lakukan migrate dengan menjalankan command:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Maka, model pada aplikasi dan basis data telah sesuai dengan yang kita inginkan.
</details>

<details>
<summary>Melakukan Routing</summary> 
Proses routing dilakukan melalui file `urls.py` pada folder main dengan mengisi dengan kode berikut:

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Function `show_main` bertujuan untuk menampilkan aplikasi dengan mengakses `main.views`. Lalu, lakukan proses routing pada file `urls.py` di direktori `inventory_co` dan isi dengan kode:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls'))
]
```

</details>
<details>
<summary>Membuat Fungsi main.html dan views.py</summary>

</details>


<details>
<summary>Melakukan Deployment</summary>
Cek kembali aplikasi sebelum melakukan deployment dengan menjalankan command:

```
python3 manage.py runserver
```

lalu masuk ke server `http://localhost:8000/main/`

Jika aplikasi dapat berjalan dengan baik, lanjutkan dengan melakukan add, commit, dan push ke dalam repository:

```
git add .
git commit -m "the main app"
git push -u origin master
```

Terakhir, saya melakukan deploy di Adaptable. Dimulai dengan  menggunakan Python App Template dengan menklik `+NEW APP`, lalu connect dengan repositori pilihan, kemudian memilih `Python App Template`, kemudian pilih opsi `PostgreSQL`. Kalian diminta untuk mengecek python version kalian dengan command:

```
python3 --version
```

Setelah itu, isi bagian command dengan:

```
python manage.py migrate && gunicorn PrettyLittleThings-Co.wsgi
```

Tunggu aplikasi hingga proses deploy selesai.
</details>


# Bagan request client ke web aplikasi berbasis Django beserta responnya
![](https://i.imgur.com/ltmg32e.png)
Terdapat komponen `client`, `urls.py`, `views.py`, `models.py`, serta berkas html `main.html` yang menjadi bagian dari berjalannya sistem. Sistem dimulai dengan **request** yang dikirimkan oleh `client` ke `urls.py` untuk mengolah file request yang kemudian dilanjutkan ke `views.py`. Pada `views.py` memproses data, mengambil data dari database, kemudian lanjut ke `models.py` dan merender berkas `main.html`. Setelah template data berhasil dirender, halaman akan dikembalikan sebagai HTTP Response kepada client.


# Alasan penggunaan Virtual Environment
Virtual environment digunakan dalam pengembangan Python (termasuk aplikasi web berbasis Django) karena memiliki beberapa manfaat:

- **Isolasi Dependensi**: Virtual environment memungkinkan kita untuk menciptakan lingkungan pengembangan yang terisolasi sehingga memungkinkan setiap proyek memiliki dependensi dan paket Python yang independen. Dengan demikian, kita dapat mencegah konflik antara versi paket yang berbeda di berbagai proyek. Dalam virtual environment, kita dapat menginstal, menghapus, atau memperbarui paket Python secara terpisah untuk setiap proyek yang membuat manajemen dependensi proyek menjadi lebih mudah dan meminimalkan risiko masalah kompatibilitas.

- **Reproducible Environment**: membuat environment pengembangan yang dapat direplikasi dengan mudah di mesin lain atau oleh rekan tim. Ini penting untuk memastikan bahwa suatu proyek dapat dijalankan dengan benar di berbagai lingkungan.

- **Keamanan dan Stabilitas**: Virtual environment melindungi sistem operasi dari perubahan tak terduga yang dapat disebabkan oleh proyek Python yang tidak terkendali. Ini memastikan stabilitas lingkungan pengembangan proyek.

Tanpa virtual environment, kita tetap dapat membuat aplikasi web berbasis Django. Namun, sangat tidak disarankan karena tanpa virtual environment, terdapat beberapa risiko serta potensi masalah yang dapat terjadi, seperti:

- **Konflik Dependensi**: Proyek Django yang berbeda mungkin memerlukan versi yang berbeda dari paket Python atau library tertentu. Tanpa virtual environment, proyek-proyek tersebut dapat saling mempengaruhi dan menimbulkan konflik dependensi.

- **Kesulitan Manajemen Dependensi**: Manajemen dependensi proyek akan menjadi lebih sulit karena kita harus memantau dan mengelola semua dependensi global di tingkat sistem.

- **Kurangnya Reproducibility**: Tanpa virtual environment, akan sulit untuk memastikan bahwa proyek dapat dijalankan dengan benar di lingkungan pengembangan yang berbeda, yang dapat menghasilkan masalah ketika kita ingin berbagi proyek atau mengerjakannya di mesin lain.


# Penjelasan terkait MVC, MVT, MVVM serta perbedaan dari ketiganya
MVC, MVT, dan MVVM adalah tiga arsitektur desain yang digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi web. Mereka memiliki konsep yang mirip dalam pemisahan tanggung jawab dalam pengembangan perangkat lunak, tetapi memiliki perbedaan dalam implementasi dan fokus.

**MVC (Model-View-Controller):**

1. **Model**: Mewakili data dan logika bisnis aplikasi. Ini mengelola data dan berisi logika yang berhubungan dengan pemrosesan data.

2. **View**: Bertanggung jawab untuk tampilan dan presentasi data kepada pengguna. Ini adalah antarmuka pengguna yang digunakan untuk menampilkan informasi.

3. **Controller**: Mengontrol alur aplikasi dan mengatur interaksi antara Model dan View. Ini menerima input dari pengguna dan mengirimkannya ke Model atau View yang sesuai.

**MVT (Model-View-Template):**

1. **Model**: Sama dengan MVC, mewakili data dan logika bisnis. Ini mengelola data dan berisi logika yang berhubungan dengan pemrosesan data.

2. **View**: Sama dengan MVC, bertanggung jawab untuk tampilan dan presentasi data. Ini adalah antarmuka pengguna yang digunakan untuk menampilkan informasi.

3. **Template**: Ini adalah bagian yang berbeda dari MVC. Template mengontrol tampilan secara langsung dan memungkinkan pengembang untuk memisahkan logika presentasi dari tampilan.

**MVVM (Model-View-ViewModel):**

1. **Model**: Sama dengan MVC dan MVT, mewakili data dan logika bisnis. Ini mengelola data dan berisi logika yang berhubungan dengan pemrosesan data.

2. **View**: Sama dengan MVC dan MVT, bertanggung jawab untuk tampilan. Ini adalah antarmuka pengguna yang digunakan untuk menampilkan informasi.

3. **ViewModel**: Ini adalah lapisan yang memediasi antara Model dan View. ViewModel mengubah data Model ke format yang dapat ditampilkan oleh View. Ini memungkinkan pemisahan yang kuat antara tampilan dan data, serupa dengan Template dalam MVT.

Perbedaan utama antara ketiganya adalah dalam implementasi dan penekanannya pada pemisahan tugas. 

- **MVC** lebih tentang pemisahan peran antara Model, View, dan Controller, tetapi sering kali tugas Controller menjadi kompleks dalam aplikasi yang besar.

- **MVT** mirip dengan MVC, tetapi menggunakan Template untuk mengelola tampilan, yang memungkinkan pemisahan logika presentasi dari tampilan.

- **MVVM** lebih mengenai pemisahan data dan tampilan. ViewModel bertanggung jawab untuk memformat data dari Model agar sesuai dengan tampilan View, sehingga tampilan tidak perlu memiliki logika pemformatan data.

Django, sebagai framework Python untuk pengembangan web, biasanya lebih sesuai dengan arsitektur MVT.