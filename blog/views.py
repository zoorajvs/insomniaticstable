from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )

from blog.models import Post


def BlogHome(request):
    context = {
        'posts': Post.objects.all(),
        # 'title' : 'Blog Home'
    }
    return render(request, 'blog/blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    extra_context = {'title': 'Blog Home'}
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    extra_context = {'title': 'User / User Blog'}
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    extra_context = {'title': 'Blog / view'}


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    extra_context = {'title': 'New Blog'}
    fields = ['post_title', 'content','content_1']

    def form_valid(self, form):
        form.instance.author = self.request.user  # for setting author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    model = Post
    extra_context = {'title': 'Blog / Update'}
    fields = ['post_title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # <<<for setting author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:  # <<<for finding that delelting person is author or not
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,  DeleteView):
    model = Post
    extra_context = {'title': 'Delete Blog'}
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
