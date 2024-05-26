from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def validate_image(image):
    file_size = image.file.size
    limit_kb = 500  # Limit the file size to 500KB
    if file_size > limit_kb * 1024:
        raise ValidationError(_("Image file too large ( > 500KB )"))
    
    valid_image_formats = ["image/jpeg", "image/png", "image/gif"]
    if image.file.content_type not in valid_image_formats:
        raise ValidationError(_("Unsupported file format. Please upload a JPEG, PNG, or GIF image."))

class Recipe(models.Model):
    class Meta:
        permissions = [ 
            ("approve_recipe", "Can approve a Recipe"),
        ]
    class RecipeCategory(models.TextChoices):
        FOOD = "Food"
        CULTURE = "Culture"
        AFRICA = "Africa"

    category = models.CharField(max_length=10, choices=RecipeCategory.choices)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipes/img/', blank=True, validators=[validate_image])  # Optional image
    pub_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/recipes/" + str(self.id) + "/"