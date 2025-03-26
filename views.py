from django.shortcuts import render
from dasboart.forms import FormBarang
from dasboart.models import Barang
from django.contrib import messages
from django.shortcuts import render, redirect
def kalu(request):
    titelnya="singa eropa"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'kalu.html',konteks)

def atribut(request):
    titelnya="raja eropa"
    konteks = {
        'titel':titelnya
    }
    return render(request,'atribut.html',konteks)

def barca(request):
    return render(request,'barca.html')

def juve(request):
    return render(request,'juventus.html')

def nassr(requst):
    return render(requst,'nassr.html')

def tambah_barang(request):
    if request.POST:
        form=FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"pemain berhasil ditambahkan")
            konteks={
                'form':form
            }
            return render(request, 'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form
        }
    return render(request,'tambah_barang.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barang':barangs,
        }
    return render(request,'ubah_brg.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('vbrg')
    




# Create your views here.

