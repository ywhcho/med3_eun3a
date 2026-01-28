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
    
    # 검색 타입 검증
    valid_search_types = ['성분명', '회사명', '효능']
    
    if search_type in valid_search_types and search_query:
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
    
    context = {
        'page_obj': page_obj,
        'search_type': search_type,
        'search_query': search_query,
    }
    return render(request, 'medicine/list.html', context)

def medicine_detail(request, pk):
    """의약품 상세 정보"""
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicine/detail.html', {'medicine': medicine})

