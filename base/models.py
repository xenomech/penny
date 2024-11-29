from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class BaseModelManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)

class BaseModel(models.Model):
    objects = BaseModelManager()
    for_user = BaseModelManager().for_user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
