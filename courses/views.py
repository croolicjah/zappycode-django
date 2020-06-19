from django.shortcuts import render, get_object_or_404

from .models import Lecture, Course


def view_lecture(request, course_slug, lecturepk, lecture_slug):
    lecture = get_object_or_404(Lecture, pk=lecturepk)
    return render(request, 'courses/view_lecture_4all.html', {'lecture': lecture})




def course_landing_page(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    return render(request, 'courses/course_landing_page.html', {'course': course})


def all_courses(request):
    courses = Course.objects.order_by('-release_date')
    return render(request, 'courses/all_courses.html', {'courses': courses})
