from django.contrib import admin
from .models import CodeReview

@admin.register(CodeReview)
class CodeReviewAdmin(admin.ModelAdmin):
    list_display = ('language', 'created_at')
    search_fields = ('language', 'code', 'review')
    list_filter = ('language', 'created_at')
