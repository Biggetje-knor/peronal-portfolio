from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blog(request):
    blog = Blog.objects.all()
    #blog = Blog.objects.order_by('-datum')[:3]
    return render(request,'blog/all_blog.html',{"blog":blog})
    #return render(request, 'blog/all_blog.html')



def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})

# Create your views here.
