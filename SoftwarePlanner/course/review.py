from django.template.loader import render_to_string

from course.project import get_project
from tool.document import text_to_html
from tool.files import read_file
from tool.text import text_join, text_lines
from course.models import Course, Review, Project, UncStudent, UrlGame
# from course.review import render_notes, requirements_met


# ------------------------
#  New Review Logic
from views.mybook import page_settings


def assign_review_pair(project_id, s1, s2):
    print(f'    Review: {s1.name}, {s2.name}')
    print(f'    Review: {s2.name}, {s1.name}')
    project = get_project(s1.course.name, project_id)
    print(assign_review(project, s1, s2))
    assign_review(project, s2, s1)


def assign_review(project, s1, s2):

    def get_labels(project):
        f = f'Documents/course/{project.course.name}/project/requirements-{project.project}'
        return text_lines(read_file(f))

    def requirements(project):
        labels = get_labels(project)
        return {f'label_{k + 1}': x for k, x in enumerate(labels)}

    def create_review_checklist(reviewer, designer, page):
        args = dict(reviewer=reviewer, designer=designer, page=page)
        args.update(requirements(project))
        print(args)
        Review.objects.create(**args)

    return create_review_checklist(s1, s2, 'bacs200/index.html')


def checklist_values(review_id):

    def sign_off(checklist, i):
        met = checklist[f'requirement_{i + 1}']
        label = checklist[f'label_{i + 1}']
        return dict(met=met, label=label)

    def get_checklist_data(values):
        checks = [sign_off(values, i) for i in range(10)]
        return checks

    checklist = Review.objects.filter(pk=review_id).values()[0]
    return get_checklist_data(checklist)


def print_reviews():
    print('Design Reviews')
    reviews = Review.objects.all()
    for r in reviews:
        print(r)
    print('%d Reviews Assigned' % len(reviews))
    print('%s Students' % len(UncStudent.objects.all()))


def review_detail_data(**kwargs):
    course = kwargs.get('course')
    if kwargs.get('object'):
        r = kwargs.get('object')
        checks = checklist_values(r.pk)
        kwargs['requirements'] = checks
        title = f'Requirements Met'
    kwargs.update(page_settings(page=f'course/{course}', course=course, title=title))
    return kwargs


def review_list_data(**kwargs):
    course = kwargs.get('course')
    reviews = get_review_data()
    title = 'Design Reviews'
    kwargs.update(page_settings(page=f'course/{course}', course=course, title=title, reviews=reviews))
    return kwargs


def review_feedback(student_id):
    return Review.objects.filter(designer=student_id).exclude(score=-1)


def student_reviews_todo(student_id):
    return Review.objects.filter(reviewer=student_id, score=-1)


def student_reviews_done(student_id):
    return Review.objects.filter(reviewer=student_id).exclude(score=-1)


def get_review_data(student=None):
    to_do_text = '''
         Complete these reviews to give timely, accurate, and helpful feedback.
         '''
    done_text = '''
         You have completed these reviews.  You can updated them at any time with new information.
         '''
    feedback_text = '''
         These reviews are for feedback on your design work.
         '''

    def review_content(i, active, title, reviews, description, edit, show):
        card = dict(id=i, title=title,  reviews=reviews, description=description, edit=edit, detail=show)
        if active:
            card['show'] = 'show'
            card['active'] = 'true'
        return card

    reviews = Review.objects.all()
    reviews_to_do   = review_content(1, True,  'Reviews To Do',   reviews, to_do_text,    True, False)
    reviews_done    = review_content(2, False, 'Reviews Done',    reviews, done_text,     True, False)
    feedback        = review_content(3, False, 'Design Feedback', reviews, feedback_text, False, True)

    data = [reviews_to_do, reviews_done, feedback]
    return data


