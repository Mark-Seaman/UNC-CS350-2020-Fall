import csv
from _csv import reader
from glob import glob
from os.path import exists

from course.lecture import create_lecture
from course.models import Course, Lesson, Project, ZoomLecture
from course.outline import outline_as_markdown, outline_tree
from course.project import create_project, get_project
from tool.document import doc_path
from tool.files import join_files, list_files, read_file, read_json, write_file
from tool.text import text_join, text_lines


def create_lesson(**kwargs):
    course = Course.objects.get(name=kwargs.get('course'))
    lesson = kwargs.get('lesson')
    lecture = kwargs.get('lecture')

    p = Lesson.objects.get_or_create(course=course, lesson=lesson)[0]
    p.date = kwargs.get('date')
    p.topic = kwargs.get('topic')
    p.project = kwargs.get('project')
    p.save()

    create_lecture(course, lesson, lecture)
    return p


def export_lessons():

    def set_default_lecture(course, lesson):
        join_links = dict(
            bacs200='https://unco.zoom.us/j/96131314570',
            bacs350='https://unco.zoom.us/j/95419819180',
            cs350='https://unco.zoom.us/j/96630908573',
        )
        lectures = ZoomLecture.objects.filter(lesson=lesson)
        if not lectures:
            create_lecture(course, lesson.lesson, join_links[course])
        if len(lectures) > 1:
            lectures[0].delete()

    lesson_csv = ''
    courses = 'bacs200', 'bacs350', 'cs350'
    for course in courses:
        records = []

        for lesson in Lesson.objects.filter(course__name=course).order_by('lesson'):
            set_default_lecture(course, lesson)
            lecture = ZoomLecture.objects.get(lesson=lesson)
            # print(f'{course}, {lesson.lesson}, {lesson.date}, {lesson.project}, {lesson.topic}, {lecture.zoom_url}')
            records.append((course, lesson.lesson, lesson.date, lesson.project, lesson.topic, lecture.zoom_url))

        with open(f'Documents/course/{course}/lessons.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(records)

        lesson_csv += read_file(f'Documents/course/{course}/lessons.csv') + '\n'
    return lesson_csv


def import_lessons():
    courses = 'bacs200', 'bacs350', 'cs350'
    for course in courses:
        with open(f'Documents/course/{course}/lessons.csv') as f:
            for row in reader(f):
                kwargs = dict(course=row[0], lesson=row[1], date=row[2], project=row[3],  topic=row[4], lecture=row[5])
                create_lesson(**kwargs)


def get_chapters(course):
    course = get_course(course)
    chapters = []
    for project in range(course.num_projects):
        lessons = [lesson for lesson in Lesson.objects.filter(course=course, project=project)]
        p = get_project(course.name, project + 1)
        project_url = f'/course/{course.name}/project/{p.project:02}'
        chapters.append(dict(project=p, project_url=project_url, lessons=lessons))
    return chapters


def get_course(course):
    course = Course.objects.get(name=course)
    return course


def get_lesson(course, lesson_num):
    return Lesson.objects.get(course__name=course, lesson=lesson_num)


def lesson_markdown(outline):
    return outline_as_markdown(outline_tree(text_lines(outline))[0])


def lesson_outlines(course):
    path = f'Documents/course/{course}/lesson/outline'
    files = [f'{path}/{f}' for f in list_files(path)]
    print(join_files(files))


def lesson_matrix(course):
    table = lesson_table(course)

    path = f'Documents/course/{course}/course.json'
    data = read_json(path)
    headings = data['lessons']['headings']
    return dict(table=table, headings=headings)


def lesson_table(course):
    course = get_course(course)
    table = []
    for project in range(course.num_projects):
        p = get_project(course.name, project + 1)
        p.type = 'unc-dark'
        p.save()
        weekly = [p]
        # weekly = []
        for lesson in Lesson.objects.filter(course=course, project=project):
            weekly.append(lesson)
        table.append(weekly)
    return table


def lesson_table2(course):
    path = f'Documents/course/{course}/course.json'
    data = read_json(path)
    table = data['lessons']['table']
    return table


def lessons_grouped_by_project(course, weeks=14):
    lessons = Lesson.objects.filter(course__name=course).order_by('lesson')
    projects = Project.objects.filter(course__name=course).order_by('project')
    return [lessons.filter(project=p+1) for p in range(14)]


def lessons_text(course):
    path = doc_path(f'course/{course}/lesson/??.md')
    return text_join([f'{len(read_file(f)):5}  {f}' for f in sorted(glob(path))])


def list_lessons(course):
    lessons = Lesson.objects.filter(course__name=course)
    return [str(x) for x in lessons]


def print_lessons_groups(lessons):
    text = f'Lessons by Week'
    for p in lessons:
        text += f'\nWeek {p[0].project + 1}\n'
        for x in p:
            text += f'    {x.date} - Lesson {x.lesson} - {x.topic}\n'
    return text


def write_lesson(path, outline):
    if not exists(path):
        text = lesson_markdown(outline).replace('\n#### ', '* ')
        print(f'Writing Lesson: {path}')
        write_file(path, text)


def course_update():

    def bacs200_update():
        course = Course.objects.get(name='bacs200')
        create_project(course=course, project='1', date='2020-08-28', title='Web Hosting')
        create_project(course=course, project='2', date='2020-09-04', title='Inspire')
        create_project(course=course, project='3', date='2020-09-11', title='Amuse')
        create_project(course=course, project='4', date='2020-09-18', title='Educate')
        create_project(course=course, project='5', date='2020-09-25', title='Superhero')
        create_project(course=course, project='6', date='2020-10-02', title='Testing')
        create_project(course=course, project='7', date='2020-10-09', title='Wanted Poster')
        create_project(course=course, project='8', date='2020-10-16', title='Business Blog')
        create_project(course=course, project='9', date='2020-10-23', title='Non-profit Blog')
        create_project(course=course, project='10', date='2020-10-30', title='Video Log')
        create_project(course=course, project='11', date='2020-11-06', title='Travel Brochure')
        create_project(course=course, project='12', date='2020-11-13', title='W3Schools Skills')
        create_project(course=course, project='13', date='2020-11-20', title='URL Game')
        create_project(course=course, project='14', date='2020-12-04', title='Professional Portfolio')
        # get_lesson(course, 42).delete()


    def bacs350_update():
        course = Course.objects.get(name='bacs350')
        create_project(course=course, project='1', date='2020-08-28', title='First Django App')
        create_project(course=course, project='2', date='2020-09-04', title='Superhero Views')
        create_project(course=course, project='3', date='2020-09-11', title='Web App Hosting')
        create_project(course=course, project='4', date='2020-09-18', title='Superhero Profiles')
        create_project(course=course, project='5', date='2020-09-25', title='Superhero Database')
        create_project(course=course, project='6', date='2020-10-09', title='Superhero Template View')
        create_project(course=course, project='7', date='2020-10-16', title='Superhero Data Views')
        create_project(course=course, project='8', date='2020-10-23', title='User Accounts')
        create_project(course=course, project='9', date='2020-10-30', title='View Inheritance')
        create_project(course=course, project='10', date='2020-11-06', title='Cards & Tables & Docs')
        create_project(course=course, project='11', date='2020-11-13', title='Tabs & Accordion')
        create_project(course=course, project='12', date='2020-12-04', title='Superhero News')
        get_project(course, 13).delete()
        get_project(course, 14).delete()
        get_lesson(course, 42).delete()

    def cs350_update():
        course = Course.objects.get(name='cs350')
        create_project(course=course, project='1', date='2020-09-04', title='Project Plan')
        create_project(course=course, project='2', date='2020-09-18', title='Technology')
        create_project(course=course, project='3', date='2020-10-02', title='Core Features')
        create_project(course=course, project='4', date='2020-10-16', title='Functionality Complete')
        create_project(course=course, project='5', date='2020-10-30', title='Test Complete')
        create_project(course=course, project='6', date='2020-11-13', title='Code Release')
        create_project(course=course, project='7', date='2020-12-04', title='Code Maintenance')
        # get_lesson(course, 42).delete()

    cs350_update()
    bacs350_update()
    bacs200_update()

