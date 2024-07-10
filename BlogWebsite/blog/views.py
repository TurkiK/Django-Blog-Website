from django.http import HttpResponse
from django.template import loader
from .models import Post
from .models import Comment
from .models import Category
from .models import User


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def blogs(request):
    myblogs = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'myblogs': myblogs
    }
    return HttpResponse(template.render(context, request))


def blogdetails(request, id):
    myblog = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'myblog': myblog,
    }
    return HttpResponse(template.render(context, request))


def comments(request, id):
    myblog = Post.objects.get(id=id)
    blogcomments = Comment.objects.filter(post=myblog)
    template = loader.get_template('comments.html')
    context = {
        'myblog': myblog,
        'blogcomments': blogcomments,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    mycategories = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycategories': mycategories
    }
    return HttpResponse(template.render(context, request))


def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers': myusers
    }
    return HttpResponse(template.render(context, request))
