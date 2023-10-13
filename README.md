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
Projek ini dibuat dengan tujuan memenuhi Tugas 4 Pemrograman Berbasis Platform.

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

<details>
<summary>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</summary>

# Tugas 5✋🏻
Projek ini dibuat dengan tujuan memenuhi Tugas 5 Pemrograman Berbasis Platform.

Saya akan menjelaskan beberapa poin-poin berikut:
- Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- HTML5 Tag yang saya ketahui.
- Perbedaan antara margin dan padding.
- Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya.
- Cara saya mengimplementasikan checklist secara step-by-step 

## Element Selector🤖
Element selector adalah cara untuk memilih atau menemukan elemen HTML yang ingin kita *style* berdasarkan tipe elemennya. Manfaat dalam hal:

- **Kesederhanaan**. Anda dapat mengatur *style default* untuk semua elemen dengan tipe yang sama. Element selector memungkinkan Anda untuk mengatur gaya untuk semua elemen HTML dengan tipe yang sama, seperti `<p>`, `<h1>`, atau `<div>`. Ini dapat membuat kode CSS Anda lebih sederhana dan mudah dipahami.
- **Kemudahan membaca**. Kode CSS lebih mudah dibaca karena mengikuti struktur HTML yang sudah ada, terutama bagi pengembang yang baru mengenal CSS.
- **Efisiensi**. Anda dapat mengurangi jumlah kode CSS yang perlu ditulis karena satu aturan CSS dapat berlaku untuk banyak elemen yang sama..

Waktu yang tepat untuk menggunakan element selector adalah saat pembuat ingin mengatur *style default* untuk tipe elemen HTML tertentu di seluruh situs web yang dimiliki serta ingin menghindari penggunaan kelas atau ID tambahan. Contohnya, jika Anda ingin mengubah warna teks untuk semua elemen `<p>`, Anda dapat menggunakan element selector `<p>`. Namun, perlu diingat bahwa penggunaan element selector dengan sangat luas dapat membuatnya sulit untuk menyesuaikan elemen individu jika Anda ingin mengubahnya secara berbeda. Oleh karena itu, lebih baik menggunakan kelas atau ID untuk membatasi cakupan gaya Anda dan memberikan lebih banyak fleksibilitas dalam desain.

## HTML5 Tag
HTML5 (Hypertext Markup Language versi 5) adalah bahasa markup versi terbaru yang digunakan untuk membuat dan merancang halaman web dimana memperkenalkan sejumlah elemen baru yang memberikan lebih banyak struktur dan semantik ke dalam dokumen web. Elemen-elemen ini membantu mengidentifikasi dan mengelompokkan konten dengan lebih baik. Berikut merupakan beberapa contoh HTML5 Tag yang saya gunakan pada tugas saya:

- **`<div>`**:
   - Fungsi: Digunakan untuk mengelompokkan dan memisahkan konten, sering digunakan untuk membuat wadah atau container.
   - Contoh:
     ```html
     <div id="container">
         <p>Ini adalah teks dalam div.</p>
     </div>
     ```

- **`<a>`**:
   - Fungsi: Digunakan untuk membuat tautan ke halaman web lain atau sumber daya online.
   - Contoh:
     ```html
     <a href="https://www.example.com">Kunjungi situs web kami</a>
     ```

- **`<p>`**:
   - Fungsi: Digunakan untuk menampilkan teks paragraf.
   - Contoh:
     ```html
     <p>Ini adalah contoh paragraf.</p>
     ```

- **`<img>`**:
   - Fungsi: Digunakan untuk menampilkan gambar pada halaman web.
   - Contoh:
     ```html
     <img src="gambar.jpg" alt="Deskripsi Gambar">
     ```


- **`<input>`**:
   - Fungsi: Digunakan untuk membuat elemen input dalam formulir.
   - Contoh:
     ```html
     <input type="text" name="nama" placeholder="Masukkan nama Anda">
     ```

- **`<button>`**:
   - Fungsi: Digunakan untuk membuat tombol pada halaman web.
   - Contoh:
     ```html
     <button type="button">Klik Saya</button>
     ```

- **`<form>`**, **`<input>`**, dan **`<button>`** (untuk membuat formulir):
   - Fungsi: Digunakan untuk membuat formulir interaktif yang memungkinkan pengguna mengirimkan data.
   - Contoh:
     ```html
     <form action="proses.php" method="post">
         <label for="nama">Nama:</label>
         <input type="text" id="nama" name="nama">
         <button type="submit">Kirim</button>
     </form>
     ```

