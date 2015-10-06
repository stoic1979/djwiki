from django.contrib import admin

# Register your models here.

from wiki.models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Edit)
