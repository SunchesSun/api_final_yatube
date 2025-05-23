from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

from .constans import TITLE_GROUP, POST_TEXT

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=TITLE_GROUP)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text[:POST_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]

    def save(self, *args, **kwargs):
        if self.user == self.following:
            raise ValidationError('Нельзя подписаться на самого себя.')
        super().save(*args, **kwargs)
