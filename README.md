# Pretty Little Things 
### by Georgina Elena Shinta Dewi Achti - 2206810995
berikut merupakan hasil pengerjaan Tugas Pemrograman Berbasis Platform.

<details>
<summary>Tugas 2: Implementasi Model-View-Template (MVT) pada Django</summary>

# TUGAS 2📕
Projek ini dibuat dengan tujuan memenuhi Tugas 2 Pemrograman Berbasis Platform. Link app dapat di akses [di sini](https://prettylittlethings-co.adaptable.app).

Saya akan menjelaskan beberapa poin-poin berikut:
1. Implementasi dalam proses pembuatan proyek Django: **PrettyLittleThings-Co**
2. Bagan request client ke web aplikasi berbasis Django beserta responnya
3. Alasan penggunaan Virtual Environment
4. Penjelasan terkait MVC, MVT, MVVM serta perbedaan dari ketiganya

## Implementasi dalam proses pembuatan proyek Django: PrettyLittleThings-Co
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
<summary>Membuat Fungsi main.html dan views.py</summary>
Saya membuat direktori baru bernama `templates` di dalam direktori aplikasi main. Di dalam direktori `templates`, saya membuat berkas baru bernama `main.html` dengan isi:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hi! It's Pretty Little Things Here~</title>
</head>
<body>
    <h1>{{judul}}</h1>

    <h5>Seller name: </h5>
    <p>{{ name }}<p>

    <h5>The Items: </h5>
    <p>{{ item }}<p>

    <h5>Price: </h5>
    <p>{{ price }}<p>

    <h5>Address: </h5>
    <p>{{ adress }}<p>

</body>
</html>
```

Kemudian pada file `views.py` pada aplikasi `main` saya menambahkan impor:

```
from django.shortcuts import render
```

serta menambahkan fungsi `show_main` sebagai berikut:

```
def show_main(request):
    context = {
        'judul': 'Hi! It is Pretty Little Things Here~',
        'name': 'Elena',
        'item': 'DIY Bracellet',
        'amount': '10',
        'price': ' Rp10.000,-',
        'adress': 'Jl. Yu'
    }

    return render(request, "main.html", context)
```

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


## Bagan request client ke web aplikasi berbasis Django beserta responnya
![](https://i.imgur.com/ltmg32e.png)
Terdapat komponen `client`, `urls.py`, `views.py`, `models.py`, serta berkas html `main.html` yang menjadi bagian dari berjalannya sistem. Sistem dimulai dengan **request** yang dikirimkan oleh `client` ke `urls.py` untuk mengolah file request yang kemudian dilanjutkan ke `views.py`. Pada `views.py` memproses data, mengambil data dari database, kemudian lanjut ke `models.py` dan merender berkas `main.html`. Setelah template data berhasil dirender, halaman akan dikembalikan sebagai HTTP Response kepada client.


## Alasan penggunaan Virtual Environment
Pada Django, virtual environment memiliki banyak manfaat yang digunakan dalam pengembangan Python bagi para pengguna. Manfaat berupa:

- **Isolasi Dependensi.**
    Dapat memungkinkan kita untuk menciptakan lingkungan pengembangan terisolasi di mana setiap proyek memiliki dependensi Python yang independen sehingga dapat menghindari konflik antara versi paket yang berbeda di berbagai proyek. Dalam virtual environment, kita dapat mengelola data secara terpisah untuk setiap proyek, membuat manajemen dependensi lebih mudah, dan mengurangi risiko masalah kompatibilitas.

- **Reproducible Environment.**
    Dapat membuat environment pengembangan yang dapat direplikasi dengan mudah di mesin lain atau oleh rekan tim. Hal ini dapat memastikan bahwa suatu proyek mampu dijalankan dengan benar di berbagai environment.

- **Keamanan dan Stabilitas.**
    Dapat melindungi sistem operasi dari perubahan tak terduga yang dapat disebabkan oleh proyek Python yang tidak terkendali. Hal ini dapat menjaga stabilitas dari environment proyek yang sedang kita jalankan.

Tanpa virtual environment, kita tetap dapat membuat aplikasi web berbasis Django. Namun, sangat tidak disarankan karena tanpa virtual environment, terdapat beberapa risiko serta potensi masalah yang dapat terjadi, seperti:

- **Konflik Dependensi.**
    Proyek Django yang berbeda mungkin memerlukan versi yang berbeda dari paket Python atau library tertentu sehingga proyek-proyek tersebut dapat saling mempengaruhi dan menimbulkan konflik dependensi.

- **Kesulitan Manajemen Dependensi.**
    Manajemen dependensi proyek akan menjadi lebih sulit karena kita harus memantau dan mengelola semua dependensi global di tingkat sistem.

- **Kurangnya Reproducibility.**
    Sulit memastikan bahwa proyek dapat dijalankan dengan benar di environment pengembangan yang berbeda sehingga menimbulkan kemungkinan masalah ketika kita ingin berbagi proyek atau mengerjakannya di tempat lain.


## Penjelasan terkait MVC, MVT, MVVM serta perbedaan dari ketiganya
MVC, MVT, dan MVVM adalah tiga arsitektur desain yang digunakan dalam pengembangan perangkat lunak, terutama dalam pengembangan aplikasi web. 

### MVC (Model-View-Controller):
1. **Model** -> mengelola data dan berisi logika untuk pemrosesan data.

2. **View** -> tampilan dan presentasi data kepada pengguna untuk menampilkan informasi.

3. **Controller** -> mengontrol alur aplikasi dan mengatur interaksi antara Model dan View.

### MVT (Model-View-Template):

1. **Model** -> mengelola data dan berisi logika untuk pemrosesan data.

2. **View** -> tampilan dan presentasi data kepada pengguna untuk menampilkan informasi.

3. **Template** -> mengontrol tampilan secara langsung dan memungkinkan pengembang untuk memisahkan logika presentasi dari tampilan.

## MVVM (Model-View-ViewModel):

1. **Model** -> mengelola data dan berisi logika untuk pemrosesan data.

2. **View** -> tampilan dan presentasi data kepada pengguna untuk menampilkan informasi.

3. **ViewModel** -> mengubah data Model ke format yang dapat ditampilkan oleh View.

Terdapat beberapa perdebaan dari MVC, MVT, dan MVVM. MVC lebih mengarah ke pemisahan peran antara Model, View, dan Controller, tetapi sering kali tugas Controller menjadi kompleks dalam aplikasi yang besar. MVT menggunakan Template untuk mengelola tampilan, yang memungkinkan pemisahan logika presentasi dari tampilan. Terakhir, MVVM lebih mengarah ke pemisahan data dan tampilan dimana ViewModel bertanggung jawab untuk memformat data dari Model agar sesuai dengan tampilan View, sehingga tampilan tidak perlu memiliki logika pemformatan data. Mereka memiliki konsep yang mirip dalam pemisahan tanggung jawab dalam pengembangan perangkat lunak, tetapi memiliki perbedaan dalam implementasi dan penekanannya pada pemisahan tugas.
</details>

<details>
<summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>

# TUGAS 3📗
Projek ini dibuat dengan tujuan memenuhi Tugas 3 Pemrograman Berbasis Platform.

Saya akan menjelaskan beberapa poin-poin berikut:
1. Perbedaan antara form POST dan form GET dalam Django
2. Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
3. Alasan mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
4. Penjelasan cara saya mengimplementasikan lanjutan proses pembuatan proyek **PrettyLittleThings-Co**

## form `POST` vs form `GET` in Django

`Form` adalah elemen HTML yang digunakan untuk mengumpulkan data dari pengguna, seperti input teks, tombol radio, atau checkbox yang memungkinkan pengguna untuk mengirim data ke _web server_ untuk diproses.

| Perbedaan | Post | Get |
| ------- | ------- | ------- |
| Pengiriman Data | Mengirim data sebagai bagian dari permintaan HTTP dan bersifat tersembunyi  | Mengirim data melalui query string dalam URL |
| Keamanan | Lebih aman karena data tidak terlihat di URL | data ditampilkan secara terbuka dalam URL |
| Penggunaan | Membuat, memperbarui, atau menghapus data sehingga cocok untuk mengirim data sensitif | Melakukan pencarian atau menampilkan data sehingga cocok untuk permintaan yang hanya mengambil data dari server tanpa mengubahnya|
| Kapasitas Data | Dapat mengirim jumlah data yang lebih besar karena data disimpan di tubuh permintaan | Dibatasi oleh panjang URL sehingga kurang cocok untuk data yang besar |

## `XML` vs `JSON` vs `HTML` dalam Pengiriman Data
| Perbedaan | XML | JSON | HTML |
| --------- | --- | ---- | ---- |
| Singkatan | eXtensible Markup Language | JavaScript Object Notation | HyperText Markup Language |
| Tujuan |  dirancang terutama untuk menyimpan, mengirimkan, dan mengatur data | merepresentasikan data dengan format sederhana yang mudah dibaca mesin dan manusia dengan menyajikan pasangan key-value di dalam suatu array | mendefinisikan tata letak, konten, serta visual halaman web yang mencakup elemen seperti judul, paragraf, daftar, tautan, dan komponen multimedia |
| Penggunaan | Digunakan dalam pertukaran data antara sistem yang berbeda dan perlu menggambarkan data yang kompleks dan terstruktur dengan baik | Digunakan dalam pengembangan aplikasi web karena mudah dibaca oleh manusia dan mudah digunakan oleh bahasa pemrograman modern | Digunakan untuk menampilkan konten web sehingga dapat diakses oleh browser web |


## `JSON` sering digunakan dalam Pertukaran Data antara App Web Modern?!
Seperti yang telah dibahas sebelumnnya, `JSON` (JavaScript Object Notation) merupakan format Bahasa-Independen yang berasal dari JavaScript yang dapat dibaca dan ditulis oleh manusia. Terdapat beberapa kegunaan dari `JSON`, yaitu:
- **Transfer data dengan mudah.**
Menyimpan semua data dalam array sehingga transfer data menjadi lebih mudah. Itu sebabnya `JSON` sangat baik untuk berbagi data dengan ukuran berapa pun, termasuk audio, video, dan lain-lain.
- **Ringan dan Mudah dibaca.** 
Sintaksnya sangat kecil, mudah, dan ringan sehingga menjadi alasan mengeksekusi dan merespons dengan cara yang lebih cepat.
- **Dukungan Bahasa Pemrograman.** 
`JSON` didukung oleh hampir semua bahasa pemrograman, sehingga memungkinkan interoperabilitas yang baik antara berbagai teknologi dan aplikasi. `JSON` memiliki jangkauan luas untuk dukungan browser kompatibilitas dengan sistem operasi sehingga tidak memerlukan banyak usaha untuk membuat semuanya kompatibel dengan browser.
- **Dukungan untuk Nested Data.** 
`JSON` mendukung data berjenjang (nested) yang memungkinkan representasi data yang kompleks dan terstruktur dengan mudah. Hal ini berguna dalam situasi di mana data memiliki hubungan hierarkis. 

# Implementasi Data
_notes: terdapat perubahan nama variabel/objek dari Tugas 2, yaitu `Item` menjadi `Product` di Tugas 3._
<details>
<summary>Membuat Input Form</summary>

Kita perlu membuat form untuk mendapatkan data baru yang ingin ditampilkan. Sebelum itu, saya membuat direktori baru pada **root** dengan nama `templates` yang di dalamnya terdapat file `base.html` yang berisi:

```
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
Saya melakukan konfigurasi pada `settings.py` di direktori `inventory_co` agar `base.html` terdeteksi sebagai template dengan menambahkan:

```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```

Kemudian, saya mengubah `main.html` pada direktori `main/templates` terlebih dahulu agar dapat menggunakan `base.html` sebagai template dasarnya dengan kode:

```
{% extends 'base.html' %}

{% block content %}
    <h1>{{judul}}</h1>

    <h5>Seller name: </h5>
    <p>{{ name }}<p>

    <h5>The Items: </h5>
    <p>{{ item }}<p>

    <h5>Price: </h5>
    <p>{{ price }}<p>

    <h5>Address: </h5>
    <p>{{ adress }}<p>

{% endblock content %}
```

Selanjutnya, saya sudah dapat fokus untuk membuat input form. Saya membuat berkas `forms.py` pada direktori `main` kemudian mengisi file dengan:

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]