- **`<h1>`, `<h2>`, `<h3>`, ..., `<h6>`** (untuk heading):
    - Fungsi: Digunakan untuk judul atau heading dengan tingkat kepentingan yang berbeda.
    - Contoh:
      ```html
      <h1>Judul Utama</h1>
      <h2>Subjudul</h2>
      <p>Isi teks...</p>
      ```

Penting untuk diingat bahwa meskipun HTML5 menawarkan banyak tag baru, penggunaan yang tepat dari tag bergantung pada konten dan struktur halaman web Anda. Anda harus memilih tag yang sesuai dengan semantik kontennya untuk meningkatkan aksesibilitas dan SEO.

## Margin vs Padding🔥
Perbedaan antara margin dan padding adalah bagaimana keduanya memengaruhi tata letak dan tampilan elemen HTML di halaman web. Ini adalah konsep penting dalam desain web dan CSS:

- **Margin:**
   - **Margin** adalah ruang di sekitar elemen HTML, yang merupakan jarak antara elemen tersebut dengan elemen lain di sekitarnya dengan kegunaan untuk mengatur jarak antara elemen dengan elemen-elemen lain di sekitarnya atau dengan tepi halaman.
   - **Margin** tidak memiliki latar belakang atau border, dan elemen-elemen dengan margin yang berdekatan akan memiliki jarak antara satu sama lain sesuai dengan margin masing-masing.

   Contoh penggunaan margin:
   ```css
   .elemen {
       margin: 10px; /* Margin sekitar elemen 10 piksel */
   }
   ```

- **Padding:**
   - **Padding** adalah ruang di sekitar isi dari elemen HTML, yang merupakan jarak antara konten elemen dan bordernya dengan kegunaan untuk mengatur jarak antara konten elemen dan batas atau bordernya.
   - **Padding** memengaruhi tampilan elemen dengan memberikan ruang di sekitar kontennya.

   Contoh penggunaan padding:
   ```css
   .elemen {
       padding: 10px; /* Padding untuk konten elemen 10 piksel */
   }
   ```

**Perbedaan Utama**

| Margin | Padding |
| ------ | ------- |
|  mempengaruhi jarak antara elemen dengan elemen-elemen di sekitarnya atau dengan tepi halaman. | mempengaruhi jarak antara konten elemen dengan bordernya. |
| tidak memiliki latar belakang atau border. | mempengaruhi bagian dalam elemen yang memiliki latar belakang atau border. |
|mempengaruhi tata letak elemen secara global. | mempengaruhi tampilan konten elemen secara lokal di dalamnya

Dalam desain web, pemahaman yang baik tentang perbedaan antara margin dan padding penting untuk mengontrol ruang dan tampilan elemen dengan tepat. Ini memungkinkan Anda untuk mengatur elemen-elemen di halaman web Anda sesuai dengan desain yang diinginkan.

##  CSS Tailwind vs Bootstrap
   Perbedaan antara Tailwind CSS dan Bootstrap
   - **BOOTSTRAP**
        - adalah kerangka kerja CSS yang lebih terstruktur dan datang dengan komponen UI yang siap pakai dengan desain bawaan yang kaya dengan komponen. Bootstrap memiliki gaya default yang mudah dikenali dimana tampilan khas "Bootstrap" yang dapat diubah dengan kustomisasi. Bootstrap memiliki ukuran yang lebih besar daripada Tailwind CSS karena komponen dan gaya default yang lebih banyak. 
        - Jadi, gunakanlah Bootstrap ketika pengembang memerlukan desain yang siap pakai dengan komponen UI yang lebih banyak, ingin menghemat waktu dalam pengembangan, serta pengembang masih termasuk kedalam kategori pemula dalam penggunaan CSS.
   - **TAILWIND CSS**
        -  adalah kerangka kerja CSS yang memberikan kontrol yang lebih besar kepada pengembang sehingga tidak memiliki banyak desain bawaan dan mengharuskan pengembang untuk membangun desain mereka dengan cara yang lebih granular menggunakan kelas CSS. Tailwind tidak memiliki gaya default yang kuat dimana seluruh elemen dimulai dengan tampilan yang sangat sederhana, dan pengembang harus menentukan semua gaya secara eksplisit. Namun, Tailwind memiliki ukuran yang lebih ringan karena hanya menyertakan kelas yang dibutuhkan dalam kode yang dihasilkan.
        - Jadi, gunakanlah Tailwind CSS ketika pengembang ingin total kontrol atas desain dan ingin menghindari gaya default yang berlebihan, telah memiliki pengalaman dalam menulis CSS dan ingin desain yang lebih kustom, serta ingin membangun tampilan yang ringan saja agar dapat memaksimalkan kinerja.

