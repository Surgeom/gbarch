# PageControllers
from core.jinja import render
from comp.models import SiteBrain
from core.decorators import debug

site = SiteBrain()


def index_page(request):
    if request['method'] == 'GET':
        ar_of_courses = []
        iter = site.iterator()
        while iter.has_next():
            ar_of_courses.append(iter)
        return '200 OK', render("index.html", arr_of_courses=ar_of_courses)
    elif request['method'] == 'POST':
        print(request['data'])


@debug
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


def register(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        surname = data['surname']
        email = data['email']
        site.create_user(name=name, surname=surname, email=email, user_type='student')

        return '200 OK', render("index.html")
    else:
        return '200 OK', render("register.html")


def reg_course(request):
    if request['method'] == 'POST':
        data = request['data']
        course_ind = int(data['course_name']) - 1
        cur_student_ind = int(data['cur_student']) - 1

        if site.students[cur_student_ind]:
            site.students[cur_student_ind].courses.append(site.courses[course_ind])
            print(site.students[cur_student_ind].courses)
        return '200 OK', render("index.html", arr_of_courses=site.courses)
    else:
        return '200 OK', render("gtcourse.html", arr_of_courses=site.courses, arr_of_students=site.students)