```

Selanjutnya, saya mengubah fungsi `show_main` dan menambahkan fungsi `create_product` pada file `views.py` dalam direktori `main` dengan kode berikut:

```
def show_main(request):
    products = Product.objects.all()

    context = {
        'judul': 'Hi! It is Pretty Little Things Here~',
        'name': 'Elena',
        'item': 'DIY Bracellet',
        'amount': '10',
        'price': ' Rp10.000,-',
        'adress': 'Jl. Yu',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

```
Fungsi `create_product` menangani input baru dari form yang akan membuat sebuah objek **ProductForm** berdasarkan data yang diterima dari `request.POST` (data yang dikirimkan melalui form). Lalu, diperiksa kembali apakah form tersebut valid dengan menggunakan `form.is_valid()` dan apabila valid dan metode request adalah POST, data produk baru akan disimpan ke database melalui `form.save()`, kemudian pengguna akan diarahkan kembali ke halaman utama dengan **HttpResponseRedirect**.

Berikutnya, saya membuat file `create_product.html` pada direktori `main` yang berisi:
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/> # tombol
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
yang akan menampilkan halaman form untuk menambah item baru. File ini mencakup form dengan token CSRF, bidang-bidang form, dan tombol "Add Product" yang mengirimkan data form ke view create_product.

Kemudian pada `main.html` di direktori `main`, saya menambahkan kode:

```
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}"> # tombol
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```
untuk menampilkan data produk yang diterima dari view `show_main` dalam bentuk tabel, serta tombol yang akan mengarahkan user pada halaman form penambahan product.


</details>

<details>
<summary>Menambahkan Fungsi pada Views</summary>

Saya menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format `HTML`, `XML`, `JSON`, `XML` by **ID**, dan `JSON` by **ID**. Untuk format `XML` dan `JSON`, saya akan menambahkan import **HttpResponse** dan **serializers** pada `views.py`di folder `main`.

Format `HTML`:
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'judul': 'Hi! It is Pretty Little Things Here~',
        'name': 'Elena',
        'item': 'DIY Bracellet',
        'amount': '10',
        'price': ' Rp10.000,-',
        'adress': 'Jl. Yu',
        'products': products
    }

    return render(request, "main.html", context)
```
`products = Product.objects.all()` mengambil semua objek Product dari database dengan Product.objects.all() dan menyimpannya dalam variabel product. Data item kemudian disertakan dalam konteks dan akan ditampilkan dalam template HTML `main.html`.


