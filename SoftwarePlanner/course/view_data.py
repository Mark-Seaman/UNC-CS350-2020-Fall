from course.project import get_project
from course.teamwork import get_teamwork_data
from course.lesson import lessons_grouped_by_project
from course.models import Lesson, Project, UncStudent, ZoomLecture
from course.students import get_student, get_teacher, students, user_list
from tool.files import read_file
from views.mybook import page_settings, read_settings
from views.view_data import doc_view_data, get_doc_data


def course_agenda(course):
    path = f'Documents/course/{course}/agenda'
    return f'Course agenda - {course}\n\n' + read_file(path)


def course_doc_data(course, doctype, doc):
    page = f'course/{course}/{doctype}/{doc}'
    data = doc_view_data(page)
    data['lessons'] = lessons_grouped_by_project(course)
    return data


def course_page(course, doctype, doc):
    if not doc:
        if not doctype:
            if not course:
                return 'course/Index'
            return f'course/{course}/Index'
        return f'course/{course}/{doctype}/Index'
    return f'course/{course}/{doctype}/{doc}'


def course_view_data(user, course, doctype, doc):
    page = course_page(course, doctype, doc)
    teacher = teacher_data(user)
    student = student_data(user, course)
    # projects = project_data(course)
    document = doc_data(course, f'course/{course}/docs/CourseWebsite')
    # users = user_list()
    enrolled = students(course)
    css = '/static/css/unc.css'

    # weekly = weekly_lessons(course)
    #
    # # if doctype == 'reviews':
    # #     reviews = render_reviews(student)
    # #     return page_settings(page=page, course=course, reviews=reviews)
    # #
    # # if doctype == 'review':
    # #     review = render_review(doc)
    # #     return page_settings(page=page, course=course, review=review)
    #
    # if doctype == 'lesson':
    #     if doc == 'Index':
    #         return page_settings(page=page, course=course, weekly=weekly, server=True)
    #     else:
    #         return page_settings(page=page, course=course, doc=document)
    #
    # if doctype == 'project':
    #     if doc == 'Index':
    #         return page_settings(page=page, course=course, student=student, projects=projects, server=True)
    #     else:
    #         return page_settings(page=page, course=course, student=student, doc=document)
    #
    # if doctype == 'docs':
    #     return page_settings(page=page, course=course, doc=document)
    #
    # if doctype == 'test':
    #     test = test_data(doc, course, '01')
    #     return page_settings(page=page, course=course, student=student, test=test)
    #
    if doctype == 'students':
        if teacher:
            return page_settings(page=page, course=course, teacher=teacher, students=enrolled, css=css, bacs200=(course=='bacs200'))
        elif student:
            return page_settings(page=page, course=course, student=student, students=enrolled, css=css, bacs200=(course=='bacs200'))
        else:
            return page_settings(page=page, course=course, css=css)
    #
    # if doctype == 'teacher':
    #     document = doc_data(course, f'private/plan/Teaching')
    #     return page_settings(page=page, course=course, teacher=teacher, doc=document,
    #                          student=student,  students=enrolled, users=users)
    #
    # if student:
    #     document = doc_data(course, f'course/{course}/docs/Welcome')
    #     teamworks = get_teamwork_data(student)
    #     bacs200 = (course == 'bacs200')
    #     cs350 = (course == 'cs350')
    #     return page_settings(page=page, course=course, student=student, doc=document, bacs200=bacs200, cs350=cs350, teamworks=teamworks)
    # else:
    #     document = doc_data(course, f'course/{course}/docs/Guest')
    #     return page_settings(page=page, course=course, doc=document)

    return page_settings(page=page, course=course, css=css, doc=document, student=student)


def index_data(course):
    weekly = weekly_lessons(course)
    url = 'index.html'
    page = f'course/{course}'
    return page_settings(page=page, course=course, weekly=weekly, url=url)


def doc_data(course, page):
    return get_doc_data(page, f'/static/images/course/{course}')


def project_data(course):
    settings = read_settings(f'course/{course}/')
    week = settings['week']
    label = settings['week_label']
    projects = [p for p in Project.objects.filter(course__name=course).order_by('project')[:week]]
    return dict(projects=projects, label=label)


def student_data(user, course):
    return get_student(course, user)


def teacher_data(user):
    if get_teacher(user):
        todo = get_doc_data('private/plan/Teaching')
        done = get_doc_data('private/plan/Teaching-Done')
        test = get_doc_data('course/Test')
        return [todo, done, test]


def test_data(student_id, course, project):
    # teacher = UncStudent.objects.get(course__name=course, email='mark.b.seaman@gmail.com')
    s = UncStudent.objects.get(pk=student_id)
    if s and s.github:
        return dict(course=course, project=project, settings={},
                    github_user=s.github_user,
                    github_url=s.github,
                    github_pages=s.github_pages,
                    github_server=s.github_server)
    else:
        bad = f'https://shrinking-world.com/static/images/sad.jpg'
        return dict(course=course, project=project, settings={},
                    github_user=bad,
                    github_url=bad,
                    github_pages=bad,
                    github_server=bad)


def weekly_lessons(course):

    def weekly_content(i, week, lessons, week_label, project):
        card = dict(id=i, title=f'{week_label} {i+1}',  lessons=lessons, project=project)
        if i == week-1:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    def get_lecture(course, id):
        lesson = Lesson.objects.get(course__name=course, lesson=id)
        x = ZoomLecture.objects.filter(lesson=lesson)
        if x:
            return x[0]

    def content(course, week, current):
        lessons = [dict(lesson=lesson, lecture=get_lecture(course, lesson.lesson)) for lesson in weekly_lessons]
        # project = get_project(course, week)
        project = None
        return weekly_content(week, current, lessons, label, project)

    settings = read_settings(f'course/{course}/')
    current_week = settings['week']
    label = settings['week_label']
    lessons = lessons_grouped_by_project(course)[:current_week]
    weekly = []
    for i, weekly_lessons in enumerate(lessons):
        # lessons = [dict(lesson=lesson, lecture=get_lecture(course, lesson.lesson)) for lesson in weekly_lessons]
        # project = get_project(course, i+1)
        # weekly.append(weekly_content(i, week, lessons, label, project))
        weekly.append(content(course, i, current_week))
    return weekly

