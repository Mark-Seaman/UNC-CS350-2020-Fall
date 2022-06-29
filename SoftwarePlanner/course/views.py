from django.views.generic import RedirectView, TemplateView, UpdateView
from os.path import exists, join, isdir

from course.models import UncStudent
from course.render import render_schedule, render_project_table, render_score
from course.view_data import course_view_data, index_data
from tool.document import list_files, render_doc
from course.slides import slides_view_data
from views.mybook import page_settings
from tool.document import doc_path
from tool.log import log_page
from views.view_data import doc_view_data


class CourseView(TemplateView):
    template_name = 'course_theme.html'

    def get_context_data(self, **kwargs):
        course = self.kwargs.get('course')
        doctype = self.kwargs.get('doctype')
        doc = self.kwargs.get('doc')
        return course_view_data(self.request.user, course, doctype, doc)


# class CourseIndex(TemplateView):
#     template_name = 'course_content.html'
#
#     def get_context_data(self, **kwargs):
#         course = self.kwargs.get('course')
#         return index_data(course)


class CourseIndexView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        return doc_view_data(f'course/Index')


class CourseRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        course = self.kwargs.get('course')
        return f'/course/{course}/Index'


class FilesView(TemplateView):
    template_name = 'files.html'

    def get_context_data(self, **kwargs):
        title = self.kwargs.get('title')
        path = join('Documents', title)
        if exists(path) and isdir(path):
            files = list_files(title)
            return page_settings(title=title, files=files)


# class LessonMatrixView(TemplateView):
#     template_name = 'lessons.html'
#
#     def get_context_data(self, **kwargs):
#         course = self.kwargs.get('course')
#         path = f'Documents/course/{course}/course.json'
#         page = f'course/{course}/Index.md'
#         # matrix = lesson_matrix(course)
#         chapters = get_chapters(course)
#         return page_settings(title=path, page=page, course=course, chapters=chapters)


class MilestonesView(TemplateView):
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):
        page = self.request.path[1:]
        doc = self.kwargs.get('course')
        path = join('course', doc)
        return page_settings(page=page, title=path, milestones=render_project_table('Project milestones', doc))


class RoleView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        course = self.kwargs.get('course')
        role = self.kwargs.get('role')
        page = f'course/{course}/plan/{role}'
        log_page(self.request, f'Course DocView - {page}')
        doc = doc_path(page)
        text = render_doc(page)
        score = render_score(page)
        return page_settings(page=page, document=doc, title=role, text=text, score=score)


class ScheduleView(TemplateView):
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):
        course = self.kwargs.get('course')
        path = f'Documents/course/{course}/Schedule'
        return page_settings(title=path, schedule=render_schedule(path))


class SlidesView(TemplateView):
    template_name = 'slides.html'

    def get_context_data(self, **kwargs):
        return slides_view_data(self.kwargs)


# class SlidesView(RedirectView):
#
#     def get_redirect_url(self, *args, **kwargs):
#         course = self.kwargs.get('course')
#         lesson = self.kwargs.get('lesson')
#         return f'http://localhost:8001/static/pages/course/{course}/slides/{lesson:02}.html'

class CoursePagesView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        course = self.kwargs.get('course')
        doctype = self.kwargs.get('doctype')
        lesson = self.kwargs.get('lesson')
        return f'/static/pages/{course}/{doctype}/{lesson:02}.html'


class CourseDocsView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        course = self.kwargs.get('course')
        doc = self.kwargs.get('doc')
        return f'/static/pages/{course}/docs/{doc}.html'


class SoftwarePlanView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        doc_path = self.get_document_name()
        return doc_view_data(doc_path)

    def get_document_name(self):
        project = self.kwargs.get('project', 'BookBuilder')
        dir = self.kwargs.get('dir', '')
        if dir:
            dir += '/'
        doc = self.kwargs.get('doc', 'Index').replace('.md', '')
        doc_path = f'swplan/{project}/{dir}{doc}.md'
        return doc_path


class StudentUpdate(UpdateView):
    model = UncStudent
    fields = ['name', 'email', 'github', 'server']
    template_name = 'student_edit.html'

    def get_context_data(self, **kwargs):
        course = self.kwargs.get('course')
        kwargs = page_settings(page=f'course/{course}', course=course)
        return super(StudentUpdate, self).get_context_data(**kwargs)

    def get_success_url(self):
        return f'/course/{self.kwargs.get("course")}'

# class UncReviewRequest(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         student = get_student('bacs200', self.request.user)
#         request_review(student)
#         return '/unc/bacs200'