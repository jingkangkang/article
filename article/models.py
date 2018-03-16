#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻标题'
        verbose_name_plural = '新闻标题'


class Item(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    create_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False, verbose_name='是否完成')
    article_category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻子栏目'
        verbose_name_plural = '新闻子栏目'


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签')
    slug = models.SlugField(max_length=50, verbose_name='描述')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    slug = models.SlugField(unique_for_year='publish_date', verbose_name='描述')
