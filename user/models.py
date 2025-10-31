from django.db import models
# AbstractBaseUser(last_login , password , is_superuser) ( set_password() , check_password() )
from django.contrib.auth.models import AbstractBaseUser  , BaseUserManager  , PermissionsMixin
# Create your models here.
class CustomUserManager(BaseUserManager ):
    def create_user(self , email , name , password = None):
        if not email:
            raise ValueError ("email is required")
        #shimaa@gmail.com
        #shimaa@GMAIL.com
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password) #hashing password
        user.save(using = self._db)
        return user
    def create_superuser(self , email , name , password):
        user = self.create_user(email , name , password) # normaluser 
        user.is_staff = True
        user.is_superuser = True 
        user.save (using = self._db)
        return user


class CustomUser(AbstractBaseUser , PermissionsMixin  ):
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=100)
    is_staff = models.BooleanField (default=False)
    is_active  = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        return self.name
