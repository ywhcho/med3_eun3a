from django.db import models

class Medicine(models.Model):
    """의약품 모델"""
    약품명 = models.CharField(max_length=200, verbose_name='약품명')
    성분명 = models.CharField(max_length=200, verbose_name='성분명')
    효능 = models.TextField(verbose_name='효능')
    용량 = models.CharField(max_length=100, verbose_name='용량')
    주의사항 = models.TextField(verbose_name='주의사항')
    회사명 = models.CharField(max_length=200, verbose_name='회사명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    
    class Meta:
        verbose_name = '의약품'
        verbose_name_plural = '의약품 목록'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.약품명

