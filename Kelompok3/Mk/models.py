from django.db import models

# Create your models here.

class Kategori(models.Model):
    kategori = models.CharField(max_length=100)
    def __str__(self):
        return self.kategori




class Post(models.Model):
    nama_mk = models.CharField(max_length=255)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nama_mk