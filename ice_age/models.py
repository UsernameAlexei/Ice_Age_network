from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# подписки
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # один пользователь - один профиль
    #  один пользователь - несколько подписок
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,  # подписка без обратной подписки
        blank=True  # подписка не обязательна
    )

    def __str__(self):
        return self.user.username  # отражение имени


class Posts(models.Model):
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.DO_NOTHING
    )
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = (
        ('without_changes', ''),
        ('changes', 'edited'),
    )

    status = models.CharField(choices=STATUS_CHOICES, default='', max_length=15)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:20]}..."
        )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # создание профиля для каждого пользователя
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
