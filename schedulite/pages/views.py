from django.http import Http404
from django.shortcuts import render
def index(http_request):
    template_name = 'blog/index.html'
    context = {
        'posts': reversed(posts)
    }
    return render(http_request, template_name, context)


def post_detail(http_request, id):
    template_name = 'blog/detail.html'

    if id not in POST_BY_ID:
        raise Http404('Page does not exist')

    context = {
        'post': POST_BY_ID[id]
    }

    return render(http_request, template_name, context)


def category_posts(http_request, category_slug):
    template_name = 'blog/category.html'
    context = {
        'category': category_slug
    }
    return render(http_request, template_name, context)
