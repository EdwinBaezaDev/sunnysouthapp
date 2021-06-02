
#Django
from django.db import models

#utils
from sunnysouth.utils.models import BaseModel

class Profile(BaseModel):
    """Profile Model."""

    user = models.OneToOneField('marketplace.User', related_name='profile', on_delete=models.CASCADE)
    slug_name = models.CharField(max_length=300, null=True)
    biography = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField('active', default=True)
    reputation = models.FloatField(default=5.0)
