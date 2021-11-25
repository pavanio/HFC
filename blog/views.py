from django.shortcuts import render
from .models import *
from django.contrib.syndication.views import Feed
from django.views import generic


class PostList(generic.ListView):
    template_name = 'blog/blog_list.html'
    queryset = Post.objects.filter(status = 'Published')
    paginate_by = 6
    context_object_name = 'blogs'

class PostDetail(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    model = Post
    context_object_name = 'blog'
    slug_field = 'title_slug'
    slug_url_kwarg = 'title_slug'

class BlogFeed(Feed):
    title = "HackForChange News"
    link = "/blog/latest/feed/"
    description = "Updates on the HFC Blog"

    def items(self):
        return Post.objects.filter(status = 'Published').order_by('-created_on')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
    def item_pubdate(self, item):
        return datetime.datetime.combine(item.created_on, datetime.time(10, 23))
