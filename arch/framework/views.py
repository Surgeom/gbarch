# PageControllers
from core.jinja import render


def index_page(request):
    print(request)
    return '200 OK', render("index.html", name='World')


def about_page(request):
    print(request)
    return '200 OK', render("about.html", key=request['key'])


def contacts_page(request):
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        msg = data['msg']
        email = data['email']
        print(f'{title}-{msg},email-{email}')
        return '200 OK', render("contacts.html")
    else:
        return '200 OK', render("contacts.html")
