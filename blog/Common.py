#coding:utf-8
import models
#文章分类按照名字来排列
def cate():
	categories = models.Category.objects.order_by('name').all()
#文章标题按照id和标题来排列，每次显示20个
def caption():
	caption = models.Article.objects.order_by('-id').values('id', 'caption')[:20]
	return caption