## Implementasi Data💻

Berikut merupakan implementasi pengerjaan Tugas 5:

<details>
<summary>Menambahkan Bootstrap ke Aplikasi</summary>

pada subdirektori `templates/base.html`, saya menambahkan tag `<meta name="viewport">`. Kemudian saya menambahkan:

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
```
</details>

<details>
<summary>Membuat Kostumisasi pada Aplikasi</summary>

pertama saya, membuat style pada subdirektori `templates/base.html` dengan kode:
```
...
<style>
            /* CSS untuk mengatur format tengah */
            body {
                background-color: #ffe1f4;
            }

            #login {
            display: flex;
            justify-content: center; /* Memposisikan elemen secara horizontal di tengah layar */
            align-items: center; /* Memposisikan elemen secara vertikal di tengah layar */
            padding-top: 50px;
            padding-bottom: 50px;
            background-color: #ffe1f4; /* Warna latar belakang */
            }
        
        
            .login {
                padding: 80px;
                max-width: 500px;
                background-color: #ffffff; /* Warna latar belakang elemen .login */
                border-radius: 10px; /* Border radius untuk sudut elemen */
                box-shadow: 0px 0px 10px rgba(255, 223, 248, 0.1); /* Efek bayangan */
            }

            .login form {
                margin-top: 10px;
            }
        
            .login table {
                margin-top: 10px; 
            }
        
            .login ul {
                margin-top: 20px;
            }

        </style>
...
```

style di atas merupakan format style untuk halaman `login`, `register`, dan `add_prodct`. Kemudian, pada masing-masing file yang ada di subdirektori `main/templates` saya berikan navbar dengan contoh implementasi berikut:
```
...
<!-- navbar untuk Login-->
<nav class="navbar bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="#" style="display: flex; align-items: center;">  <!-- agar posisi logo dan judul sejajar--> 
                    <img src="https://i.imgur.com/Oyp81gz.png" alt="Logo" class="d-inline-block align-text-top logo-img" style="width: 10%;"> <!-- agar ukuran logo menyesuaikan dengan judul-->
                    <span class="fw-bold fs-1">Login</span> <!-- ukuran judul -->
                </a>
            </div>
        </nav>
