from random import choice
from random import randint
from random import shuffle

from django.core.management import BaseCommand

from applications.courses.models import Addition
from applications.courses.models import Course
from applications.courses.models import CourseCategory
from applications.courses.models import ProgramModule
from applications.module_parts import models
from applications.users.models import User


class Command(BaseCommand):
    help = "Creates given amount of course objects to db"

    def create_categories(self):
        CourseCategory.objects.all().delete()
        categories_num = 20
        categories_params = [
            {"title": f"category{num}", "description": f"This is test category №{num}"}
            for num in range(categories_num + 1)
        ]
        bulk_list = [CourseCategory(**p) for p in categories_params]
        CourseCategory.objects.bulk_create(bulk_list)
        return bulk_list

    def get_teachers(self, users, max_count=5):
        num_of_teachers = randint(1, max_count)
        teachers = list(users.filter(is_teacher=True))
        shuffle(teachers)
        return teachers[:num_of_teachers]

    def get_students(self, users, author, max_count=20):
        num_of_students = randint(1, max_count)
        students = list(users.exclude(id=author.id))
        shuffle(students)
        return students[:num_of_students]

    def create_additions(self, course):
        additions_params = [
            {
                "course": course,
                "title": f"{course} №{num} addition",
                "text": f"This is test addition {num} for {course}",
            }
            for num in range(1, 10)
        ]
        bulk_list = [Addition(**p) for p in additions_params]
        Addition.objects.bulk_create(bulk_list)

    def create_modules(self, course):
        module_params = [
            {
                "course": course,
                "title": f"{course} №{num} module",
                "description": f"This is module {num} for {course}",
            }
            for num in range(1, randint(5, 10))
        ]
        bulk_list = [ProgramModule(**p) for p in module_params]
        return ProgramModule.objects.bulk_create(bulk_list)

    def create_lessons(self, module):
        lessons_params = [
            {
                "module": module,
                "text": f"This is test lesson {num} for {module}",
                "video": "https://www.youtube.com/watch?v=lZTT1bQYGZ4",
            }
            for num in range(2, randint(5, 10))
        ]
        bulk_list = [models.Lesson(**p) for p in lessons_params]
        models.Lesson.objects.bulk_create(bulk_list)

    def create_tasks(self, module):
        task_params = [
            {
                "module": module,
                "text": f"This is test task {num} for {module}",
                "video": "https://www.youtube.com/watch?v=lZTT1bQYGZ4",
            }
            for num in range(2, randint(5, 10))
        ]
        bulk_list = [models.Task(**p) for p in task_params]
        models.Task.objects.bulk_create(bulk_list)

    def create_tests(self, module):
        test_params = [
            {
                "module": module,
                "text": f"This is test {num} for {module}",
                "video": "https://www.youtube.com/watch?v=lZTT1bQYGZ4",
            }
            for num in range(2, randint(5, 10))
        ]
        bulk_list = [models.Test(**p) for p in test_params]
        return models.Test.objects.bulk_create(bulk_list)

    def create_questions(self, test):
        questions_params = [
            {
                "test": test,
                "question_body": f"This is test question {num} for {test}",
            }
            for num in range(1, randint(3, 10))
        ]
        bulk_list = [models.TestQuestion(**p) for p in questions_params]
        models.TestQuestion.objects.bulk_create(bulk_list)
        for question in bulk_list:
            self.create_answers(question)

    def create_answers(sefl, question):
        answers_params = [
            {
                "question": question,
                "text": f"this is answer {num} for {question}",
                "is_right": choice((True, False)),
            }
            for num in range(1, randint(3, 5))
        ]
        bulk_list = [models.TestAnswer(**p) for p in answers_params]
        models.TestAnswer.objects.bulk_create(bulk_list)

    def add_arguments(self, parser):
        parser.add_argument("number_of_courses", type=int)
        parser.add_argument("number_of_teachers", type=int)
        parser.add_argument("number_of_students", type=int)

    def handle(self, *args, **options):
        courses_num = options.get("number_of_courses")
        teachers_num = options.get("number_of_teachers")
        # students_num = options.get("number_of_students")

        self.stdout.write("Creating categories")
        categories = list(self.create_categories())
        self.stdout.write("Succesfully created 20 categories")

        self.stdout.write(f"Creating {courses_num} courses")
        users = User.objects.all()
        Course.objects.all().delete()

        courses = []
        for num in range(1, courses_num + 1):
            author = users[randint(1, len(users) - 1)]
            title = f"course{num}"
            course = Course(
                title=title,
                author=author,
                category=choice(categories),
                price=randint(1000, 100000),
            )
            courses.append(course)

        Course.objects.bulk_create(courses)
        self.stdout.write(f"created {courses_num} courses succesfully")

        self.stdout.write("setting students and teachers to courses")
        for course in courses:
            # print(course, 'OK')
            author = course.author
            teachers = self.get_teachers(users, teachers_num)
            students = self.get_students(users, author, courses_num)
            course.students.set(students)
            course.teachers.set(teachers)
        self.stdout.write("setting students and teachers to courses complited")

        self.stdout.write("creating additions for courses")
        for course in courses:
            # print(course, 'OK')
            self.create_additions(course)
        self.stdout.write("creating additions for courses complited")

        self.stdout.write("creating modules for courses")
        modules = []
        for course in courses:
            data = self.create_modules(course)
            modules += data
        self.stdout.write("creating modules for courses complited")

        self.stdout.write("creating module parts")
        for module in modules:
            self.create_lessons(module)
            self.create_tasks(module)
            tests = self.create_tests(module)
            for test in tests:
                self.create_questions(test)
        self.stdout.write("creating module parts complited")
        self.stdout.write("\nall data created succesfully")
