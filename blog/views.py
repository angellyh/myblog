#coding:utf-8

from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import time
import datetime
from django.db.models import Q
from django.db import connection
import Common
import os
import models
from forms import CommentForm
from markdown import markdown

#博客侧栏功能

def r_sidebar(request):

    categorys = models.Category.objects.order_by('-id')
    articles = models.Article.objects.all()

    #计算每种分类中的文章数量
    for category in categorys:
        category.article_num = 0
        for article in articles:
            if article.category == category:
                category.article_num += 1
        category.save()

    return categorys

#首页功能
def default(request):
 
    categorys = r_sidebar(request)
    articles = models.Article.objects.order_by('-hits')[0:6]
    return render_to_response('index.html',locals())
#博文目录
def article_list(request):
    categorys = r_sidebar(request)
    keywords = request.GET.get('keywords')
    category = request.GET.get('category')

    #根据搜索、分类和默认确定对应的文章
    if keywords:
        articles = models.Article.objects.order_by('-id').filter(Q(caption__icontains=keywords) | Q(content__icontains=keywords))
    elif category:
        articles = models.Article.objects.order_by('-id').filter(category__id=int(category))
    else :
        articles = models.Article.objects.order_by('-id')

    #分页    
    paginator = Paginator(articles, 20) #每页显示20篇文章

    #跳转到某页的文章
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    try:
        articlelist = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        articlelist = paginator.page(1)

    #如果页数太多，则将显示页数的范围定为当前页码的前后几页
    after_range_num = 5
    befor_range_num = 4

    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]


    return render_to_response('article_list.html', locals())

#文章内容
def article_detail(request):
    categorys = r_sidebar(request)

    #根据id获取文章
    articleid = int(request.GET.get('article'))
    article = models.Article.objects.get(id = articleid)

    #更新浏览次数
    article.hits +=1
    #显示文章评论
    commentlist = models.Comment.objects.filter(article_id = articleid)
    #读者对文章进行顶！d=====(￣▽￣*)b或者踩
    if request.POST.has_key('good'):
        article.goods += 1
    if request.POST.has_key('bad'):
        article.bads += 1

    #提交评论
    if request.POST.has_key('commentsubmit'):

        formInfo = CommentForm(request.POST)
        if formInfo.is_valid():
            submiterror = 0
            comment = formInfo.cleaned_data
            models.Comment.objects.create(name=comment['name'], content=comment['content'], article=article, email=comment['email'])
            article.times += 1
        else:
            submiterror = 1

    article.save()
    form = CommentForm()

    return render_to_response('article_detail.html', locals(), context_instance = RequestContext(request))
def about_me(request) :
    return render_to_response('aboutme.html', locals())