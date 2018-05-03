from django.contrib import admin

# Register your models here.
# Use Django admin to edit and delete the posts we've just modeled

from django.contrib import admin
from .models import Post

admin.site.register(Post) # to make Post object/model visible on the admin page