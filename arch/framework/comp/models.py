class User:
    def __init__(self, type_of_user, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.type = type_of_user


class Trainer(User):
    pass


class Student(User):
    courses = []


class UsersFactory:
    dict_of_users = {
        'trainer': Trainer,
        'student': Student
    }

    @classmethod
    def create_user(cls, type_of_user, name, surname, email):
        return cls.dict_of_users[type_of_user](name=name, surname=surname, email=email,
                                               type_of_user=type_of_user)


class Course:
    lvls_dict = {
        "newbie": "newbie",
        "master": "master",
    }

    def __init__(self, name, lvl):
        self.name = name
        self.lvl = self.lvls_dict[lvl]


class DivingCourse(Course):
    pass


class FightingCourse(Course):
    pass


class CoursesFactory:
    dict_of_courses = {
        'diving': DivingCourse,
        'fight': FightingCourse,
    }

    @classmethod
    def create_course(cls, type_of_course, type_of_lvl):
        return cls.dict_of_courses[type_of_course](type_of_course, type_of_lvl)


a = CoursesFactory.create_course('diving', 'master')
b = CoursesFactory.create_course('fight', 'newbie')


class SiteBrain:
    def __init__(self):
        self.trainers = []
        self.students = []
        self.courses = []

    def create_user(self, user_type, name, surname, email):
        cur_user = UsersFactory.create_user(name=name, surname=surname, email=email,
                                            type_of_user=user_type)
        if user_type == "student":
            self.students.append(cur_user)
            print("++++++++")
        else:
            self.trainers.append(cur_user)
        return cur_user

    def create_course(self, course_type, course_lvl):
        return CoursesFactory.create_course(course_type, course_lvl)

    def get_course(self, name, lvl):
        for course in self.courses:
            if name == course.name and lvl == course.lvl:
                return course
            else:
                return None

    def iterator(self):
        return SiteBrainIterator(self.courses)


class SiteBrainIterator:
    def __init__(self, items):
        self.indx = 0
        self.items = items

    def has_next(self):
        return False if self.indx >= len(self.items) else True

    def next(self):
        item = self.items[self.indx]
        self.indx += 1
        return item
