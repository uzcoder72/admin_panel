from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django import forms

from core.models import Person, Course, Grade

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("last_name__startswith", )
    list_display = ("last_name", "first_name", "show_average")
    fields = ("first_name", "last_name", "courses")
    def show_average(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        return format_html("<b><i>{}</i></b>", result["grade__avg"])
    show_average.short_description = "Average Grade"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["first_name"].label = "First Name (Humans only!):"
        return form


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "view_students_link")
    list_filter = ("year", )

    def view_students_link(self, obj):
        count = obj.person_set.count()
        url = (
            reverse("admin:core_person_changelist")
            + "?"
            + urlencode({"courses__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, count)

    view_students_link.short_description = "Students"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass