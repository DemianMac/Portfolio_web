from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/imagenes', blank=True)
    tecnologias = models.CharField(max_length=250, blank=True)
    url_github = models.URLField(blank=True)
    url_vivo = models.URLField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def get_tecnologias_list(self):
        if self.tecnologias:
            return [t.strip() for t in self.tecnologias.split(',') if t.strip()]
        return []
