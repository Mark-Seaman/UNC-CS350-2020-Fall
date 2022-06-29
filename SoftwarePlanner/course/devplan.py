from django.template.loader import render_to_string

from course.lesson import  get_course
from course.outline import read_outline_tree
from tool.files import read_file, read_json, write_file, write_json


LIFECYCLE_MILESTONES = []


# def create_content_outline(course):
#     data = read_dev_plan(f'course/{course}/plan')
#     lessons = update_lessons(data)
#     c = get_course(course)
#     outline = f'{c.title}\n\n'
#     outline += "LESSON PLAN\n\n"
#     for w, p in enumerate(lessons):
#         outline += f'\n    Project {p[0]["milestone"]}\n\n'
#         for lesson in p:
#             outline += f"        {lesson['title']}\n"
#     path = f'Documents/course/{course}/outline'
#     write_file(path, outline)


def create_doc_file(path, deliver):
    with open(path, 'w') as f:
        f.write(deliver)
    return f'    {path}'


def create_milestone_instructions(milestone, milestone_label):
    milestone = milestone + 1
    title = f"Milestone {milestone} - {milestone_label}"
    req = read_task_file(milestone, 'requirements')
    design = read_task_file(milestone, 'design')
    code = read_task_file(milestone, 'code')
    test = read_task_file(milestone, 'test')
    data = dict(title=title, requirements=req, design=design, code=code, test=test,
                description='This milestone is for some unknown purpose.  Just do it anyway!')
    text = render_to_string('milestone.md', data)
    path = f'Documents/course/cs350/plan/milestone-{milestone}'
    create_doc_file(path, text) + '\n'
    return path


def lifecycle_roles():
    return [
        dict(role='requirements', name='Project Manager - Requirements'),
        dict(role='design', name='Designer - Design'),
        dict(role='code', name='Programmer - Code'),
        dict(role='test', name='QA Engineer - Test'),
    ]


def read_dev_plan(plan):
    return read_json(f'Documents/{plan}/devplan.json')


def read_task_file(milestone, role):
    path = f'Documents/course/cs350/plan/m{milestone}-{role}'
    return read_file(path)


def role_label(role):
    roles = ['requirements', 'design', 'code', 'test', 'tdd']
    return roles[role]


def show_dev_plan_data(data):
    text = f'Milestones: {data["milestones"]}\n\n'
    text += f'Roles: {data["roles"]}\n\n'
    tasks = data["tasks"]
    text += f'Tasks:\n\n'
    for x in tasks:
        text += f"    {x}\n"
        for key in tasks[x]:
            text += f"        {key} : {tasks[x][key]}\n"
    return text


def update_dev_plan(course, plan):

    def milestone_title(m, milestones):
        return f"Milestone #{m + 1} - {milestones[m]}"

    def get_milestone_data(tree):
        return {i: m[0] for i, m in enumerate(tree[1:])}

    def get_lessons_data(tree):
        return {i: m[0] for i, m in enumerate(tree[1:])}

    def get_roles_data(tree, milestones):
        deliverables = {}

        for r, role in enumerate(tree[1:]):
            for m, milestone in enumerate(milestones):
                key = f'{m}/{r}'
                deliver = role[1:][m][0]
                details = [x[0] for x in role[1:][m][1:]]
                deliverables[key] = dict(role=r, role_name=role[0], deliverable=deliver, details=details, milestone=m,
                                         milestone_name=milestone_title(m, milestones))
        return deliverables

    def create_dev_plan(course):
        data = {}
        path = f'Documents/course/{course}/devplan.outline'
        # print(path)
        tree = read_outline_tree(path)[0]

        for topic in tree:
            # print(topic)
            if topic[0] == 'Software Checklist Milestones':
                m = get_milestone_data(topic)
                data['milestones'] = m
            if topic[0] == 'Development Role Responsibility':
                r = get_roles_data(topic, data['milestones'])
                data['tasks'] = r
                data['roles'] = lifecycle_roles()
            if topic[0] == 'Special Lessons':
                data['special-lessons'] = get_lessons_data(topic)
        return data

    def write_dev_plan(plan, data):
        write_json(f'Documents/{plan}/devplan.json', data)

    data = create_dev_plan(course)
    return write_dev_plan(plan, data)


# def write_plan_docs(milestones, roles, tasks):
#     log = "\n\nWriting Documents for Development Plan\n\n"
#     for m in range(7):
#         # print(f'    Milestone {m + 1}: {milestones[m]}')
#         for r in range(4):
#             text = write_task_file(m, r, milestones, roles)
#             log += text + '\n'
#         # log += f'    Milestone {m + 1}: {milestones[m]}' + '\n'
#         log += f'{create_milestone_instructions(m, milestones[m])}\n'
#     return log
#
#
# def write_task_file(m, r, milestones, roles):
#     deliver = roles[f'{m}/{r}']
#     role = role_label(deliver["role"])
#     milestone = f"m{deliver['milestone'] + 1}"
#     path = f'Documents/course/cs350/plan/{milestone}-{role}'
#     delivery = dict(
#         milestone=m + 1,
#         milestone_label=milestones[m],
#         role=role,
#         goal=deliver["deliverable"],
#         description='This milestone is for some unknown purpose.  Just do it anyway!',
#         requirements=deliver["details"],
#     )
#
#     text = render_to_string('task.md', delivery)
#     create_doc_file(path, text) + '\n'
#     return path


# def update_lessons(plan):
#
#     def milestone_name(m, plan):
#         milestone = plan["milestones"][str(m)]
#         return f"Milestone #{m + 1} - {milestone}"
#
#     def role_label(role, m, plan):
#         milestone = plan["milestones"][str(m)]
#         labels = ['Requirements', 'Design', 'Code', 'Test']
#         return f"{labels[role]} - {milestone}"
#
#     milestones = []
#     lessons = {}
#     for milestone in range(7):
#         project_lessons = []
#         for task in range(6):
#
#             delivery = None
#             details = None
#             if task == 0:
#                 lesson = milestone * 6 + 1
#                 path = f'{lesson:02}.md'
#                 title = milestone_name(milestone, plan)
#                 style = 'cell-dark'
#                 details = milestone_name(milestone, plan)
#             elif task < 5:
#                 lesson = milestone * 6 + task + 1
#                 path = f'{lesson:02}.md'
#                 title = role_label(task-1, milestone, plan)
#                 style = ['cell-dark', 'cell-blue', 'cell-green', 'cell-orange', 'cell-red', 'cell-light'][task]
#                 delivery = plan['tasks'][f'{milestone}/{task-1}']
#             else:
#                 lesson = milestone * 6 + 6
#                 path = f'{lesson:02}.md'
#                 title = f'Special Topic #{milestone+1}'
#                 style = 'cell-light'
#                 details = 'No Special details'
#             m = milestone_name(milestone, plan)
#             x = dict(url=path, lesson=lesson, title=title, style=style, milestone=m, details=details, delivery=delivery)
#             project_lessons.append(x)
#             lessons[lesson] = x
#         milestones.append(project_lessons)
#     return milestones
