from django.http import HttpResponse
from django.template import loader
from .models import Post


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
        'myblog': myblog
    }
    return HttpResponse(template.render(context, request))
