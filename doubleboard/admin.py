from django.contrib import admin
from .models import QuestionDouble

# Register your models here.
class QuestionDoubleAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(QuestionDouble, QuestionDoubleAdmin)