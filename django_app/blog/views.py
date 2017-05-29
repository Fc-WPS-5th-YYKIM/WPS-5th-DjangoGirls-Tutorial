from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # context 딕셔너리의 키와 view(html)의 {{}} 변수와 매칭하여 데이터를 파싱 한다.
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title': 'PostList from post_list view',
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context=context)
