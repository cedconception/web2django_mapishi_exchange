from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


#cette fonction permet de valider une image 
def validate_image(image):
    file_size = image.file.size
    limit_kb = 500  # Limit the file size to 500KB
    if file_size > limit_kb * 1024:
        raise ValidationError(_("Image file too large ( > 500KB )"))
    
    valid_image_formats = ["image/jpeg", "image/png", "image/gif"]
    if image.file.content_type not in valid_image_formats:
        raise ValidationError(_("Unsupported file format. Please upload a JPEG, PNG, or GIF image."))