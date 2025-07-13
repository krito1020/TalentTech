from django.db import models

class Comercio(models.Model):
    nombre = models.CharField(max_length=200)
    sector = models.CharField(max_length=100)
    subsector = models.CharField(max_length=100)
    articulos = models.TextField()
    direccion = models.CharField(max_length=300)
    celular = models.CharField(max_length=20, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    link_maps = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_instagram = models.URLField(blank=True)

    def __str__(self):
        return self.nombre