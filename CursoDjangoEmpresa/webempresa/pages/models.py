from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido") # models.TextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Order", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["order", "title"]
    
    def __str__(self):
        return self.title