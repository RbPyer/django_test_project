import django.http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm, RegisterForm


# Create your views here.
class PostView(View):
    """
    Render posts
    """
    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        posts = Post.objects.all()
        return render(request, "blog/blog.html", {"post_list": posts})


class PostDetails(View):
    """
    post's page
    """
    def get(self, request: django.http.HttpRequest, page_id: int):
        post = Post.objects.get(id=page_id)
        return render(request, "blog/blog_details.html", {"post": post})


class AddComments(View):
    """
    add comments
    """
    def post(self, request: django.http.HttpRequest, post_id: int):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = post_id
            form.save()
        return redirect(f'/{post_id}')


@login_required
def profile_view(request):
    return render(request, "blog/profile.html")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("blog:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


