from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# 2 seperate definition here

class PostListView(TemplateView):
    template_name = "blog/post_list.html"

# def post_list(request):
   # return render(request, 'blog/post_list.html', {})
