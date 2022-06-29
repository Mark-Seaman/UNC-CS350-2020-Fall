from django.views.generic import TemplateView, UpdateView

from course.teamwork import teamwork_summary
from course.models import Teamwork
from course.view_data import teacher_data
from views.mybook import page_settings


class TeamworkEdit(UpdateView):
    model = Teamwork
    fields = ['question_1', 'question_2', 'question_3', 'notes']
    template_name = 'teamwork_edit.html'
    success_url = '/course/cs350'

    def get_context_data(self, **kwargs):
        kwargs = super(TeamworkEdit, self).get_context_data(**kwargs)
        page = self.request.path[1:]
        m = kwargs.get('object').milestone+1
        course = kwargs.get('course')
        kwargs.update(page_settings(page=page, course=course, milestone=m))
        return kwargs


class TeamworkSummary(TemplateView):
    template_name = 'teamwork_summary.html'

    def get_context_data(self, **kwargs):
        kwargs = super(TeamworkSummary, self).get_context_data(**kwargs)
        page = self.request.path[1:]
        if teacher_data(self.request.user):
            course = kwargs.get('course')
            teamworks = teamwork_summary()
            kwargs.update(page_settings(page=page, course=course, teamworks=teamworks))
            return kwargs