from django.contrib import admin
from .models import UserProfile, Challenge, TestCase, Solution, Comment, Tag

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Challenge)
admin.site.register(TestCase)
admin.site.register(Solution)
admin.site.register(Comment)
admin.site.register(Tag)