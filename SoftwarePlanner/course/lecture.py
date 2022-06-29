from glob import glob
from os import rename
from os.path import isfile, join

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from course.models import Lesson, ZoomLecture


# def create_lectures():
#     lesson = 27
#     url = 'https://unco.zoom.us/rec/play/z16-YD5Q_kkC67DB2vJw5YeLQeYqdG2-qPs8b5IvSSVwdEkLdMJPbHZY7hY26hUYuy-AJAqXwIjk9ai4.CRDOXWWUf2sKpIYX'
#     create_lecture('bacs200', lesson, url)
#     url = 'https://unco.zoom.us/rec/play/CC20jF7OePxeVZQ8q6eAZbWkXRpaGFWuM_w7Gj-JrCthoLWfNRlofbhJWPI68n7dQN9_OzoqX1_ZZBSv.e6UOIbw6FB1QQc7_'
#     create_lecture('bacs350', lesson, url)
#     url = 'https://unco.zoom.us/rec/play/jyhNR906sfAjDIOZgs6s9-3WIWYy7k6W5acEyYU8BZKMJ3PYSToQdSqvGoctC4fGiaVEUz4r3sQgNGSn.zwNwNw6CnEejAxWS'
#     create_lecture('cs350', lesson, url)
#
from tool.text import text_join


def course_lectures(course):
    return ZoomLecture.objects.filter(lesson__course__name=course)


def create_lecture(course, lesson_num, url):
    lesson = Lesson.objects.get(course=course, lesson=lesson_num)
    # lecture = ZoomLecture.objects.filter(lesson=lesson)
    # if len(lecture)>1:
    #     lecture[0].delete()
    lecture = ZoomLecture.objects.get_or_create(lesson=lesson)[0]
    lecture.zoom_url = url
    lecture.save()


def list_lectures():
    for z in ZoomLecture.objects.all():
        print(f'{z.lesson.course.name} - {z.lesson.date} - Lesson {z.lesson.lesson} - {z.zoom_url}')


def lecture_videos(zoom):
    return filter(isfile, glob(f"{zoom}/*"))


def rename_videos(course, zoom):

    def rename_video(old, new):
        print(f'rename {old} {new}')
        rename(old, new)

    for lesson in Lesson.objects.filter(course__name=course).order_by('lesson'):
        d = str(lesson.date).replace('-','')
        found = f'{course} - {d} not found'
        for x in lecture_videos(zoom):
            if d in x:
                found = x
                rename_video(x, f'{zoom}/{lesson.date}.mp4')
                break
        if found.endswith('not found'):
            print(found)


def find_videos(course, zoom):
    for lesson in Lesson.objects.filter(course__name=course).order_by('lesson'):
        d = str(lesson.date).replace('-', '')
        found = f'{d} not found'
        for x in lecture_videos(zoom):
            if d in x:
                found = x
                break
        print(found)



class LectureListView(ListView):
    model = ZoomLecture
    template_name = 'list.html'


class LectureUpdateView(UpdateView):
    model = ZoomLecture
    template_name = 'edit.html'
    fields = '__all__'


class LectureCreateView(CreateView):
    model = ZoomLecture
    template_name = 'edit.html'
    fields = '__all__'


# from tool.files import read_file
# from tool.text import find_markdown_links
#
#
# def set_lectures(course):
#     text = read_file(f'Documents/course/{course}/docs/ZoomLectures.md')
#     links = find_markdown_links(text)
#     for i, x in enumerate(links[1:]):
#         create_lecture(course, i+1, x[1])
#
# def setup_lectures():
#     set_lectures('bacs200')
#     set_lectures('bacs350')
#     set_lectures('cs350')
#     list_lectures()
