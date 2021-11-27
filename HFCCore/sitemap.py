from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *
from blog.models import Post
from EventsEngine.models import *


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'about',
            'privacy',
            'community',
            'problem_statements',
            'projects',
            'terms_conditions',
            'contact',
            'donate',    
        ]
    def location(self, item):
        return reverse(item)
    
class ProblemStatementSitemap(Sitemap):
    def items(self):
        return Problem_Statement.objects.all()
    def location(self, item):
        return reverse('problem_discription', args=[item.title_slug])

class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()
    def location(self, item):
        return reverse('project_detail', args=[item.project_slug])

class IssueAreaSitemap(Sitemap):
    def items(self):
        return Issue_Area.objects.all()
    def location(self, item):
        return reverse('issue_area', args=[item.issue_area_slug])

class BlogSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
    def location(self, item):
        return reverse('blog-detail', args=[item.title_slug])

class EventSitemap(Sitemap):
    def items(self):
        return Events.objects.all()
    def location(self, item):
        return reverse('event_detail', args=[item.title_slug])

