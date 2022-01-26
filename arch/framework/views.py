# PageControllers
from core.jinja import render


def index_page(request):
    print(request)
    return '200 OK', render("index.html", name='World')


def about_page(request):
    print(request)
    return '200 OK', render("about.html", key=request['key'])
