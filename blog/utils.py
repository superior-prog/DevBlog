from django.contrib.auth.models import AnonymousUser

from .models import *


def increaseViewCount(user, blog_post):
    if blog_post.totalViewCount is None:
        blog_post.totalViewCount = 0
    blog_post.totalViewCount = blog_post.totalViewCount + 1
    blog_post.save()

    BlogViewModel.objects.create(
        viewer=user,
        viewed=blog_post,
    )
    return


def add_to_blog_keyword(user, keyword):
    if keyword is not None:
        if user.is_authenticated:
            BlogSearchKeywordModel.objects.create(
                searched_by=user,
                searched_for=keyword,
            )
    return


def add_to_keyword_model(keyword):
    if keyword is not None:
        try:
            obj = KeywordModel.objects.get(keyword=keyword)
        except:
            obj = None

        if obj is not None:
            obj.total_count = obj.total_count + 1
            obj.save()
        else:
            KeywordModel.objects.create(
                keyword=keyword,
                total_count=1
            )
    return
