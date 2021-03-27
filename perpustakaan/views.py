from django.shortcuts import render

# Create your views here.
def buku(request):
    judul = ["Belajar Django", "Belajar Bootstrap", "Belajar HTML"]
    penulis = "Dindin"

    value = {
        'title' : judul,
        'penulis' : penulis

    }
    return render(request, 'buku.html', value)

def penerbit(request):
    return render(request, 'penerbit.html')