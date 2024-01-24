from django.db import models


class NewsCategory(models.Model):
    """Категории статьи """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news_categories'


class NewsArticle(models.Model):
    """Статья"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news_articles'


class TickerMessage(models.Model):
    """Бегущая строка"""
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'news_ticker_messages'


class Comment(models.Model):
    """Коментарии статьи"""
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('NewsArticle', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.created_at}'

    def is_parent(self):
        return self.parent_comment is None

    class Meta:
        db_table = 'news_comments'


class Rating(models.Model):
    """Рейтинг статьи"""
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('NewsArticle', on_delete=models.CASCADE)

    class Meta:
        db_table = 'news_ratings'
