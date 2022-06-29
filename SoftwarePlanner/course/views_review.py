from django.views.generic import DetailView, ListView, UpdateView

from course.models import Review
# from course.review import count_score, get_review, render_review, render_reviews
from course.review import review_detail_data, review_list_data
from views.mybook import page_settings


class ReviewList(ListView):
    model = Review
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ReviewList, self).get_context_data(**kwargs)
        return review_list_data(**kwargs)


class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ReviewDetail, self).get_context_data(**kwargs)
        return review_detail_data(**kwargs)

        # kwargs['requirements'] = checklist_values(self.kwargs['pk'])
        # course = self.kwargs.get('course')
        # kwargs.update(page_settings(page=f'course/{course}', course=course))
        # return kwargs


class ReviewEdit(UpdateView):
    model = Review
    fields = '__all__'
    template_name = 'review_edit.html'

    def get_context_data(self, **kwargs):
        kwargs = super(ReviewEdit, self).get_context_data(**kwargs)

        # return review_list_data(**kwargs)
        # pk = self.kwargs.get('pk')
        # review = get_review(pk)
        #
        # page = f'course/{course}/reviews'
        # labels = [r.strip() for r in review.requirement_labels.split('\n')]
        # kwargs = dict(title='Design Review', labels=labels, )
        # kwargs = super(ReviewEdit, self).get_context_data(**kwargs)
        course = self.kwargs.get('course')
        kwargs.update(page_settings(page=f'course/{course}', course=course))
        return kwargs

    # def form_valid(self, form):
    #     self.object.score = 5 # count_score(self.object)
    #     self.object.date = now()
    #     return super(ReviewEdit, self).form_valid(form)

    def get_success_url(self):
        student = self.object.reviewer
        return f'/course/{student.course.name}/reviews'


# class ReviewFeedback(TemplateView):
#     template_name = 'review_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs = super(ReviewFeedback, self).get_context_data(**kwargs)
#         pk = kwargs.get('pk')
#         course = kwargs.get('course')
#         page = f'course/{course}/reviews'
#         kwargs.update(render_review(pk))
#         kwargs.update(page_settings(page=page, course=course))
#         return kwargs
#
#
# class Reviews(TemplateView):
#     template_name = 'reviewer_todo.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs = super(Reviews, self).get_context_data(**kwargs)
#         course = self.kwargs.get('course')
#         page = f'course/{course}/reviews'
#         student = get_student(course, self.request.user)
#         kwargs.update(render_reviews(student))
#         kwargs.update(page_settings(page=page, course=course))
#         return kwargs

