from course.appteam import get_team, list_teams, team_members
from course.models import Teamwork


def create_teamwork_surveys():
    def create_team_survey(milestone, team):
        for m1 in team_members(team):
            for m2 in team_members(team):
                if m1 != m2:
                    print(m1.student.name, ' -- ', m2.student.name)
                    Teamwork.objects.get_or_create(student=m1.student, teammate=m2.student, milestone=milestone)

    def create_teamwork_survey(milestone):
        for team in list_teams():
            create_team_survey(milestone, team)

    # create_teamwork_survey(0)
    # create_teamwork_survey(1)
    create_teamwork_survey(2)


def get_teamwork_data(student):

    def milestone_surveys(student, milestone):
        return Teamwork.objects.filter(student=student, milestone=milestone)

    return [(1, milestone_surveys(student, 0)),
            (2, milestone_surveys(student, 1)),
            (3, milestone_surveys(student, 2))]


def teamwork_summary():

    def milestone_summary(milestone):
        results = []
        not_done = []
        for t in Teamwork.objects.filter(milestone=milestone):
            score = (1 if t.question_1 else 0) + (1 if t.question_2 else 0) + (1 if t.question_3 else 0)
            if t.notes:
                results.append(dict(teamwork=t, team=get_team(t.teammate), score=score))
            else:
                not_done.append(dict(teamwork=t, team=get_team(t.teammate), score=score))
        return milestone+1, results, not_done

    return [milestone_summary(2)]