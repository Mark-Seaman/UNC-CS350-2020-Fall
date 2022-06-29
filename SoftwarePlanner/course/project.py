from course.models import Project


def create_project(**kwargs):
    p = Project.objects.get_or_create(course=kwargs.get('course'), project=kwargs.get('project'))[0]
    p.date = kwargs.get('date')
    p.title = kwargs.get('title')
    p.save()


def get_project(course, project_num):
    return Project.objects.get(course__name=course, project=project_num)


def list_projects(course):
    projects = Project.objects.filter(course__name=course).order_by('project')
    return [str(x) for x in projects]


def project_due(schedule, project_num):
    for d in schedule:
        if d['project'] == project_num+1:
            date = d['date']
    return date