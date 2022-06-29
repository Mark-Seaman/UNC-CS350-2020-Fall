from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView

from views.mybook import page_settings
from .appteam import team_view_data
from .models import AppTeam, Checklist
from .students import get_teacher


class TeamUpdateView(UpdateView):
    model = Checklist
    template_name = 'checklist_edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        kwargs = super(TeamUpdateView, self).get_context_data(**kwargs)
        page = 'course/cs350'
        course = kwargs.get('course')
        if get_teacher(self.request.user):
            kwargs.update(page_settings(page=page, course=course))
            return kwargs


class TeamsView(ListView):
    model = AppTeam
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        kwargs = super(TeamsView, self).get_context_data(**kwargs)
        kwargs.update(team_view_data(get_teacher(self.request.user)))
        return kwargs


class TeamView(DetailView):
    model = AppTeam
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        kwargs = super(TeamView, self).get_context_data(**kwargs)
        kwargs.update(team_view_data(get_teacher(self.request.user), kwargs['object']))
        return kwargs


