"""
URL configuration for shikkhashala project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('notices/', views.notices, name='notices'),
    path('notices_detail/<int:id>/', views.notices_detail, name='notices_detail'),
    path('submit_number/', views.submit_number, name='submit_number'),
    path('gallery/', views.gallerys, name='gallery'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login, name='login'),
    path('logout/', views.admin_logout, name='logout'),
    path('profile_teacher/', views.profile_teacher, name='profile_teacher'),
    path('upload_topic/', views.upload_topic, name='upload_topic'),
    path('attandance_for/', views.attandance_for, name='attandance_for'),
    path('add_student_attandance/<courses>/', views.add_student_attandance, name='add_student_attandance'),
    path('profile_student/', views.profile_student, name='profile_student'),
    path('check_topic/', views.check_topic, name='check_topic'),
    path('topic_details/<int:id>/', views.topic_details, name='topic_details'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('enroll/<int:id>/', views.enroll, name='enroll'),
    path('download_routine/<int:id>/', views.download_routine, name='download_routine'),
    path('download_result/<courses>/', views.download_result, name='download_result'),
    path('download_reciept/', views.download_reciept, name='download_reciept'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