Format `XML`:

```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

Format `JSON`:

``` 
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```


Format `XML` by **ID**:

```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

Format `JSON` by **ID**:
``` 
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
</details>
<details>
<summary>Membuat Routing URL</summary>

Tambahkan kelima path **url** fungsi diatas ke dalam **urlpatterns** pada `urls.py` di folder `main`. Tidak lupa untuk meng-import-nya dari `views.py`.

``` 
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```

Dengan begitu, input form sudah selesai dibuat dan siap digunakan. Jalankan command `python manage.py runserver` dan kunjungi http://localhost:8000.
</details>

<details>
<summary>Postman Screenshot</summary>

1. Screenshot `HTML`
![](https://i.imgur.com/BSpmURi.png)
![](https://i.imgur.com/XN5WnWL.png)

2. Screenshot `XML`
![](https://i.imgur.com/utbizIL.png)

3. Screenshot `XML` by **ID**
![](https://i.imgur.com/6qx8lbV.png)

4. Screenshot `JSON`
![](https://i.imgur.com/9LOAx1D.png)

5. Screenshot `JSON` by **ID**
![](https://i.imgur.com/h7u3xHo.png)

</details>
</details>

<details>
<summary> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </summary>

# Tugas 4📙
Projek ini dibuat dengan tujuan memenuhi Tugas 3 Pemrograman Berbasis Platform.

Saya akan menjelaskan beberapa poin-poin berikut:

- Apa itu Django UserCreationForm, serta apa kelebihan dan kekurangannya
- Perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan alasan mengapa keduanya penting
- Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna
- Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- Cara saya mengimplementasikan checklist di atas secara step-by-step.

## Django `UserCreationForm`🧐
 Django `UserCreationForm` adalah sebuah form Django yang digunakan untuk membuat user baru di dalam suatu web app. `UserCreationForm` umumnya memiliki 3 field, yaitu `username`, `password1`, dan `password2`. Field `password2` biasanya digunakan untuk mengonfirmasi password sebelumya.

| Kelebihan | Kekurangan |
| --------- | ---------- |
| mudah digunakan karena merupakan default form dari Django sehingga tidak perlu membuat model form lagi dan data pendaftar dapat langsung disimpan di database. | tidak customizable secara ekstensif karena memiliki tingkat kustomisasi yang terbatas sehingga membutuhkan model form dengan field tambahan atau logika validasi yang lebih kompleks sehingga untuk penambahan field lain dan perubahan tampilan harus dilakukan perubahan sendiri. |
| validasi otomatis yang mana data yang dimasukkan oleh pengguna, yaitu keunikan nama pengguna, kata sandi yang cukup kuat, dll akan melakukan validasi secara otomatis. | |
| secara langsung berintegrasi dengan Django's _authentication system_ yang membuat mudah untuk menambahkan sistem autentikasi ke dalam aplikasi Django. | |

## Autentikasi 🆚 Otorisasi dalam Konteks Django
**PERBEDAAN👐🏻**
- Autentikasi adalah proses verifikasi siapa user yang berusaha menggunakan akses yang melibatkan verifikasi nama pengguna (username) dan kata sandi (password) yang dimasukkan oleh pengguna sesuai dengan yang ada dalam database. 
- Otorisasi adalah proses verifikasi user yang telah diautentikasi apakah dapat mengakses suatu sistem sehingga proses ini memutuskan apa yang diperbolehkan atau tidak diperbolehkan untuk pengguna yang sudah terautentikasi. 

**Mengapa Keduanya Penting?**

Autentikasi penting untuk memastikan bahwa pengguna yang masuk adalah pengguna yang sah, sedangkan otorisasi penting untuk mengontrol hak akses pengguna dalam aplikasi. Dengan kombinasi autentikasi dan otorisasi, kita dapat memastikan bahwa pengguna hanya dapat mengakses bagian dari aplikasi yang sesuai dengan izin mereka untuk menjaga keamanan serta privasi data.

## Cookies dalam Konteks Aplikasi Web Django🍪✨
**Apa itu Cookies🤔💭?**

Cookies adalah penyimpanan data client yang disimpan oleh server web dan dikirim kembali ke server setiap kali permintaan dilakukan. Jadi, penyimpanan bersifat **sementara** karena data hanya tersimpan ketika pengguna sedang melakukan interaksi di dalam aplikasi web. Cookies mengandung informasi tertentu, seperti pengenal sesi atau preferensi pengguna, dan disimpan dalam penyimpanan lokal browser. 

**Cara Django Menggunakan Cookies untuk Mengelola Data Sesi Pengguna**

Cookies dikelola dengan struktur seperti **map** yang terdiri dari **key** dan **value** berupa user dan data yang disimpan. Untuk menjaga keamanan data, pada Django juga terdapat expiration date sehingga ketika pengguna sudah keluar dari aplikasi web, seluruh data pengguna juga akan dinonaktifkan. Umumnya, cookies digunakan untuk menyimpan informasi sementara seperti ID sesi, preferensi pengguna, atau informasi lain yang diperlukan untuk interaksi selama sesi pengguna.

## Keamanan Penggunaan Cookies dalam Pengembangan Web
Cookies disimpan pada browser client sehingga keamanan sebenarnya tergantung pada browser milik client. Selain itu, cookies juga dapat dilihat secara langsung oleh pengguna sehingga data yang disimpan tidak aman jika digunakan untuk menyimpan sesuatu yang sifatnya **private**.

Beberapa resiko potensial yang harus diwaspadai terhadap keamanan cookies adalah adanya Cookie Theft yaitu pencurian cookies karena mendapat akses ilegal ke cookies pengguna. Umumnya menyerang informasi pengguna yang bersifat private seperti ID, validation token, dan lain-lain sehingga sesi pengguna dapat diambil alih.

Beberapa risiko potensial yang terkait dengan penggunaan cookies, berupa:
- **Cross-Site Scripting (XSS)**. Terjadi ketika data yang disimpan dalam cookies tidak dihindari atau disaring dengan benar. Penyerang dapat memasukkan kode skrip berbahaya ke dalam cookies yang akan dieksekusi oleh browser pengguna saat cookies tersebut digunakan.
- **Session Hijacking**. Terjadi ketika cookies digunakan untuk mengelola sesi pengguna dan tidak dienkripsi dengan baik, ada risiko sesi pengguna yang dapat dicuri oleh penyerang dan penyerang masuk ke akun pengguna tanpa izin.
- **Man-in-the-Middle (MitM) Attacks**. Terjadi ketika koneksi antara pengguna dan server tidak aman (contoh, tanpa HTTPS) sehingga cookies dapat disadap oleh penyerang saat transit. 

## Implementasi Data💻
<details>
<summary>Implementasi fungsi Registrasi, Log in, dan Log out</summary>

Untuk mengimplementasikan fungsi registrasi, login, dan logout, pada subdirektori `main` di `views.py` saya menambahkan:
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
```

