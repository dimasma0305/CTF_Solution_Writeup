from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    CustomLoginView,
    RegisterPage,
    TaskCreate,  # TaskDetail,
    TaskDelete,
    TaskList,
    TaskUpdate,
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", TaskList.as_view(), name="task_list"),
    # path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path("task-create/", TaskCreate.as_view(), name="task_create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task_update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task_delete"),
]
