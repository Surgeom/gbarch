# PageControllers
from core.jinja import render
from comp.models import SiteBrain
from core.decorators import debug

site = SiteBrain()


@debug
def index_page(request):
    # print(request)
    return '200 OK', render("index.html", arr_of_courses=site.courses)


def about_page(request):
    # print(request)
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


def create_course(request):
    if request['method'] == 'POST':
        data = request['data']
        course_name = data['course_name']
        lvl = data["course_lvl"]
        try:
            site.courses.append(site.create_course(course_type=course_name, course_lvl=lvl))
            return '200 OK', render("index.html", arr_of_courses=site.courses)
        except KeyError:
            return '200 OK', render("crCourse.html")
    return '200 OK', render("crCourse.html")
