from chameleon import PageTemplate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect
from django.template import engines
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .models import Task


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task_list")


class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "task_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list"] = context["task_list"].filter(user=self.request.user)
        context["count"] = context["task_list"].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["task_list"] = context["task_list"].filter(
                title__icontains=search_input
            )

        context["search_input"] = search_input

        return context


# class TaskDetail(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = "task_detail"

# def get_queryset(self):
#     queryset = Task.objects.filter(user=self.request.user, pk=self.pk)

#     return queryset

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     print(self.get_object())

#     if self.get_object().user != self.request.user:
#         context["task_detail"] = "you dont have permission to view this"
#         return context

#     return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        template = PageTemplate(form.instance.description).render()
        form.instance.user = self.request.user
        form.instance.description = "TODO AGAIN"
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user, id=self.kwargs["pk"])

        return queryset


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task_delete"
    success_url = reverse_lazy("task_list")
