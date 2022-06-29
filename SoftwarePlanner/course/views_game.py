from django import forms
from django.forms import Form
from django.views.generic import FormView, TemplateView

from course.models import UrlGame
from course.students import get_student
from course.urlgame import generate_url_question, get_hint, url_feedback
from views.mybook import page_settings


class UncUrlGameAnswer(FormView):

    class UrlForm(Form):
        answer = forms.CharField()
        url = forms.CharField()
        url_type = forms.CharField()
        page = forms.CharField()
        correct = forms.CharField()
        answered = forms.IntegerField()
        left = forms.IntegerField()

    form_class = UrlForm
    template_name = 'urlgame.html'

    def get_context_data(self, **kwargs):
        kwargs = super(UncUrlGameAnswer, self).get_context_data(**kwargs)
        course = self.kwargs.get('course')
        page = f'course/{course}'
        student = get_student(course, self.request.user)
        kwargs.update(page_settings(page=page, course=course, title='URL Crusher'))

        # student = get_student('bacs200', self.request.user)
        # header = ['UNC BACS', student.name, "/static/images/unc/Bear.200.png", 'UNC Bear']
        # kwargs['header'] = dict(title=header[0], subtitle=header[1], logo=header[2], logo_text=header[3])

        self.answer = self.request.GET.get('answer', "None")
        self.page = self.request.GET.get('page', "None")
        self.url = self.request.GET.get('url', "None")
        self.url_type = self.request.GET.get('url_type', "None")
        self.correct = self.request.GET.get('correct', 'None')
        self.iscorrect = (self.request.GET.get('iscorrect') == u'True')
        self.image = self.request.GET.get('image')
        hint = get_hint(self.url_type)

        answer = dict(a=dict(answer=self.answer, url=self.url, correct=self.correct, image=self.image,
                      page=self.page, url_type=self.url_type, iscorrect=self.iscorrect, hint=hint))

        game = UrlGame.objects.get_or_create(student=student)[0]
        game = dict(correct=game.correct, incorrect=game.answered - game.correct, answered=game.answered, left=game.left)

        kwargs.update(answer)
        kwargs.update(game)
        return kwargs

        # return dict(title=title, student=student, a=answer, answered=game.answered, correct=game.correct, incorrect=game.answered-game.correct, left=game.left)

    def form_valid(self, form):
        student = get_student('bacs200', self.request.user)
        game = UrlGame.objects.get_or_create(student=student)[0]

        self.url = form.data.get('url')
        self.answer = form.data.get('answer')
        self.correct = form.data.get('correct')
        self.page = form.data.get('page')
        self.url_type = form.data.get('url_type')

        self.iscorrect = (self.correct == self.answer)
        if self.iscorrect:
            game.left = game.left - 1
            game.correct += 1
        else:
            game.left = 10
        game.answered = game.answered + 1
        game.save()

        return super(UncUrlGameAnswer, self).form_valid(form)

    def get_success_url(self):
        student = get_student('bacs200', self.request.user)
        game = UrlGame.objects.get_or_create(student=student)[0]
        if game.left < 1:
            return '/course/bacs200/url-game-done'
        else:
            parms = '&'.join([
                "answer=%s" % self.answer,
                "url=%s" % self.url,
                "correct=%s" % self.correct,
                "page=%s" % self.page,
                "url_type=%s" % self.url_type,
                "image=%s" % url_feedback(self.answer, self.correct),
                "iscorrect=%s" % self.iscorrect,
            ])
            return '/course/bacs200/url-answer?%s' % parms


class UncUrlGameQuestion(TemplateView):
    template_name = 'urlgame.html'

    def get_context_data(self, **kwargs):
        kwargs = super(UncUrlGameQuestion, self).get_context_data(**kwargs)
        course = self.kwargs.get('course')
        page = f'course/{course}'
        student = get_student(course, self.request.user)
        kwargs.update(page_settings(page=page, course=course, title='URL Crusher'))

        game = UrlGame.objects.get_or_create(student=student)[0]
        question = generate_url_question()
        # return dict(title=title, student=student, q=question, correct=game.correct, incorrect=game.answered-game.correct, answered=game.answered, left=game.left)
        game = dict(q=question, correct=game.correct, incorrect=game.answered-game.correct, answered=game.answered, left=game.left)
        kwargs.update(game)

        return kwargs


class UncUrlGameDone(TemplateView):
    template_name = 'urlgame_done.html'

    def get_context_data(self, **kwargs):
        kwargs = super(UncUrlGameDone, self).get_context_data(**kwargs)
        course = self.kwargs.get('course')
        page = f'course/{course}'
        student = get_student(course, self.request.user)
        kwargs.update(page_settings(page=page, course=course, title='URL Crusher', student=student))
        game = UrlGame.objects.get_or_create(student=student)[0]
        game = dict(correct=game.correct, incorrect=game.answered-game.correct, answered=game.answered, left=game.left)
        kwargs.update(game)
        return kwargs