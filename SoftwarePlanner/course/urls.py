from django.urls import path

from views.views import WorkshopView
from .views_review import ReviewDetail, ReviewEdit, ReviewList
from .views_team import TeamUpdateView, TeamView, TeamsView
from .views import CourseIndexView, CourseView, CourseDocsView, CoursePagesView, SlidesView, StudentUpdate
from book.views import BookChapterView, BookView
from .views_auth import student_login, student_logout, student_register
from .views_game import UncUrlGameAnswer, UncUrlGameDone, UncUrlGameQuestion
# from .views_review import ReviewEdit, ReviewFeedback, Reviews
from .views_teamwork import TeamworkEdit, TeamworkSummary

from .lecture import LectureListView, LectureCreateView, LectureUpdateView

# URL Routes
urlpatterns = [

    # User Auth
    path('course/<str:course>/register', student_register),
    path('course/<str:course>/login', student_login),
    path('course/<str:course>/logout', student_logout),

    # Student
    path('student/<str:course>/<int:pk>', StudentUpdate.as_view(), name='student-edit'),

    # # Book
    # path('book', BookView.as_view()),
    # path('book/<str:book>', BookView.as_view()),
    # path('book/<str:book>/<str:chapter>', BookChapterView.as_view()),

    # URL Game
    path('course/<str:course>/url-question', UncUrlGameQuestion.as_view()),
    path('course/<str:course>/url-answer', UncUrlGameAnswer.as_view()),
    path('course/<str:course>/url-game-done', UncUrlGameDone.as_view()),

    # Team
    path('course/cs350/team/', TeamsView.as_view(), name='team'),
    path('course/cs350/team/<int:pk>', TeamView.as_view(), name='team_detail'),
    path('course/cs350/engineer/<int:pk>/', TeamUpdateView.as_view(), name='engineer_edit'),

    # # Teamwork
    # path('course/<str:course>/teamwork/', TeamworkSummary.as_view()),
    # path('course/<str:course>/teamwork/<int:pk>', TeamworkEdit.as_view()),
    # # path('course/<str:course>/teamwork-milestone/<int:milestone>', TeamworkSurvey.as_view()),

    # Review
    path('course/<str:course>/review/<int:pk>/', ReviewEdit.as_view()),
    path('course/<str:course>/review/<int:pk>',  ReviewDetail.as_view()),
    # path('course/<str:course>/review/<int:pk>', ReviewEdit.as_view()),
    path('course/<str:course>/reviews', ReviewList.as_view()),
    # path('course/<str:course>/feedback/<int:pk>', ReviewFeedback.as_view()),

    # Course
    path('course',                                          CourseIndexView.as_view()),
    path('course/<str:course>',                             CourseView.as_view()),
    path('course/<str:course>/slides/<int:lesson>',         SlidesView.as_view()),
    path('course/<str:course>/docs/<str:doc>',              CourseDocsView.as_view()),
    path('course/<str:course>/<str:doctype>/<int:lesson>',  CoursePagesView.as_view()),
    path('course/<str:course>/<str:doctype>/<str:doc>',     CourseView.as_view()),

    # Lecture
    path('lecture/<int:pk>',    LectureUpdateView.as_view(),   name='lecture_edit'),
    path('lecture/',            LectureListView.as_view(),     name='lecture_list'),

    # path('lecture/add', LectureCreateView.as_view(), name='lecture_add'),
    # path('course/<str:course>/<int:lesson>', SlidesView.as_view()),

    # path('course/<str:course>/<str:doc>',       CourseView.as_view(), name='doc'),
    # path('course/<str:course>',                 LessonMatrixView.as_view()),
    # path('course/<str:course>/outline',         CourseOutlineView.as_view()),
    # url(r'^course/(?P<course>[\w\-.]*)/plan/(?P<role>[\w/\-.]*)$', RoleView.as_view()),

    # Software Plan
    # path('swplan',                              SoftwarePlanView.as_view(), dict(project='', doc='Index')),
    # path('swplan/<str:project>',                SoftwarePlanView.as_view(), dict(doc='Index')),
    # path('swplan/<str:project>/<str:doc>',      SoftwarePlanView.as_view()),
    # path('swplan/<str:project>/<str:dir>/<str:doc>', SoftwarePlanView.as_view()),


    # Workshop
    path('workshop', WorkshopView.as_view()),
]
