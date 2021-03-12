from django.contrib import admin
from .models import BlogPost,TechPost


admin.site.register(BlogPost)
admin.site.register(TechPost)