# ------------------------
#  Old Review Logic
#
#
# def assign_review_pair(s1, s2, project_id, date):
#     # print('    Review: %s, %s' % (s1.name, s2.name))
#     # print('    Review: %s, %s' % (s2.name, s1.name))
#     page = 'bacs200/index.html'
#     requirements = get_requirements(project_id)
#     notes = 'Add a description of all the problems found'
#     create_review(s1.pk, s2.pk, page, requirements, notes, date)
#     create_review(s2.pk, s1.pk, page, requirements, notes, date)
#
#
# # def assign_team_reviews():
# #
# #     def review_pairs(groups):
# #         x = []
# #         for team in groups:
# #             for reviewer in team:
# #                 for designer in team:
# #                     if reviewer != designer:
# #                         x.append((designer, reviewer))
# #         return x
# #
# #     teams = review_teams()
# #     pairs = review_pairs(teams)
# #     print(f'{len(pairs)} Review Pairs in class')
# #     # print(pairs)
# #     for p in pairs:
# #         project = 14
# #         due = '2020-05-01'
# #         # print(f'assign_review_pair {p[0]}, {p[1]}, project {project}, {due}')
# #         # print(p[0])
# #         s1 = Student.lookup(p[0])
# #         s2 = Student.lookup(p[1])
# #         assign_review_pair(s1, s2, project, due)
#
#
# # def assign_self_reviews():
# #     date = '2020-03-27'
# #     for student in Course.students('bacs200'):
# #     # student = Student.get_record(98)
# #         assign_review_pair(student, student, 1, date)  # Project #1
# #         assign_review_pair(student, student, 2, date)  # Project #2
# #         assign_review_pair(student, student, 8, date)  # Project #8
# #         assign_review_pair(student, student, 9, date)  # Project #9
#
#
# # def build_review_team(student):
# #     ReviewTeam.objects.create(student=student)
# #     if (len(ReviewTeam.objects.all()) % 4) == 0:
# #         ReviewTeam.objects.all().delete()
#
#
# def count_score(r):
#     requirements = [r.requirement_1, r.requirement_2, r.requirement_3, r.requirement_4, r.requirement_5,
#                     r.requirement_6, r.requirement_7, r.requirement_8, r.requirement_9, r.requirement_10]
#     return len([x for x in requirements if x])
#
#
# def create_review(reviewer, designer, page, requirements):
#     r = Review.objects.get_or_create(reviewer_id=reviewer, designer_id=designer, page=page)[0]
#     r.requirement_labels = requirements
#     r.notes = 'Add notes for improving this page.'
#     r.save()
#     return r
#
#
# def get_requirements(project):
#     requirements = open(f'Documents/course/bacs200/project/{project}-requirements').read()
#     return requirements
#
#
# def get_review(id):
#     return Review.objects.get(pk=id)
#
#
# def grade_reviews(page):
#     print('\nTo Do ' + page)
#     for r in Review.objects.filter(page=page, score=-1):
#         print("    " + r.reviewer.name)
#     print('\nDone ' + page)
#     for r in Review.objects.filter(page=page).exclude(score=-1):
#         print("    " + r.reviewer.name)
#
#
# def reviewer_scores(student_id):
#     reviews = student_reviews_done(student_id)
#     return [r.score for r in reviews]
#
#
# def designer_scores(student_id):
#     reviews = review_feedback(student_id)
#     return [r.score for r in reviews]
#
#
# # def request_review(student):
# #     print("Request Review: %s " % student)
# #     for team in ReviewTeam.objects.all():
# #         assign_review_pair(team.student, student)
# #     build_review_team(student)
#
#
# def review_feedback(student_id):
#     return Review.objects.filter(designer=student_id).exclude(score=-1)
#
#
# def student_project_data(course):
#     data = []
#     for s in Course.students(course):
#         data.append(dict(student=s, designer=designer_scores(s.pk), reviewer=reviewer_scores(s.pk)))
#     return data
#
#
# def student_reviews_todo(student_id):
#     return Review.objects.filter(reviewer=student_id, score=-1)
#
#
# def student_reviews_done(student_id):
#     return Review.objects.filter(reviewer=student_id).exclude(score=-1)
#
#
# def show_students(course):
#     print('Students - %s' % len(Course.students(course)))
#     for s in Course.students(course):
#         print('%s. %s' % (s.pk, s.name))
#
#
# def student_project_data(course):
#     data = []
#     for s in Course.students(course):
#         game = UrlGame.objects.filter(student=s)
#         if game:
#             game = game[0].left
#         else:
#             game = 10
#         data.append(dict(student=s, urlgame=game, designer=designer_scores(s.pk), reviewer=reviewer_scores(s.pk)))
#     return data
#
#
# def print_reviews():
#     print('Design Reviews')
#     reviews = Review.objects.all()
#     for r in reviews:
#         print(r)
#     print('%d Reviews Assigned' % len(reviews))
#     print('%s Students' % len(UncStudent.objects.all()))
#
#
# def schedule_teacher_review():
#     s = UncStudent.lookup('Sensei 200')
#     print(s)
#     project = Project.lookup('bacs200', 1)
#     page, requirements, notes = 'index.php', get_requirements(), 'Add a description of all the problems found'
#     create_review(s.pk, s.pk, project, requirements, notes)
#
#
# # def verify_students():
# #     for team in review_teams():
# #         for student in team:
# #             print(student)
# #             s = Student.lookup(student)
# #             print(s.pk, s.name)
# #
# #
# # def review_teams():
# #     # print(text_join([t for t in teams]))
# #     members = [text_lines(t)[1:-1] for t in teams]
# #     return members
# #     # team = {}
# #     # students = [str(s.name) for s in Course.students('bacs200')]
# #     # for i in range(10):
# #     #     team[i] = students[i*5:i*5+5]
# #     #     members = text_join([m.name for m in team[i]])
# #     #     print(f'\nTeam[{i+1}] :\n{members}')
# #     # print(text_join(students))
# #     # print(len(text_lines(students)))
#
#
# def render_notes(review):
#     return text_to_html(review.notes)
#
#
# def requirements_met(review):
#     def status(req):
#         return '<span class="green">PASS</span>' if req else '<span class="red blinking">FAIL</span><b></b>'
#
#     status = [status(review.requirement_1), status(review.requirement_2), status(review.requirement_3),
#               status(review.requirement_4), status(review.requirement_5), status(review.requirement_6),
#               status(review.requirement_7), status(review.requirement_8), status(review.requirement_9),
#               status(review.requirement_10)]
#     labels = [r.strip() for r in review.requirement_labels.split('\n')]
#     return zip(labels, status)
#
#
# def render_review(review_id):
#     review = get_review(review_id)
#     return dict(title='Design Review',
#                 review=review,
#                 requirements=requirements_met(review),
#                 notes=render_notes(review))
#
#
# def render_review_list(text, reviews, **options):
#     data = dict(description=text, reviews=reviews)
#     data.update(options)
#     return render_to_string('_review_list.html', data)
#
#
# def render_reviews(student):
#     to_do_text = '''
#          The following reviews are scheduled to be completed by the due date. You will only
#          get credit if the review is done correctly and on time.
#          '''
#     done_text = '''
#          You have completed these reviews.  You can updated them at any time with new information
#          '''
#     feedback_text = '''
#          These reviews are for feedback on your design work.
#          '''
#     reviews_to_do = render_review_list(to_do_text, student_reviews_todo(student.pk), course=student.course.name, edit=True)
#     reviews_done = render_review_list(done_text, student_reviews_done(student.pk), course=student.course.name, edit=True, score=True)
#     feedback = render_review_list(feedback_text, review_feedback(student.pk), course=student.course.name, show=True, score=True)
#
#     todo_data = [0, 'Reviews To Do', reviews_to_do, 'active']
#     done_data = [1, 'Reviews Done', reviews_done, '']
#     feedback_data = [2, 'Design Feedback', feedback, '']
#
#     data = dict(student=student, reviews=[todo_data, done_data, feedback_data], course=student.course.name)
#     # return render_to_string('review_tasks.html', data)
#     return data


