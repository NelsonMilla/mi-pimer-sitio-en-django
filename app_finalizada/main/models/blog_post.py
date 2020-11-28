from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=32)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class BlogPost(models.Model):
    title = models.CharField(verbose_name='titulo', max_length=32)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/images')
    content= models.TextField()

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
