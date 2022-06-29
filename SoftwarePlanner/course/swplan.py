from os.path import exists

from course.devplan import read_dev_plan
from course.lesson import get_lesson
from course.models import Lesson
from tool.files import read_json, read_lines, write_file


# def generate_BookBuilder_docs():
#     plan = 'course/cs350/plan'
#     github = 'https://github.com/Mark-Seaman'
#     repo = 'Mark-Seaman.github.io'
#     path = 'blob/master/BookBuilder'
#     project = dict(name='Book Builder',
#                    docs=f'Documents/swplan/BookBuilder',
#                    github=github,
#                    repo=repo,
#                    path=path,
#                    github_path=f'{github}/{repo}/{path}')
#     plan = read_dev_plan(plan)
#     milestones = plan['milestones']
#     roles = plan['roles']
#     tasks = plan['tasks']
#     return write_project_plan(project, milestones, roles, tasks)


def create_project_deliverable(project, milestones, tasks, m, r):
    t = f'{m}/{r}'
    task = tasks[t]
    role = role_label_name(int(r))
    filename = f'Milestone-{int(m)+1}/{role}'
    text = f'# Milestone {int(m)+1}. {milestones[m]} - {role}\n\n'
    text += f'\n## PROJECT INFO\n\n'
    text += f'* [Software Project Plan - {project["name"]}](../Index.md)\n\n'
    text += f'* Other Roles - {list_role_docs()}\n\n\n'
    text += f'* File: {filename}.md\n\n'
    text += f'* URL: {project["github_path"]}/{filename}.md\n\n'
    text += f'* Documents: {project["docs"]}\n\n'
    text += f'* Git Repo: {project["repo"]}\n\n'
    text += f'\n\n\n### Milestone {int(m)+1}. {milestones[m]}\n\n'
    text += f'\n\nRole: {task["role_name"]}\n'
    text += f'\nGoal: {task["deliverable"]}\n\n'
    for d in task["details"]:
        text += f'* {d}\n'
    text += f'\n\n\n## {project["name"]} - {task["deliverable"]}\n\n'
    for d in task["details"]:
        text += f'\n\n### {d}\n'
    return text


def list_role_docs():
    return ', '.join([f'[{role_label_name(r)}.md]({role_label_name(r)}.md)\n' for r in range(4)])


def project_links_text(project):
    text = f'# Software Project Plan - {project["name"]}\n\n'
    text += f'\n## PROJECT INFO\n'
    text += f'* Documents: {project["docs"]}\n'
    text += f'* File: {project["docs"]}/Index.md\n'
    text += f'* Github Account: [{project["github"]}]({project["github"]})\n'
    text += f'* Git Repo: {project["repo"]}\n'
    text += f'* Git Path: {project["path"]}\n'
    text += f'* Git File: [{project["github_path"]}/Index.md]({project["github_path"]}/Index.md)\n'
    text += f'\n### ROLES\n\n* Requirements - Project Manager\n* Design - Tech Lead\n* Code - Programmer\n* Test - QA Engineer\n\n'
    text += f'\n### TOOLS\n\n* Django & Python\n* Github\n* Brackets\n* Python Anywhere\n\n'
    text += f'\n### TEAM\n\n* Mark Seaman\n\n'
    text += f'\n### MILESTONES\n\n'
    return text


def role_label_name(role):
    roles = ['Requirements', 'Design', 'Code', 'Test']
    return roles[role]


def syllabus_schedule(course):
    text = "Schedule of Topics\n\n"
    lessons = Lesson.objects.filter(course__name=course).order_by('date')
    for i, x in enumerate(lessons):
        text += f'{x.date} - {x.topic}\n'
    return text


def update_lesson_titles(course):
    if course == 'cs350':
        path = f'Documents/course/{course}/course.json'
        data = read_json(path)
        lesson_num = 1
        for project in data['lessons']['table']:
            for lesson in project:
                if lesson['delivery']:
                    x = get_lesson(course, lesson_num)
                    x.topic = lesson["delivery"]["deliverable"]
                    x.save()
                else:
                    x = get_lesson(course, lesson_num)
                    x.topic = lesson["title"]
                    x.save()
                lesson_num += 1
    if course == 'bacs200':
        lessons = f'Documents/course/{course}/lesson-topics'
        for i, lesson in enumerate(read_lines(lessons)):
            # print(i+1, lesson)
            o = get_lesson(course, i+1)
            o.topic = lesson
            o.save()


def task_filename(milestone, role):
    filename = f'Milestone-{int(milestone) + 1}/{role_label_name(int(role))}.md'
    return filename


def write_milestone_index(path, m, project, milestones, tasks):
    text = f'# Milestone {int(m) + 1}. {milestones[m]}\n'
    for r in range(4):
        t = f'{m}/{r}'
        task = tasks[t]
        text += f'\n\n### Role: {task["role_name"]}\n'
        text += f'\nGoal: {task["deliverable"]}\n\n'
        filename = f'{role_label_name(r)}.md'
        text += f'\nDocument: [{filename}]({filename})\n\n'
        for d in task["details"]:
            text += f'* {d}\n'
    if not exists(path):
        write_file(path, text)
        return f'Writing {path}\n'


def write_project_plan(project, milestones, roles, tasks):
    log = "\n\nWriting Documents for Development Plan\n\n"
    text = project_links_text(project)
    for doc in milestones:
        text += f'* [{int(doc) + 1}. {milestones[doc]}](Milestone-{int(doc) + 1}/Index.md)\n'
    path = f'{project["docs"]}/Index.md'
    if not exists(path):
        write_file(path, text)
        log += f'Writing {path}\n'
    for m in milestones:
        path = f'{project["docs"]}/Milestone-{int(m) + 1}/Index.md'
        write_milestone_index(path, m, project, milestones, tasks)

        for r in range(4):
            path = f'{project["docs"]}/{task_filename(m, r)}'
            text = create_project_deliverable(project, milestones, tasks, f'{m}', f'{r}')
            if not exists(path):
                write_file(path, text)
                log += f'Writing {path}\n'
    return log

