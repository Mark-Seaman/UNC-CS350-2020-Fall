from os import listdir
from os.path import exists

# from course.lesson import create_course_lessons, create_lesson, get_course
# from course.project import create_project, project_due
from course.models import Course, Lesson, Project
from course.outline import main_topics, read_outline_tree
from tool.days import list_unc_schedule
from tool.document import doc_path, doc_title
from tool.files import read_file, write_file
from tool.shell import banner
from tool.text import text_join, text_replace


def course_outline(course):
    path = f'Documents/course/{course}/outline'
    return read_outline_tree(path)


# def create_courses():
#     create_bacs200()
#     create_bacs350()
#     create_cs350()
#
#
# def create_cs350():
#     course = 'cs350'
#     c = Course.objects.get_or_create(name=course)[0]
#     c.description = 'This class teaches Software Checklist Skills.'
#     c.title = 'UNC CS 350 - Software Checklist (with Scrum/TDD)'
#     c.num_projects = 7
#     c.num_lessons = 42
#     c.save()
#     create_course_lessons(course, course_outline(course), schedule(course))
#     export_agenda(course)
#     import_agenda(course)
#
#
# def create_bacs350():
#     course = 'bacs350'
#     c = Course.objects.get_or_create(name=course)[0]
#     c.description = 'This class teaches web development using Python and the Django web framework.'
#     c.title = 'UNC BACS 350 - Web Apps (with Python/Postgres)'
#     c.num_projects = 14
#     c.num_lessons = 42
#     c.save()
#     create_course_lessons(course, course_outline(course), schedule(course))
#     export_agenda(course)
#     import_agenda(course)
#
#
# def create_bacs200():
#     course = 'bacs200'
#     c = Course.objects.get_or_create(name=course)[0]
#     c.description = 'This class teaches web development using HTML and CSS.'
#     c.title = 'UNC BACS 200 - Web Apps (with HTML/CSS)'
#     c.num_projects = 14
#     c.num_lessons = 42
#     c.save()
#     create_course_lessons(course, course_outline(course), schedule(course))
#     export_agenda(course)
#     import_agenda(course)


def export_agenda(course):
    c = Course.objects.get(name=course)
    text = f'{c.title}\n\n'
    lessons = Lesson.objects.filter(course__name=course).order_by('date')
    projects = Project.objects.filter(course__name=course).order_by('date')
    text += '\nSCHEDULE\n\n'
    for i, x in enumerate(lessons):
        text += f'    {i}, {x.date}\n'
    text += '\nPROJECTS\n\n'
    for i, x in enumerate(projects):
        text += f'    {i}, {x.date}, {x.title}, {x.project}\n'
    text += '\nLESSONS\n\n'
    for i, x in enumerate(lessons):
        text += f'    {i}, {x.date}, {x.topic}, {x.project}\n'
    agenda = f'Documents/course/{course}/agenda'
    write_file(agenda, text)


# def import_agenda(course):
#     # reset_lessons(course)
#
#     path = f'Documents/course/{course}/agenda'
#     outline = read_outline_tree(path)
#     dates = schedule(course)
#     course_record = get_course(course)
#
#     for node in outline:
#         if node[0] == 'PROJECTS':
#             for i, project in enumerate(node[1:]):
#                 date = project_due(dates, i)
#                 title = project[0].split(",")[2][1:]
#                 # print(f'DEBUG {title} - due {date}')
#                 create_project(course=course_record,
#                                date=date,
#                                title=title,
#                                project=i + 1)
#
#         if node[0] == 'LESSONS':
#             for i, lesson in enumerate(node[1:]):
#                 title = lesson[0].split(",")[2][1:]
#                 num = dates[i]['lesson']
#                 date = dates[i]['date']
#                 week = dates[i]['project']
#                 # print(f'DEBUG {date} - {title} - {week}')
#                 create_lesson(course=course_record,
#                               date=date,
#                               lesson=num,
#                               topic=title,
#                               project=week-1)
#                 p = Project.objects.get(course=course_record, project=week)
#                 p.date = date
#                 p.save()
#

def list_courses():

    return text_join([str(c) for c in Course.objects.all()])


def show_course_plan(course):
    path = doc_path(f'course/{course}/outline')
    return banner(course) + main_topics(read_file(path), 2)


def schedule(course):

    def list_unc_schedule2(start='2020-08-24', num_weeks=15):
        schedule = list_unc_schedule(start, num_weeks)
        return [(int((s[0] - 1) / 2) + 1, s[1]) for s in schedule]

    if course == 'cs350':
        sessions = list_unc_schedule2()
    else:
        sessions = list_unc_schedule()
    dates = []
    for i, d in enumerate(sessions):
        dates.append(dict(project=d[0], lesson=i+1, date=d[1].split(',')[1][1:]))
    return dates


def write_all_lessons(course):

    def create_lesson_file(path, i, lesson):
        text = lesson_markdown(i, lesson)
        if not exists(path):
            write_file(path, text)
            return f'    Write lesson {path}'
        else:
            return f'    Lesson exists {path}'

    def lesson_markdown(i, lesson):
        text = f'# Lesson {i + 1} - {lesson[0]}\n\n'
        for topic in lesson[1:]:
            text += f'\n## {topic[0]}\n'
            for subtopic in topic[1:]:
                text += f'\n### {subtopic[0]}\n\n'
                for item in subtopic[1:]:
                    text += f'* {item[0]}\n'
                    for subitem in item[1:]:
                        text += f'    * {subitem[0]}\n'
        return text

    def write_lesson_docs(course, lessons):
        log = f"\n\nWriting Lessons for {course}\n\n"
        for i, lesson in enumerate(lessons):
            path = f'Documents/course/{course}/lesson/{i+1:02}.md'
            log += create_lesson_file(path, i, lesson) + '\n'
        update_lesson_titles(course)
        return log

    def update_lesson_titles(course):
        lessons = {}
        for f in sorted(listdir(f'Documents/course/{course}/lesson')):
            if f.endswith('.md'):
                x = f.replace('.md', '')
                title = doc_title(f'course/{course}/lesson/{f}')
                title = text_replace(title, r'Lesson \d* - ', '')
                lessons[x] = title
        text = ''
        for x in lessons:
            text += lessons[x] + '\n'
        write_file(f'Documents/course/{course}/lessons', text)

    tree = course_outline(course)
    for node in tree:
        if node[0] == 'LESSON PLAN':
            return write_lesson_docs(course, node[1:])


