from django.urls import path,include
from users import views

urlpatterns = [
    path('user/',views.UserDetailAPI.as_view(),name='user_detail'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('teacher/',views.TeacherList.as_view(),name='teachers_list'),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view(),name='teacher_detail'),
    path('student/',views.StudentList.as_view(),name='students_list'),
    path('student/<int:pk>/',views.StudentDetail.as_view(),name='student_detail'),
]
