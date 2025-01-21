from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    process = models.TextField()
    picture = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.name