from csv import reader
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from os import listdir
from os.path import exists

from course.models import Course, UncStudent
from tool.files import read_csv_file, write_csv_file
from tool.log import log_exception
from tool.text import text_join
from tool.user import add_user_login, find_user_login, list_users


def add_canvas_students(course):
    students = canvas_students(course)
    output = f"\nStudents in {course}:  {len(students)} students\n\n"
    for s in students:
        output += f'{s[0]:25} {s[1]}\n'
        x = UncStudent.objects.filter(name=s[0])
        if not x:
            output += f'    add {s[0]:25} {s[1]}\n'
            first, last = s[0].split(' ')
            add_student(course, first, last, s[0], s[1])
        elif x[0].email != s[1]:
            output += f'    email -\n    student:{x[0].email:25} \n    canvas:{s[1]} \n    user:{x[0].user.email}\n'
            x[0].email = s[1]
            x[0].save()
    return output


# add_student('Sensei', '200', 'mark.b.seaman+200@gmail.com', 'http://unco-bacs.org', 'bacs200')

def add_student(course, first, last, username, email, server=None, github=None):
    u = find_user_login(email)
    if not u:
        u = add_user_login(first, last, username, email)
    c = Course.objects.get(name=course)
    s = UncStudent.objects.get_or_create(name=f'{first} {last}', email=email, course=c, user=u)[0]
    s.server = server if server else 'https://github.com'
    s.github = github if github else 'https://github.com/UNC-STUDENT'
    s.save()
    return s


def add_teacher(course):
    add_student(course, 'Mark', 'Seaman', 'MarkSeaman', 'mark.b.seaman@gmail.com', 'https://Mark-Seaman.github.io',
                'https://github.com/Mark-Seaman')


def canvas_update_list(course):
    path = f'/Users/seaman/Github/UNC-2020-Fall/{course}'
    if exists(path):
        f = sorted(listdir(path))[-2]
        # print(f)
        table = [(row[0], row[3]) for row in read_csv_file(f'{path}/{f}')[2:]]
        table = [row for row in table if row[0] != 'Test UncStudent' and 'Points Possible' not in row[0]]
        course_path = f'Documents/course/{course}/students.csv'
        write_csv_file(course_path, table)
        return table
    else:
        return []


def canvas_students(course):
    student_file = f'Documents/course/{course}/students.csv'
    with open(student_file) as f:
        return [(r[0], r[1]) for r in reader(f)]


def check_student_enrollment():
    for course in ['bacs200', 'bacs350', 'cs350']:
        add_teacher(course)
        # print(canvas_students(course))
        print(add_canvas_students(course))
        print(drop_students(course))
    print(show_users())


def drop_students(course):
    canvas = canvas_students(course)
    canvas_names = [e[0] for e in canvas]
    canvas_emails = [e[1] for e in canvas]
    text = f'\nSTUDENTS in {course}\n\n'
    for s in UncStudent.objects.filter(course__name=course):
        name = f'{s.user.first_name} {s.user.last_name}'
        if not s.name in canvas_names:
            try:
                if s.email != 'mark.b.seaman@gmail.com':
                    if not s.email in canvas_emails:
                        text += f'drop    {s.name:30} student: {s.pk} email: {s.email}\n'
                    else:
                        text += f'missing {s.name:30} student: {s.pk} email: {s.email} user: {name}\n'
                    UncStudent.objects.get(pk=s.pk).delete()
            except:
                pass
    return text


def drop_student(email):
    s = UncStudent.objects.get(email=email)
    if s:
        # s.user.delete()
        s.delete()


def delete_user(email):
    u = User.objects.filter(email=email)
    if u:
        u[0].delete()


def find_students(course):
    import_students(course)


def fix_students():

    # Fix the link
    for s in UncStudent.objects.all():
        if s.github == 'https://github.com/UNC-STUDENT':
            s.github = None
            s.server = None
            s.save()

    # Deactivate all users with no class
    for u in user_list():
        if not u['classes']:
            u = User.objects.get(email=u['email'])
            u.is_active = False
            u.save()

    # Mark Seaman record
    u = User.objects.get(email='mark.b.seaman@gmail.com')
    u.first_name = 'Mark'
    u.last_name = 'Seaman'
    u.is_active = True
    u.save()

    # Delete
    delete_user('ethridgee16@gmail.com')


def get_student(course, user):
    try:
        if not user.is_anonymous:  #  and not user.username == 'MarkSeaman'
            return UncStudent.objects.get(course__name=course, user=user)
    except:
        log_exception(f'Cannot find student record, {user}')


def get_teacher(user):
    return not user.is_anonymous and user.username == 'MarkSeaman'


def import_students(course):
    output = ''
    student_file = f'Documents/course/{course}/students.csv'
    with open(student_file) as f:
        for row in reader(f):
            output += f'{row[0]:25} {row[1]}\n'
            u = find_user_login(row[1])
            if not u:
                print(f'add_user({course}, {row[0]}, {row[1]})')
            else:
                s = UncStudent.objects.filter(course__name=course, email=row[1])
                if not s:
                    print(f'Found User {row[0]} email: {u.email}')
                    first, last = row[0].split(' ')
                    print(f'add_student({course}, {first}, {last}, {row[0]}, {row[1]})')
                # else:
                #     print(f'Found UncStudent {row[0]} in {course}')
    return output


def sensei_students():
    text = "\nSensei UncStudents\n"
    for course in ['bacs200', 'bacs350', 'cs350']:
        text += f"\nStudents in {course}\n"
        for i, s in enumerate(students(course)):
            text += f'{course} {i+1} {s}\n'
    return text


def show_users():
    def courses(x):
        return ','.join([f'{i.course.name}' for i in x])

    def entry(u):
        return f'{u["pk"]}. {u["name"]:30} {u["email"]:30} {courses(u["classes"])}'

    users = [entry(u) for u in user_list()]
    return '\nUSERS\n\n' + text_join(users)


def students(course):
    return UncStudent.objects.filter(course__name=course, user__is_active=True).order_by(Lower('user__last_name'))


def user_list():

    def user_info(user):
        name = user.first_name + ' ' + user.last_name
        classes = UncStudent.objects.filter(email=user.email)
        return dict(pk=user.pk, name=name, email=user.email, classes=classes)

    return [user_info(u) for u in User.objects.all().order_by('last_name') if u.is_active]

