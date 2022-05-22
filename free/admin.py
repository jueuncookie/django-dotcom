from django.contrib import admin
from .models import QuestionFree

# Register your models here.
class QuestionFreeAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(QuestionFree, QuestionFreeAdmin)