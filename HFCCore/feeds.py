"""from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.template.defaultfilters import truncatewords_html
from django.apps import apps
#Entry = apps.get_model('andablog', 'Entry')

from django.urls import reverse_lazy

class LatestEntriesFeed(Feed):
    
    MAX_ENTRIES = 10

    title = 'Latest blog entries'
    description = 'Latest blog entries sorted by newest to oldest.'

    def item_pubdate(self, item):
        return item.published_timestamp

    def link(self):
        return reverse('andablog:entrylist')

    def item_description(self, item):
        # TODO: "Better support for truncating markup" #2
        return truncatewords_html(item.content, 26)

    def item_title(self, item):
        return item.title

    def items(self):
        return Entry.objects.filter(is_published=True).order_by('-published_timestamp')[:self.MAX_ENTRIES]

class LatestBlogEntries(LatestEntriesFeed):
    feed_copyright = 'HackForChange'
    title = 'Latest Blog Entries'
    description = 'Updates on the latest blog entries from hackforchange.co.in'
    link = reverse_lazy('andablog:entrylist')"""
