from ckeditor.fields import RichTextField
from django.db import models
from user.models import User


class BlogModel(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255)
    blog_subtitle = models.CharField(max_length=255, null=True, blank=True)
    blog_content = RichTextField()
    blog_image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    totalViewCount = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.blog_title + " by " + self.author.name

    @property
    def number_of_comments(self):
        return BlogCommentModel.objects.filter(blogpost_connected=self).count()


class BlogCommentModel(models.Model):
    blog_post = models.ForeignKey(BlogModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.name, self.blog_post.blog_title[:40])
