from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class BaseModelManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(user=user)


class BaseModel(models.Model):
    objects = BaseModelManager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
