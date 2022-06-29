from csv import reader
from django.template.loader import render_to_string
from os import listdir
from os.path import join
from markdown import markdown

from tool.document import doc_path
from tool.files import read_file
from tool.text import text_lines
from views.view_data import render_table


# def list_lessons(course):
#     def lesson_title (path):
#         return text_lines(read_file(path))[0][2:]
#
#     lessons = sorted(listdir(doc_path(join('course', course, 'lesson'))))
#     links = []
#     for f in lessons:
#         title = lesson_title(doc_path(join('course', course, 'lesson', f)))
#         links.append((f, title))
#     return render_to_string('lessons.html', dict(course=course, files=links))


def render_milestones(course):
    title = 'Project Milestones'
    milestones = render_table(title, read_file(f'Documents/course/{course}/milestones.csv'))
    return milestones


def render_project_table(title, course):
    table = []
    with open(f'Documents/course/{course}/milestones.csv') as f:
        for i,row in enumerate(reader(f)):
            if i>0:
                roles = ['requirements', 'design', 'code', 'test']
                links = [f'<a href="/course/cs350/plan/m{i}-{x}">{x} tasks</a>' for x in roles]
                milestone_link = f'<a href="/course/cs350/plan/milestone-{row[1]}">Milestone {row[1]}</a>'
                table.append([row[0], milestone_link] + links)
    return render_to_string("table.html", dict(title=title, rows=table))


def render_schedule(course):
    title = 'Schedule of Lessons - Fall 2020'
    milestones = render_table(title, read_file(f'Documents/course/{course}/schedule.csv'))
    return milestones


def render_score(page):
    text = render_to_string('score.md', dict(goal='GOAL', requirements=[]))
    return markdown(text)


