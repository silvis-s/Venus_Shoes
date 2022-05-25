from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="project")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    #price = models.FloatField(verbose_name= "precio")
    available = models.BooleanField(verbose_name="disponible", default=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

#-------------------------------------------

class CategoryProd(models.Model):
    name = models.CharField(max_length=100, verbose_name= "nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualización")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name= "titulo")
    categories = models.ForeignKey(CategoryProd,on_delete=models.CASCADE, verbose_name="categorias")
    image = models.ImageField(verbose_name="imagen", upload_to="tienda", blank=True)
    price = models.FloatField(verbose_name= "precio")
    available = models.BooleanField(verbose_name="disponible", default=True)
    content = models.TextField(verbose_name= "contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualización")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-created']

    def __str__(self):
        return self.title