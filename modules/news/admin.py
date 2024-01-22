from django.contrib import admin

from modules.news.models import *

admin.site.register(NewsCategory)
admin.site.register(NewsArticle)
admin.site.register(TickerMessage)
admin.site.register(Comment)
admin.site.register(Rating)
