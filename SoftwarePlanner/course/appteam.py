from course.models import AppTeam, Checklist, TeamMember, UncStudent
from tool.document import doc_content
from tool.files import read_file
from tool.text import text_lines
from views.mybook import page_settings
from .devplan import role_label
from .models import AppTeam, TeamMember


def add_team_member(team, member):
    t = AppTeam.objects.get_or_create(name=team[:19])[0]
    if t:
        student = find_student(member)
        id = len(TeamMember.objects.filter(team=t)) + 1
        m = TeamMember.objects.get_or_create(student=student, team=t)[0]
        m.member_id = id
        m.save()


def assign_role(member, milestone, has_five):
    if milestone > 3 and has_five:
        role = (member.member_id + milestone) % 5
    else:
        role = ((member.member_id + milestone - 2) % 4)
    return dict(name=member.student.name, role=role_label(role))


# def assign_roles(milestone, members):
#     return [dict(name=x, role=role_label(milestone - 1)) for i, x in enumerate(members)]

def cleanup_records():
    for team in list_teams():
        checklist = Checklist.objects.filter(milestone=4, team=team)
        if len(checklist)>1:
            checklist[0].delete()
            # print(len(checklist))


def create_milestone_checklists(milestone):
    def get_milestone_requirements(milestone):
        req = []
        for line in text_lines(read_file('Documents/course/cs350/docs/Milestones.md')):
            if line.startswith('        *'):
                req.append(line[10:])
        return req[milestone * 16:(milestone + 1) * 16]

    def milestone_requirements(milestone):
        labels = get_milestone_requirements(milestone - 1)
        return {f'label_{k + 1}': x for k, x in enumerate(labels)}

    def create_milestone_checklist(milestone, team):
        args = dict(milestone=milestone, team=team)
        args.update(milestone_requirements(milestone))
        # print(args)
        Checklist.objects.get_or_create(**args)

    for team in list_teams():
        create_milestone_checklist(milestone, team)


def find_student(name):
    student = UncStudent.objects.filter(name=name, course__name='cs350')
    if student:
        return student[0]
    else:
        print(name, 'not found')
        return UncStudent.objects.get(name='Mark Seaman', course__name='cs350')


def get_team(student):
    team = TeamMember.objects.filter(student=student)
    if team:
        return team[0].team


def import_teams():
    TeamMember.objects.all().delete()
    AppTeam.objects.all().delete()
    for line in text_lines(doc_content('course/cs350/docs/AppTeams.md')):
        if line.startswith('### '):
            team = line[4:]
        elif line.startswith('    '):
            add_team_member(team, line[4:])
    print_teams()


def list_teams():
    return AppTeam.objects.all()


def print_teams():
    text = 'App Teams for CS 350'
    for team in list_teams():
        text += str(team) + '\n'
        for member in team_members(team):
            text += f'    {member.member_id}. - {member.student.name}\n'
    return text


def team_members(team):
    return team.teammember_set.all()


def checklist_values(team, milestone=None):

    def sign_off(checklist, i):
        return dict(met=checklist[f'requirement_{i + 1}'], label=checklist[f'label_{i + 1}'],
                    notes=checklist[f'notes_{i + 1}'])

    def get_checklist_data(values):
        checks = [sign_off(values, i) for i in range(16)]
        checks = [(role_label(i), checks[i * 4:i * 4 + 4]) for i in range(4)]
        return checks

    checklists = Checklist.objects.filter(team_id=team)
    if milestone:
        checklists = checklists.filter(milestone=milestone)
    return [get_checklist_data(checklist) for checklist in checklists.values()]


def team_view_data(teacher, team=None):

    def team_milestone_roles(team, milestone):
        has_five = (len(team_members(team)) == 5)
        return [assign_role(member, milestone, has_five) for member in team_members(team)]

    def get_checklist(team, milestone):
        return Checklist.objects.filter(team=team, milestone=milestone)

    def get_milestone_data(team, milestone):
        roles = team_milestone_roles(team, milestone)
        checklist = get_checklist(team, milestone)
        checks = checklist_values(team.pk, milestone)
        return dict(team=team, milestone=milestone, checklist=checklist, checks=checks, roles=roles)

    page = 'course/cs350'
    if team:
        milestones = [get_milestone_data(team, m+1) for m in range(5)]
        return page_settings(page=page, course='cs350', teacher=teacher, milestones=milestones)
    else:
        return page_settings(page=page, course='cs350', teacher=teacher)


# def print_team_members(milestone):
#     print(f'\n\nMilestone {milestone}\n')
#     for team in list_teams():
#         print('   ', team)
#         for member in team_members(team):
#             has_five = (len(team_members(team)) == 5)
#             role = assign_role(member, milestone, has_five)["role"]
#             print(f'       {member.member_id}. {member.student.name} - {role}')


# def reassign_teams():
#
#     def reassign(name, team):
#         team = AppTeam.objects.get(name=team)
#         member = TeamMember.objects.get(student__name=name)
#         member.team = team
#         member.member_id = 5
#         member.save()
#
#     reassign('Marcus Arata', 'ElBow Space')
#     reassign('Christian Hogue', 'SMS Twitter')
#     reassign('Seth Holland', 'Easel')
#     reassign('Jacob Schroeder', 'Capture Webapp')