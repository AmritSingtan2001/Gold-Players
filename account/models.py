from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


'''Custom User Manager'''
class UserManager(BaseUserManager):
    def create_user(self, email,  name=None, phone_no=None, password=None, password2=None,**extra_fields):
        
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_no= phone_no
        )

        user.set_password(password)
        user.is_user = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name=None, phone_no=None, password=None,**extra_fields):
        user = self.create_user(
            email,
            password=password,
            name=name,
            phone_no= phone_no
        )
        user.is_admin = True
        user.is_superuser =True
        user.save(using=self._db)
        return user

'''Custom User Model'''
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200,null=True, blank=True)
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=150,null=True, blank=True)
    avatar = models.ImageField(upload_to="avatarimage/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    @property
    def is_staff(self):
        return self.is_admin 
    