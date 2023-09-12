from django.shortcuts import render

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
