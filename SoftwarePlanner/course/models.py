from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField(default='No Description is Set')
    num_projects = models.IntegerField(default=14)
    num_lessons = models.IntegerField(default=42)

    def __str__(self):
        return '%4d %-10s %-44s' % (self.pk, self.name, self.title)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    lesson = models.IntegerField()
    topic = models.CharField(max_length=100)
    project = models.IntegerField(null=True)
    reading = models.CharField(null=True, max_length=200)
    zybooks = models.CharField(null=True, max_length=200)
    type = models.CharField(null=True, max_length=100)

    def __str__(self):
        return '%4d %-10s %-10s %4d. %s' % (self.pk, self.course.name, self.date, self.lesson, self.topic)

    @property
    def url(self):
        return f'/course/{self.course.name}/lesson/{self.lesson:02}'


class Project(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    project = models.IntegerField()
    type = models.CharField(null=True, max_length=100)

    def __str__(self):
        return '%4d %-10s %-10s %4d. %s' % (self.pk, self.course.name, self.date, self.project, self.title)

    @property
    def url(self):
        return f'/course/{self.course.name}/project/{self.project:02}'


class UncStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    server = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    zbooks = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '%d. %-40s %-40s %s' % (self.pk, self.email, self.name, self.server)

    @staticmethod
    def students(course):
        return UncStudent.objects.filter(course__name=course)

    @property
    def github_user(self):
        return self.github.replace('https://github.com/', '')

    @property
    def github_pages(self):
        u = self.github_user
        return f'https://github.com/{u}/{u}.github.io'

    @property
    def github_server(self):
        u = self.github_user
        return f'https://{u}.github.io'


class AppTeam(models.Model):
    name = models.CharField(max_length=20)
    server = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(AppTeam, on_delete=models.CASCADE)
    student = models.ForeignKey(UncStudent, on_delete=models.CASCADE)
    member_id = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.team.name} - member {self.member_id}. - {self.student.name}'


class UrlGame(models.Model):
    student = models.ForeignKey(UncStudent, on_delete=models.CASCADE)
    answered = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    left = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.student.name} - answered {self.answered}, correct {self.correct}, left {self.left}'


class Review(models.Model):
    reviewer = models.ForeignKey(UncStudent, on_delete=models.CASCADE, editable=False)
    designer = models.ForeignKey(UncStudent, on_delete=models.CASCADE, related_name='designer', default=1, editable=False)
    page = models.CharField(max_length=100, null=True, editable=False)
    score = models.IntegerField(default=-1, editable=False)
    date = models.DateField(null=True, editable=False)
    notes = models.TextField(null=True)   # validators=[MinLengthValidator(10)]
    # requirement_labels = models.TextField(default='NONE')
    requirement_1 = models.BooleanField(default=False)
    requirement_2 = models.BooleanField(default=False)
    requirement_3 = models.BooleanField(default=False)
    requirement_4 = models.BooleanField(default=False)
    requirement_5 = models.BooleanField(default=False)
    requirement_6 = models.BooleanField(default=False)
    requirement_7 = models.BooleanField(default=False)
    requirement_8 = models.BooleanField(default=False)
    requirement_9 = models.BooleanField(default=False)
    requirement_10 = models.BooleanField(default=False)
    label_1 = models.CharField(max_length=100, null=True, editable=False)
    label_2 = models.CharField(max_length=100, null=True, editable=False)
    label_3 = models.CharField(max_length=100, null=True, editable=False)
    label_4 = models.CharField(max_length=100, null=True, editable=False)
    label_5 = models.CharField(max_length=100, null=True, editable=False)
    label_6 = models.CharField(max_length=100, null=True, editable=False)
    label_7 = models.CharField(max_length=100, null=True, editable=False)
    label_8 = models.CharField(max_length=100, null=True, editable=False)
    label_9 = models.CharField(max_length=100, null=True, editable=False)
    label_10 = models.CharField(max_length=100, null=True, editable=False)

    def __str__(self):
        return f'Review {self.pk}.  reviewer {self.reviewer.pk} - designer {self.designer.pk} - score{self.score}'


