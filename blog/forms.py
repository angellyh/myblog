#coding:utf-8
from django import forms

class CommentForm(forms.Form):
	"""评论表单"""
	name = forms.CharField(label=u"姓名")
	email = forms.EmailField(required=False, label=u"邮箱")
	content = forms.CharField(widget=forms.Textarea, label=u"内容")