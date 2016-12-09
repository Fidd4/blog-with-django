# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic

from .forms import PostForm, TagForm
from .models import Post, Tag


def index(request):
    """ Список постов на главной. """
    today = timezone.now().date()
    posts = Post.status.active().order_by('-posted')

    if request.user.is_staff or request.user.is_superuser:
        posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        post_paginator = paginator.page(page)
    except PageNotAnInteger:
        post_paginator = paginator.page(1)
    except EmptyPage:
        post_paginator = paginator.page(paginator.num_pages)

    context = {
        'post_paginator': post_paginator,
        'today': today,
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, pk):
    """ Страница с детальной информацией о посте. """
    post = get_object_or_404(Post, pk=pk)
    if post.posted > timezone.now().date() or not post.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    return render(request, 'blog/post_detail.html', {'post': post})


class TagDetail(generic.DetailView):
    """
    Страница с детальной информацией о теге.
    Список тегов выполнен в виде шаблонного тега.
    """
    model = Tag
    template_name = 'blog/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        """ Получает посты определенного тега. """
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        context['posts'] = Post.status.active().filter(tags=self.object).order_by('-posted')
        if self.request.user.is_staff or self.request.user.is_superuser:
            context['posts'] = Post.objects.all().filter(tags=self.object).order_by('-posted')
        return context


@login_required
def add_tag(request):
    """ Обработка формы добавления тегов. """
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect('/')
    else:
        form = TagForm()
    return render(request, 'blog/add_tag.html', {'form': form})


@login_required
def add_post(request):
    """ Обработка формы добавления постов. """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class TagUpdate(generic.UpdateView):
    """ Редактирование тега. """
    model = Tag
    template_name = 'blog/tag_update.html'
    fields = ('title', 'slug', 'description', 'keywords')
    success_url = reverse_lazy(index)


@method_decorator(login_required, name='dispatch')
class PostUpdate(generic.UpdateView):
    """ Редактирование поста. """
    model = Post
    template_name = 'blog/post_update.html'
    fields = (
        'title_page',
        'title_post',
        'draft',
        'preview',
        'text',
        'posted',
        'tags',
        'description',
        'keywords',
    )
    success_url = reverse_lazy(index)


@method_decorator(login_required, name='dispatch')
class TagDelete(generic.DeleteView):
    """ Удаление тега. """
    model = Tag
    template_name = 'blog/tag_delete.html'
    success_url = reverse_lazy(index)


@method_decorator(login_required, name='dispatch')
class PostDelete(generic.DeleteView):
    """ Удаление поста. """
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy(index)
