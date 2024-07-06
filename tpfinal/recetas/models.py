from django.db import models

# Create your models here.

class Receta(models.Model):
    name = models.CharField(default="", max_length=200)
    description = models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus, culpa mollitia nobis obcaecati sit ex. Molestiae eaque dolores, sapiente dolorem rem placeat quae quas praesentium consequatur explicabo cum...")
    image = models.ImageField(null=True, blank=True, upload_to="recetas")
    created = models.DateTimeField(auto_now_add=True)
    # link = models.URLField(null=True,blank=True)
    # eso es para cuando funcione, y se pueda añadir un link a la receta, o se genere solo..
    
    def __str__(self):
        return self.name    
