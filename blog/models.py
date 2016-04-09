#coding:utf-8
from __future__ import unicode_literals
import time
from django.db import models
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse

class Category(models.Model):
	"""文章分类"""
	name = models.CharField(max_length=100)
	article_num = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' % self.name

class Article(models.Model):
	"""文章属性"""
	category = models.ForeignKey(Category, verbose_name=u'分类')
	caption = models.CharField('标题', max_length=200)
	shortcontent = models.TextField('文章摘要', max_length=500)
	content = models.TextField('正文', null=True)
	createtime = models.DateTimeField('创建时间', auto_now_add=False, blank=True)
	updatetime = models.DateTimeField('更新时间', auto_now=True, editable=True,null=True)
	hits = models.IntegerField('点击数', default=0)
	times = models.IntegerField('阅读数', default=0)
	goods = models.IntegerField('顶', default=0) #顶！d=====(￣▽￣*)b
	bads = models.IntegerField('踩', default=0) #踩！
	def __unicode__(self):
		return u'%s' % self.caption

class Comment(models.Model):
			"""评论属性"""
			name = models.CharField(max_length=50)
			email = models.EmailField()
			content = models.TextField()
			createtime = models.DateTimeField(auto_now_add=True, blank=True)
			article = models.ForeignKey(Article)

			def __unicode__(self):
				return u'%s' % self.article



