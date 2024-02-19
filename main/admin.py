from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([courses, teachers, routine, results, students, contact, gallery, carousel, profile,give_number,class_topic,enroll,notices])

@admin.register(students_attandance)
class students_attandanceAdmin(admin.ModelAdmin):
    filter_horizontal = ('name',)

@admin.register(teachers_attandance)
class teachers_attandanceAdmin(admin.ModelAdmin):
    filter_horizontal = ('name',)

@admin.register(student_payment)
class student_paymentAdmin(admin.ModelAdmin):
    filter_horizontal = ('name',)