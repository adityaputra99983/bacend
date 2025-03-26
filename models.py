from django.db import models

# Create your models here.
class jenis(models.Model):
    nama=models.CharField(max_length=8)
    ket=models.TextField
    def __str__(self):
        return self.nama
    
class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(jenis,on_delete=models.CASCADE,null=True)

  #  def __str__(self):
   #   return "{}. {}" .format(self.kodebrg.self.nama)