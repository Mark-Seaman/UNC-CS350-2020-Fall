from django.contrib import admin


from .models import Course, Lesson, AppTeam, Checklist, Review, Teamwork, TeamMember, UncStudent, UrlGame

admin.site.register(AppTeam)
admin.site.register(Course)
admin.site.register(Checklist)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(TeamMember)
admin.site.register(Teamwork)
admin.site.register(UncStudent)
admin.site.register(UrlGame)

