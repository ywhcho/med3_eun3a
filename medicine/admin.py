from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['약품명', '성분명', '회사명', 'created_at']
    list_filter = ['회사명', '성분명']
    search_fields = ['약품명', '성분명', '회사명', '효능']
    date_hierarchy = 'created_at'

