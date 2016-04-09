#coding:utf-8
from django.contrib import admin
from blog.models import *
from pagedown.widgets import AdminPagedownWidget
from django import forms
class CategoryAdmin(admin.ModelAdmin):
	#展示文章分类列表
	list_display = ('name', 'article_num')

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'	

class ArticleAdmin(admin.ModelAdmin):
	#展示文章属性
	list_display = ('caption', 'category' , 'createtime','updatetime', 'hits', 'times', 'goods', 'bads')
	search_fields=('caption', 'createtime') #搜索框：标题，创建时间
	list_filter = ('createtime',) #过滤器：创建时间
	date_hierarchy='createtime' #导航条过滤器：创建时间
	ordering=('-updatetime',)
	fields = ('caption', 'category', 'shortcontent', 'content', 'createtime',)
	raw_id_fields=('category',)
	form = ArticleForm

class CommentAdmin(admin.ModelAdmin):
	#展示评论
	list_display = ('article', 'content', 'createtime', 'name', 'email')


#注册功能和数据表
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
