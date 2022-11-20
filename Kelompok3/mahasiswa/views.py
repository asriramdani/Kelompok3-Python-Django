from django.shortcuts import render

# Create your views here.
from . forms import Mahasiswa

from . models import Guest
def index(request):
    buku_mahasiswa = Mahasiswa()

    context = {
        'BukuMahasiswa' :buku_mahasiswa,

    }

    if request.method=="POST":
        Guest.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
        )
        
    return render(request, 'mahasiswa/index.html', context)
