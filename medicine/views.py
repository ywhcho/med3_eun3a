from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Medicine

def medicine_list(request):
    """의약품 목록 및 검색"""
    medicines = Medicine.objects.all()
    
    # 검색 필터
    search_type = request.GET.get('search_type', '')
    search_query = request.GET.get('search', '')
    
    if search_type and search_query:
        if search_type == '성분명':
            medicines = medicines.filter(성분명__icontains=search_query)
        elif search_type == '회사명':
            medicines = medicines.filter(회사명__icontains=search_query)
        elif search_type == '효능':
            medicines = medicines.filter(효능__icontains=search_query)
    
    # 페이지네이션 (10개씩)
    paginator = Paginator(medicines, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 검색용 드롭다운 데이터
    성분_list = Medicine.objects.values_list('성분명', flat=True).distinct().order_by('성분명')
    회사_list = Medicine.objects.values_list('회사명', flat=True).distinct().order_by('회사명')
    효능_list = Medicine.objects.values_list('효능', flat=True).distinct()[:20]  # 효능은 텍스트가 길어서 제한
    
    context = {
        'page_obj': page_obj,
        'search_type': search_type,
        'search_query': search_query,
        '성분_list': 성분_list,
        '회사_list': 회사_list,
        '효능_list': 효능_list,
    }
    return render(request, 'medicine/list.html', context)

def medicine_detail(request, pk):
    """의약품 상세 정보"""
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicine/detail.html', {'medicine': medicine})

