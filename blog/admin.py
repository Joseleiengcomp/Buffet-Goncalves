from django.contrib import admin
# superuser: jose.cptm@gmail.com
# senha: negoerica1
# Register your models here.
from django.contrib import admin
from .models import Post


admin.site.register(Post)
