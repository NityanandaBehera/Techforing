
from django.urls import path
from .views import (
    RegisterUser,
    LoginUser,
    UserDetail,
    ProjectList,
    ProjectDetail,
    TaskList,
    TaskDetail,
    CommentList,
    CommentDetail
)

urlpatterns = [
    # User Endpoints
    path('users/register/', RegisterUser.as_view(), name='register_user'),
    path('users/login/', LoginUser.as_view(), name='login_user'),
    path('users/<int:id>/', UserDetail.as_view(), name='user_detail'),

    # Project Endpoints
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/<int:id>/', ProjectDetail.as_view(), name='project_detail'),

    # Task Endpoints
    path('projects/<int:project_id>/tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:id>/', TaskDetail.as_view(), name='task_detail'),

    # Comment Endpoints
    path('tasks/<int:task_id>/comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:id>/', CommentDetail.as_view(), name='comment_detail'),
]
