from django.urls import path
from . import views

urlpatterns = [
    path('courses_list/', views.CoursesListView.as_view(), name='course_list'),
    
    path('home/', views.HomeView.as_view(), name='home'),

    path('instructor/', views.InstructorCoursesView.as_view(), name='instructor_courses'),

    path('create-course/', views.CourseCreateView.as_view(), name='course-create'),

    path('instructor-course-details/<str:uuid>/', views.InstructorCoursesDetailView.as_view(), name='instructor-courses-details'),

    path('instructor-course-delete/<str:uuid>/', views.InstructorCourseDeleteView.as_view(), name='instructor-courses-delete'),

    path('instructor-course-update/<str:uuid>/', views.InstructorCoursesUpdateView.as_view(), name='instructor-courses-update'),




]