from django.shortcuts import render, get_object_or_404
from django.views import View

from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration
)

class InstructorList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )

class InstructorDetail(View):
    def get(self, request, pk):
        instructor = get_object_or_404(
            Instructor,
            pk=pk
        )
        section_list = instructor.sections.all()
        return render(
            request,
            'courseinfo/instructor_detail.html',
            {'instructor': instructor, 'section_list': section_list}
        )

class SectionList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list': Section.objects.all()}
        )


class SectionDetail(View):

    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        return render(
            request,
            'courseinfo/section_detail.html',
            {'section': section,
             'semester' : semester,
             'course': course,
             'instructor': instructor,
             'registration_list': registration_list}
        )


class CourseList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list': Course.objects.all()}
        )

class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk
        )
        id = course.course_id
        number = course.course_number
        name = course.course_name
        course_list = Course.objects.all()
        return render(
            request,
            'courseinfo/course_list_detail.html',
           {'id': id,
            'course': course,
            'number': number,
            'name': name,
            'course_list': course_list}
        )

class SemesterList(View):
        def get(self, request):
            return render(
                request,
                'courseinfo/semester_list.html',
                {'semester_list': Semester.objects.all()}
            )


class SemesterDetail(View):
    def get(self, request, pk):
        semester = get_object_or_404(
            Semester,
            pk=pk
        )
        section_list = semester.sections.all()
        return render(
            request,
            'courseinfo/semester_detail.html',
            {'semester': semester, 'section_list': section_list}
        )



class StudentList(View):
        def get(self, request):
            return render(
                request,
                'courseinfo/student_list.html',
                {'student_list': Student.objects.all()}
            )


class StudentDetail(View):
    def get(self, request, pk):
        student = get_object_or_404(
            Student,
            pk=pk
        )
        id = student.student_id
        student_list = Student.objects.all()
        return render(
            request,
            'courseinfo/student_detail.html',
            {'student': student, 'id': id, 'student_list': student_list}
        )
#

# class StudentDetail(View):
#     def get(self, request, pk):
#         student = get_object_or_404(
#             Student,
#             pk=pk
#         )
#         firstname = student.first_name
#         lastname = student.last_name
#         student_list = Student.objects.all()
#         return render(
#             request,
#             'courseinfo/student_detail.html',
#             {'student': student,
#              'firstname': firstname,
#              'lastname': lastname,
#              'student_list': student_list}
#         )


class RegistrationList(View):
    def get(self, request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )

class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        number = registration.registration_id
        section = registration.section_id
        student = registration.student_id
        registration_list = Registration.objects.all()
        return render(
            request,
            'courseinfo/registration_detail.html',
           {'registration': registration,
            'number': number,
            'section': section,
            'student': student,
            'registration_list': registration_list}
        )



# class CourseDetail(View):
#     def get(self, request, pk):
