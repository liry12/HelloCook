from django import template
from article.models import ArticlePost
from django.db.models import Count
from django.shortcuts import get_object_or_404

register = template.Library()


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()

@register.simple_tag
def article_total_views(article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    return article.users_view.count()


@register.inclusion_tag('article/list/most_liked_articles.html')
def most_liked_articles(n=5):
    most_liked_articles = ArticlePost.objects.order_by("-users_like")[:n]
    return {"most_liked_articles": most_liked_articles}


@register.inclusion_tag('article/list/most_viewed_articles.html')
def most_viewed_articles(n=5):
    most_viewed_articles = ArticlePost.objects.order_by("-users_view")[:n]
    return {"most_viewed_articles": most_viewed_articles}


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_articles": latest_articles}


# @register.inclusion_tag('article/list/most_commented_articles.html')
@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]