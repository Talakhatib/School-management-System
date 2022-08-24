from django.urls import path,include
from courses import views

urlpatterns = [
    path('course/',views.CourseList.as_view(),name='courses_list'),
    path('course/<int:pk>/',views.CourseDetail.as_view(),name='course_detail'),
    path('teaches/',views.TeachesList.as_view(),name='teaches_list'),
    path('teaches/<int:pk>/',views.TeachesDetail.as_view(),name='teaches_detail'),
    path('enroll/',views.EnrollList.as_view(),name='enroll_list'),
    path('enroll/<int:pk>/',views.EnrollDetail.as_view(),name='enroll_detail'),
    path('doexam/',views.DoExamList.as_view(),name='doexam_list'),
    path('doexam/<int:pk>/',views.DoExamDetail.as_view(),name='doexam_detail'),
    path('results/',views.ResultList.as_view(),name='result_list'),
    path('results/<int:pk>/',views.ResultDetail.as_view(),name='result_detail'),
]

