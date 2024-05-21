from django.db import models

class Recipe(models.Model):
    class Meta:
        permissions = [
            ("publish_recipe", "Can publish a Recipe"),
            ("edit_custom_recipe", "Can edit a Recipe"),  
            ("remove_recipe", "Can delete a Recipe"),  
            ("approve_recipe", "Can approve a Recipe"),
        ]

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