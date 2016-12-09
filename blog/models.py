# -*- coding: utf-8 -*- 
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.http import Http404
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class StatusManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(StatusManager, self).filter(draft=False).filter(posted__lte=timezone.now())


class Tag(models.Model):
    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'

    title = models.CharField(verbose_name=u"Название тега", max_length=200, unique=True)
    slug = models.SlugField(verbose_name=u"URL", max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь')
    description = models.CharField(verbose_name=u"Description", max_length=200, blank=True)
    keywords = models.CharField(verbose_name=u"Keywords", max_length=200, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag-detail', args=(self.slug,))


class Post(models.Model):
    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

    title_page = models.CharField(
        verbose_name=u"Заголовок страницы (Title)",
        max_length=200,
        blank=True,
    )
    title_post = models.CharField(
        verbose_name=u"Заголовок статьи (h1)",
        max_length=200,
        unique=True,
    )
    draft = models.BooleanField(verbose_name=u"Не публиковать", default=False)
    preview = RichTextUploadingField(verbose_name=u"Превью")
    text = RichTextUploadingField(verbose_name=u"Полная статья")
    posted = models.DateField(
        verbose_name=u"Дата публикации (пример: 01.01.2016)",
        auto_now=False,
        auto_now_add=False,
    )
    tags = models.ManyToManyField(Tag, verbose_name=u"Теги")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'Пользователь')
    description = models.CharField(verbose_name=u"Description", max_length=200, blank=True)
    keywords = models.CharField(verbose_name=u"Keywords", max_length=200, blank=True)

    objects = models.Manager()
    status = StatusManager()

    def __str__(self):
        return self.title_post
