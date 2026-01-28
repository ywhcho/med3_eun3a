from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import models
from .models import Post

def post_list(request):
    """게시글 목록"""
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'board/list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    """게시글 상세"""
    post = get_object_or_404(Post, pk=pk)
    # 조회수 증가 (race condition 방지를 위해 update 사용)
    Post.objects.filter(pk=pk).update(views=models.F('views') + 1)
    post.refresh_from_db()
    return render(request, 'board/detail.html', {'post': post})

@login_required
def post_create(request):
    """게시글 작성"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            messages.success(request, '게시글이 작성되었습니다.')
            return redirect('board:list')
        else:
            messages.error(request, '제목과 내용을 모두 입력해주세요.')
    
    return render(request, 'board/form.html', {'form_type': 'create'})

@login_required
def post_update(request, pk):
    """게시글 수정"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 수정 가능
    if post.author != request.user:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            post.title = title
            post.content = content
            post.save()
            messages.success(request, '게시글이 수정되었습니다.')
            return redirect('board:detail', pk=pk)
        else:
            messages.error(request, '제목과 내용을 모두 입력해주세요.')
    
    return render(request, 'board/form.html', {'form_type': 'update', 'post': post})

@login_required
def post_delete(request, pk):
    """게시글 삭제"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자만 삭제 가능
    if post.author != request.user:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('board:list')
    
    return render(request, 'board/delete.html', {'post': post})

