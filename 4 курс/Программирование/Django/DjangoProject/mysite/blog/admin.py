from django.contrib import admin
from .models import Post, Poll, Choice

admin.site.register(model_or_iterable=Post)
admin.site.register(Poll)
admin.site.register(Choice)