...
```

Lalu, saya membuat kostumisasi tabel produk dengan kode:

```
...
<div class="container">
        <table class="table"> <!-- Tambahkan style margin: 0 auto; untuk membuat tabel berada di tengah -->
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                    <th scope="col">Description</th>
                    <th scope="col">Date Added</th>
                    <th scope="col">Actions</th> <!-- Kolom untuk tombol Edit dan Delete -->
                </tr>
            </thead>
            <tbody>
                {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

                {% for product in products %}
                <tr>
                    <td>{{product.name}}</td>
                    <td>{{product.price}}</td>
                    <td>{{product.description}}</td>
                    <td>{{product.date_added}}</td>
                    <td> 
                        <div class="d-flex justify-content-between">
...
```

Setelah itu, pada setiap button yang ada saya buat kostumisasi sebagai berikut:
```
<form>
    <!-- Kustomisasi button Edit-->
    <a href="{% url 'main:edit_product' product.pk %}">
        <button type="button" class="btn btn-primary btn-sm">Edit</button>
    </a>
</form>
```

Terakhir untuk kostumisasi background, saya menggunakan warna pink `#ffe1f4`.

</details>
</details>

<details>
<summary>Tugas 6: JavaScript dan Asynchronous JavaScript</summary>

# Tugas 6🔥
Projek ini dibuat dengan tujuan memenuhi Tugas 6 Pemrograman Berbasis Platform. Berikut merupakan link hasil deployment, [georgina-elena-tugas](http://georgina-elena-tugas.pbp.cs.ui.ac.id.)

Saya akan menjelaskan beberapa poin-poin berikut:
- Perbedaan antara asynchronous programming dengan synchronous programming
- Penjelasan paradigma event-driven programming dalam penerapan JavaScript dan AJAX
- Penerapan asynchronous programming pada AJAX
- Membandingkan penerapan AJAX antara Fetch API dengan Library JQuery 
- Implementasi Data

## Asynchronous Programming vs Synchronous Programming👩🏻‍💻

| Asynchronous programming | Synchronous Programming |
| ------------------------ | ----------------------- |
| eksekusi program tanpa ketergantungan pada proses lain (operasi independen) | program dieksekusi secara berurutan sesuai dengan urutan dan prioritasnya |
| program dieksekusi secara bersamaan tanpa harus menunggu tugas sebelumnya selesai | program dieksekusi satu per satu, dan eksekusi program berikutnya hanya dimulai setelah program sebelumnya selesai |
| lebih responsif dan efisien karena dapat melanjutkan eksekusi ketika tugas I/O sedang berlangsung | menghambat kinerja aplikasi dan menyebabkan aplikasi terasa "tertunda" saat menunggu tugas I/O |


## Event-Driven Programming🚙

Event-Driven Programming mengacu pada pendekatan di mana pemrograman fokus merespons peristiwa atau kejadian tertentu yang berasal dari sumber eksternal seperti masukan pengguna atau perubahan sistem. Dalam konteks JavaScript dan AJAX berarti tugas-tugas dijalankan sebagai respons terhadap peristiwa seperti klik tombol, permintaan jaringan selesai, atau interaksi pengguna lainnya. Contoh penerapannya pada aplikasi ini adalah button delete, ketika button ini ditekan (event) maka akan dijalankan fungsi deleteProduct.

## Asynchronous Programming pada AJAX

Pada AJAX, asynchronous programming sangat penting karena permintaan jaringan seringkali memerlukan waktu untuk menyelesaikan operasi. AJAX dengan JavaScript menggunakan metode seperti fetch atau XMLHttpRequest untuk mengirim permintaan jaringan. Kode JavaScript tidak  "menghentikan" eksekusi saat permintaan jaringan sedang berlangsung. Jadi, setelah pemuatan halaman HTML awal, data dapat diperbarui secara dinamis tanpa harus me-reload seluruh halaman web. Ini membuat interaksi lebih responsif, karena data dapat diperbarui di latar belakang tanpa mengganggu pengguna. Dengan eksekusi secara asynchronous, AJAX menjaga kecepatan dan fleksibilitas dalam menanggapi pengguna serta mempertahankan lingkungan yang didorong oleh data.

## Fetch API vs Library JQuery

| Fecth API | Library JQuery |
| --------- | -------------- |
| terdapat dalam standar JavaScript modern, tidak memerlukan pustaka tambahan | abstraksi tinggi dan mudah digunakan, mengurangi kerumitan kode | Memerlukan unduhan dan penggunaan pustaka eksternal, yang dapat memperlambat waktu muat aplikasi |
| lebih ringan dalam hal ukuran, meningkatkan kinerja dan kecepatan aplikasi | tidak seefisien Fetch API dalam hal kinerja |
| menyediakan fleksibilitas yang besar dalam mengelola permintaan dan respons | menyediakan berbagai fitur tambahan, seperti animasi dan manipulasi DOM | 
| lebih rendah level abstraksi dibandingkan dengan jQuery, sehingga memerlukan penulisan kode yang lebih banyak | abstraksi tinggi dan mudah digunakan, mengurangi kerumitan kode |

Dari kelebihan serta kekurangan yang ada, menurut saya teknologi yang lebih baik untuk digunakan adalah Fetch API. Hal ini saya simpulkan dengan melihat kelebihan Fetch API dalam penggunaan di banyak proyek modern dimana lebih ringan, lebih kuat, dan sesuai dengan tren saat ini.

## Implementasi Data

<details>
<summary>AJAX GET</summary>

Membuat fungsi untuk menampilkan data produk yang difilter untuk user yang telah login dan menambahkan path url ke urls.py.

```
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))
```

Pada tugas sebelumnya saya memakai tabel bukan cards, maka dari itu saya memodifikasi tabel saya menjadi card dengan kode berikut:

```
<div class="row row-cols-1 row-cols-md-3 g-4" id="item_card"> 
        <div class="row"> <!-- Gunakan id untuk menempatkan tabel di sini -->
            {% for product in products %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title" style="font-weight: bold;">{{ product.name }}</h5>
                            <p class="card-text">Price      : {{ product.price }}</p>
                            <p class="card-text">Description: {{ product.description }}</p>
                            <p class="card-text">Date Added : {{ product.date_added }}</p>
                            <div class="d-flex justify-content-between">
                                <a href="{% url 'main:edit_product' product.pk %}" class="btn btn-primary btn-sm">Edit</a>
                                <a href="{% url 'main:delete_product' product.pk %}" class="btn btn-danger btn-sm">Delete</a>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
```

Kemudian, membuat fungsi untuk melakukan fetch data JSON di dalam tag `<script>` pada` main.html`. Data difetch secara _asynchronous_ :
```
async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
```

Membuat fungsi pada `<script>` yang akan memperbarui data-data secara asynchronous ketika terjadi suatu event tanpa me-reload halaman. Pada fungsi ini ada loop yang mengiterasi semua item milik user dan menampilkan atributnya dalam bentuk cards. Saya mengimplementasikan kode sebagai berikut:

```
async function refreshProducts() {
        document.getElementById("item_card").innerHTML = "";
        const products = await getProducts();

        products.forEach((product) => {
            const card = document.createElement("div");
            card.className = "col-md-4 mb-4";
            card.innerHTML = `
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${product.fields.name}</h5>
                        <p class="card-text">Price: ${product.fields.price}</p>
                        <p class="card-text">Description: ${product.fields.description}</p>
                        <p class="card-text">Date Added: ${product.fields.date_added}</p>
                        <div class="d-flex justify-content-between">
                            <a href="#" class="btn btn-primary btn-sm edit-button">Edit</a>
                            <a href="#" class="btn btn-danger btn-sm delete-button">Delete</a>
                        </div>
                    </div>
                </div>`;

            // Sisipkan kartu ke dalam elemen dengan ID "item_card"
            document.getElementById("item_card").appendChild(card);
        });

        // event listener untuk "Edit" button
        document.querySelectorAll(".edit-button").forEach((editButton, index) => {
            editButton.addEventListener("click", async () => {
                const productId = products[index].pk;  // Gantilah ini dengan cara Anda mendapatkan ID produk
                const editUrl = "{% url 'main:edit_product' 0 %}".replace(0, productId); // Ganti 'main:edit_product' dengan nama URL yang sesuai
                window.location.href = editUrl;
            });
        });

        // event listener untuk "Delete" button
        document.querySelectorAll(".delete-button").forEach((deleteButton, index) => {
            deleteButton.addEventListener("click", async () => {
                const productId = products[index].pk;  // Gantilah ini dengan cara Anda mendapatkan ID produk
                const deleteUrl = "{% url 'main:delete_product' 0 %}".replace(0, productId); // Ganti 'main:delete_product' dengan nama URL yang sesuai
                window.location.href = deleteUrl;
            });
        });

    }


```



</details>
<details>
<summary>AJAX POST</summary>

Dalam implementasi AJAX POST, saya membuat sebuah tombol yang akan membuka sebuah modal dengan form untuk menambahkan item.

**Button**
```
<button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#addItemModal">Add Item by AJAX</button>
```

**Modal**
```
<div class="modal fade" id="addItemModal" tabindex="-1" aria-labelledby="addItemModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header" style="background-color: #D4D4E7;">
                <h1 class="modal-title fs-5" id="addItemModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="background-color: #E4E4F0;">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer" style="background-color: #D4D4E7;">
                <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-light" id="button_add" data-bs-dismiss="modal">Add Item</button>
            </div>
        </div>
    </div>
</div>
```

Lalu, pada file `views.py` di direktori `main` saya membuat fungsi view baru untuk menambahkan item baru ke dalam database dengan kode berikut:
```
@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

Kemudian, pada file `urls.py` di direktori `main`, saya menambahkan path:
```
...
path('create-ajax/', create_ajax, name='create_ajax'),
```

Selanjutnya form dalam modal yang sudah dibuat, saya disambungkan ke path `/create-ajax/` dengan membuat fungsi pada blok `<script>`, kode sebagai berikut:
```
function addProduct() {
    fetch("{% url 'main:create_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}
```

Fungsi kode di atas adalah setelah item baru dibuat, halaman akan diperbaharui secara asynchronous dengan dipanggilnya fungsi refreshProduct.


</details>
<details>
<summary>Collectstatic</summary>

Setelag segala implementasi telah selesai, saya menjalankan perintah `python manage.py collectstatic` pada terminal dengan menggunakan environtment (env) untuk mengumpulkan file static pada aplikasi.

</details>


</details>
