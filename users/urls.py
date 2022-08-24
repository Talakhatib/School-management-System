from django.urls import path,include
from users import views

urlpatterns = [
    
    path('user/<int:pk>',views.UserDetailAPI.as_view(),name='user_detail'),
    path('user_change_password/',views.ChangePasswordView.as_view(),name='change_password_user'),
    path('login/',views.LoginView.as_view(),name='token_obtain_pair'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('teacher/',views.TeacherList.as_view(),name='teachers_list'),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view(),name='teacher_detail'),
    path('student/',views.StudentList.as_view(),name='students_list'),
    path('student/<int:pk>/',views.StudentDetail.as_view(),name='student_detail'),
]
