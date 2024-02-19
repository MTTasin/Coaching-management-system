from django.shortcuts import render, redirect, get_object_or_404
from .models import contact as c, courses as co, teachers, teachers_attandance, routine, results, students as s, students_attandance as sta, contact, gallery, carousel, profile, student_payment, give_number, class_topic, enroll as e, notices as n
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as loginr, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
import datetime
from django.http import FileResponse
from django.http import HttpResponseNotFound, HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import io



# Create your views here.

def index (request):
    carousels = carousel.objects.all()
    course = co.objects.all()
    galleries = gallery.objects.all()
    teacher = teachers.objects.all()
    notices = n.objects.all().order_by('-id')
    context= {
        'carousels': carousels,
        'course': course,
        'galleries': galleries[:10],
        'teacher': teacher,
        'notices': notices[:3],
        
    }
    return render(request, 'index.html', context)

def notices(request):
    notices = n.objects.all()
    context = {'notices': notices}
    return render(request, 'notices.html', context)

def notices_detail(request, id):
    notice = n.objects.get(id=id)
    context = {'notice': notice}
    return render(request, 'notices_detail.html', context)

def submit_number(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        date_time = datetime.datetime.now()
        user = give_number(number=number, date_time=date_time)
        user.save()
        return render(request, 'contact_success.html')

def teachers_panel (request):
    teacher = teachers.objects.all()
    context = {'teacher': teacher}
    return render(request, 'teachers_panel.html', context)

def gallerys (request):
    galleries = gallery.objects.all()
    context = {'gallery': galleries}
    return render(request, 'gallery.html', context)

def profile_student(request):
    student = s.objects.get(user__name__username=request.user)  # Retrieve the student record for the logged-in user
    attandance = sta.objects.filter(name = student)
    context = {
        'student': student,
        'attandance': attandance,
        'attandance_count': attandance.count(),
        'attandance_new_ten': attandance.order_by('-date')[:30],
        # Add other context variables as needed (e.g., courses, assignments, etc.)
    }
    return render(request, 'profile_student.html', context)

@login_required
def check_topic(request):
    user = request.user.profile  # Assuming access to the logged-in user
    student = s.objects.get(user=user)  # Fetch student model linked to user
    enrolled_courses = student.courses.all()  # Get user's enrolled courses

    if enrolled_courses:
        topics = class_topic.objects.filter(courses__in=enrolled_courses).order_by('-id').all()
    else:
        # Handle cases where user has no enrolled courses
        topics = class_topic.objects.none()  # Return an empty queryset

    context = {
        'topics': topics
    }
    return render(request, 'check_topic.html', context)


@login_required
def topic_details(request, id):
    topic = class_topic.objects.get(id=id)
    context = {
        'topic': topic
    }
    return render(request, 'topic_details.html', context)

@user_passes_test(lambda u: u.is_staff)
def profile_teacher(request):
    teacher = teachers.objects.get(user__name__username=request.user)
    attandance = teachers_attandance.objects.filter(name=teacher)  # Retrieve the teacher record for the logged-in user
    context = {
        'teacher': teacher,
        'attandance': attandance,
        'attandance_count': attandance.count(),
        'attandance_new_ten': attandance.order_by('-date')[:30],
        # Add other context variables as needed (e.g., students, classes, etc.)
    }
    return render(request, 'profile_teacher.html', context)

@user_passes_test(lambda u: u.is_staff)
def upload_topic(request):
    if request.method == 'POST':
        form = topicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_topic_success.html')
    else:
        form = topicForm()
    return render(request, 'upload_topic.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def attandance_for(request):
    students_class = co.objects.all()
    context = {
        'students_class': students_class
    }
    return render(request, 'attandance_for.html', context)

@user_passes_test(lambda u: u.is_staff)
def add_student_attandance(request, courses):
    students = s.objects.filter(courses=courses)
    context = {
        'students': students,
        'count': students.count()
    }
    if request.method == 'POST':
        name_ids = request.POST.getlist('name')  # Assuming name is a multiple select field
        date = request.POST.get('date')
        att = sta(date=date)
        att.save()
        selected_students = s.objects.filter(pk__in=name_ids)  # Retrieve the student objects from the IDs
        att.name.set(selected_students)  # Use the set() method to assign the ManyToMany field
        return render(request, 'add_student_attandance_success.html')
    return render(request, 'student_attandance.html', context)



def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            if user.is_staff:
                loginr(request, user)
                return redirect('profile_teacher')
            else:
                loginr(request, user)
                return redirect('profile_student')
        else:
            messages.error(request, 'Invalid Username or password')
            return render(request,"login.html")
    elif request.method == 'GET':
        return render(request,"login.html")

@login_required
def admin_logout(request):
    logout(request)
    return redirect('login')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = c(name=name, email=email, message=message, subject=subject)
        if contact:
            contact.save()
            return render(request, 'contact_success.html')
    return render(request, 'contact_us.html')

def contact_success(request):
    return render(request, 'contact_success.html')


def enroll(request, id):
    course = co.objects.get(id=id)
    routine = course.routine_set.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gurdian_name = request.POST.get('gurdian_name')
        gurdian_phone = request.POST.get('gurdian_phone')
        gurdian_relation = request.POST.get('gurdian_relation')
        courses = course.title
        student = e(name=name, email=email, phone=phone, address=address, gurdian_name=gurdian_name, gurdian_phone=gurdian_phone, gurdian_relation=gurdian_relation, courses=courses)
        student.save()
        return render(request, 'enroll_success.html')
    context = {'course': course, 'routine': routine} if routine else {'course': course}
    return render(request, 'enroll.html', context)



# def fot downloading a PDF file that is uploaded to routine model
def download_routine(request, id):
    course = get_object_or_404(co, id=id)
    routine = course.routine_set.latest('id')  # Get the latest routine for the course
    response = HttpResponse(routine.routine_pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="routine.pdf"'
    return response

def download_result(request, courses):
    result = results.objects.filter(courses=courses).order_by('-id').first()
    result_name = result.name
    response = HttpResponse(result.result, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'
    return response


# def for downloading a PDF file from a template hello.html
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def download_reciept(request):
    payment = student_payment.objects.filter(name__user__name__username=request.user).order_by('id')
    total = 0
    for i in payment:
        total += i.paid_amount
    context = {
        'payment': payment,
        'total': total
    }
    pdf = render_to_pdf('reciept.html', context)
    return HttpResponse(pdf, content_type='application/pdf')