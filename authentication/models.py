import logging

from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.text import slugify


logger = logging.getLogger('mailings')


class User(AbstractUser):

    RENTER = 'r'
    GOALIE = 'g'
    ROLES = [(RENTER, 'Renter'), (GOALIE, 'Goalie')]

    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    is_verified = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    role = models.CharField(max_length=1, choices=ROLES, default=GOALIE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


