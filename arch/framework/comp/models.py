class User:
    pass


class Trainer(User):
    pass


class Student(User):
    pass


class UsersFactory:
    dict_of_users = {
        'trainer': Trainer,
        'student': Student
    }

    @classmethod
    def create_user(cls, type_of_user):
        return cls.dict_of_users[type_of_user]()


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

    def create_user(self, user_type):
        return UsersFactory.create_user(type_of_user=user_type)

    def create_course(self, course_type, course_lvl):
        return CoursesFactory.create_course(course_type, course_lvl)

    def get_course(self, name, lvl):
        for course in self.courses:
            if name == course.name and lvl == course.lvl:
                return course
            else:
                return None