class Checklist(models.Model):
    team = models.ForeignKey(AppTeam, on_delete=models.CASCADE)
    milestone = models.IntegerField()
    date = models.DateField(null=True, editable=False)
    requirement_1 = models.BooleanField(default=False)
    requirement_2 = models.BooleanField(default=False)
    requirement_3 = models.BooleanField(default=False)
    requirement_4 = models.BooleanField(default=False)
    requirement_5 = models.BooleanField(default=False)
    requirement_6 = models.BooleanField(default=False)
    requirement_7 = models.BooleanField(default=False)
    requirement_8 = models.BooleanField(default=False)
    requirement_9 = models.BooleanField(default=False)
    requirement_10 = models.BooleanField(default=False)
    requirement_11 = models.BooleanField(default=False)
    requirement_12 = models.BooleanField(default=False)
    requirement_13 = models.BooleanField(default=False)
    requirement_14 = models.BooleanField(default=False)
    requirement_15 = models.BooleanField(default=False)
    requirement_16 = models.BooleanField(default=False)
    notes_1 = models.TextField(null=True, blank=True)
    notes_2 = models.TextField(null=True, blank=True)
    notes_3 = models.TextField(null=True, blank=True)
    notes_4 = models.TextField(null=True, blank=True)
    notes_5 = models.TextField(null=True, blank=True)
    notes_6 = models.TextField(null=True, blank=True)
    notes_7 = models.TextField(null=True, blank=True)
    notes_8 = models.TextField(null=True, blank=True)
    notes_9 = models.TextField(null=True, blank=True)
    notes_10 = models.TextField(null=True, blank=True)
    notes_11 = models.TextField(null=True, blank=True)
    notes_12 = models.TextField(null=True, blank=True)
    notes_13 = models.TextField(null=True, blank=True)
    notes_14 = models.TextField(null=True, blank=True)
    notes_15 = models.TextField(null=True, blank=True)
    notes_16 = models.TextField(null=True, blank=True)
    label_1 = models.CharField(max_length=100, null=True)
    label_2 = models.CharField(max_length=100, null=True)
    label_3 = models.CharField(max_length=100, null=True)
    label_4 = models.CharField(max_length=100, null=True)
    label_5 = models.CharField(max_length=100, null=True)
    label_6 = models.CharField(max_length=100, null=True)
    label_7 = models.CharField(max_length=100, null=True)
    label_8 = models.CharField(max_length=100, null=True)
    label_9 = models.CharField(max_length=100, null=True)
    label_10 = models.CharField(max_length=100, null=True)
    label_11 = models.CharField(max_length=100, null=True)
    label_12 = models.CharField(max_length=100, null=True)
    label_13 = models.CharField(max_length=100, null=True)
    label_14 = models.CharField(max_length=100, null=True)
    label_15 = models.CharField(max_length=100, null=True)
    label_16 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'Milestone {self.milestone}, Team: {self.team.name},  {self.date}'

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.team.id)])


# class ProjectMilestone(models.Model):
#     team = models.ForeignKey(AppTeam, on_delete=models.CASCADE)
#     milestone = models.IntegerField()
#
#     def __str__(self):
#         return f'Milestone #{self.milestone}, id: {self.pk}, team: {self.team.name}'


class Teamwork(models.Model):
    student = models.ForeignKey(UncStudent, on_delete=models.CASCADE, editable=False)
    teammate = models.ForeignKey(UncStudent, related_name='teammate', on_delete=models.CASCADE, editable=False)
    milestone = models.IntegerField(editable=False)
    question_1 = models.BooleanField(default=False)
    question_2 = models.BooleanField(default=False)
    question_3 = models.BooleanField(default=False)
    notes = models.TextField(null=True)

    def __str__(self):
        return f'Teamwork {self.pk}.  student {self.student.name} - teammate {self.teammate.name}'


class ZoomLecture(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=1)
    zoom_url = models.URLField()

    def __str__(self):
        return f'Lecture {self.lesson.lesson}. {self.lesson.date}'

    def get_absolute_url(self):
        return reverse('lecture_edit', args=[str(self.id)])

