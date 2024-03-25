from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    cooking_time = models.TextField(max_length = 10, blank=True)
    image = models.ImageField(upload_to='../recipes/img/', blank=True)  # Optional image
    #average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/recipes/" + str(self.id) + "/"