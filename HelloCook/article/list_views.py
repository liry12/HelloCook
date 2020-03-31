from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ArticlePost
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from .forms import CommentForm



def article_titles(request, username=None):
    if username:
        user = User.objects.get(username=username)
        articles_title = ArticlePost.objects.filter(author=user)
        try:
            userinfo = user.userinfo
        except:
            userinfo = None
    else:
        articles_title = ArticlePost.objects.all()

    paginator = Paginator(articles_title, 5)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    if username:
        return render(request, "article/list/author_articles.html",
                      {"articles": articles, "page": current_page, "userinfo": userinfo, "user": user})
    return render(request, "article/list/article_titles.html", {"articles": articles, "page": current_page})

# @login_required(login_url='/account/login')
# def article_detail(request, id, slug):
#     article = get_object_or_404(ArticlePost, id=id, slug=slug)
#     return render(request, "article/list/article_content.html", {"article": article})


@login_required(login_url='/account/login')
def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "article/list/article_content.html",
                  {"article": article, "comment_form": comment_form})


@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def like_article(request):
    article_id = request.POST.get("id")
    action = request.POST.get("action")
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action == "like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")


@csrf_exempt
@require_POST
@login_required(login_url='/account/login/')
def view_article(request):
    article_id = request.POST.get("id")
    article = ArticlePost.objects.get(id=article_id)
    article.users_view.add(request.user)
    return HttpResponse("1")

