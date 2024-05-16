from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipes/img/', blank=True)  # Optional image
    pub_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/recipes/" + str(self.id) + "/"