Setelah mengimpor, saya juga mendefinisikan masing-masing functionnya, seperti:
- `register(request)` -> menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- `login_user(request)` -> mengautentikasi pengguna yang ingin login.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) #cookie
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

- `logout_user(request)` -> melakukan mekanisme logout.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login') #cookie
    return response
```

Kemudian, pada subdirektori `main/templates` saya membuat file:
- `register.html` dengan kode:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
- `login.html` dengan kode:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Kemudian, pada subdirektori `main` di `views.py` saya mengimport `from django.contrib.auth.decorators import login_required` dan  mengatur bagian `login_required` pada bagian atas `show_main`:
```
@login_required(login_url='/login')
def show_main(request):
...
```

Lalu, saya menyambungkannya ke file urls.py untuk setiap path register, login, dan logout, seperti berikut:
- import:
```
from main.views import register 
from main.views import login_user
from main.views import logout_user
```
- di dalam `urlpatterns`
```
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ...
```

</details>
<details>
<summary>Membuat dua akun pengguna dengan masing-masing tiga dummy data </summary>

Saya melakukan uji coba dengan menjalankan program pada http://localhost:8000/ dan memanfaatkan fungsi register untuk mendaftarkan 2 akun baru, yaitu `georginaelena` dan `georginaelena_2`. Kemudian, untuk masing-masing akun yang telah dibuat, saya menerapkan fungsi login, menambahkan masing-masing 3 dummy data, dan menerapkan fungsi logout. Berikut tampilan website pada kedua akun:
- user: `georginaelena`
![](https://i.imgur.com/jasrAtb.png)

- user: `georginaelena_2`
![](https://i.imgur.com/z77W0VM.png)

</details>
<details>
<summary>Menghubungkan model Product dengan User</summary>

Dalam menghubungkan model Product dengan User, pertama-tama  pada `models.py` dalam subdirektori `main`, saya mengimpor:
```
...
from django.contrib.auth.models
...
```
untuk mengimport User ke dalam `models.py`. Setelah itu, pada Product saya tambahkan:
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Simpan semua perubahan, dan lakukan migrasi model dengan `python manage.py makemigrations` dan ` python manage.py migrate`.
Lalu, mengubah kode di views.py untuk create_item dan show_main sebagai berikut:
```
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user) #menambahkan ini

    context = {
        'judul': 'Hi! It is Pretty Little Things Here~',
        'name': request.user.username, #menambahkan ini
        'item': 'DIY Bracellet',
        'amount': '10',
        'price': ' Rp10.000,-',
        'adress': 'Jl. Yu',
        'products': products,
        'last_login': request.COOKIES['last_login'], #cookie
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST": #mengubah ini
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Dengan ini, sudah terhubunglah model Product dengan User serta cookie dan context akan disesuaikan ke dalam HTML file. 

</details>
<details>
<summary>Menampilkan detail informasi pengguna yang sedang Logged in seperti Username dan menerapkan Cookies seperti Last Login di halaman utama aplikasi</summary>

Sebelumnya, saya telah mengatur cookie sehingga informasi pengguna yang sedang logged in dan last login hanya perlu diatur pada file HTML dengan menambahkan:
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
pada `main.html` untuk menampilkannya.

</details>


</details>
