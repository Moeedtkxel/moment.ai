from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        """ Create and return a `User` with an email, username and password.
        :rtype: user
        """
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        # kwargs.__delitem__('confirm_password')

        user = self.model(email=self.normalize_email(email), username=kwargs.get('username'))
        # user = User.objects.create_user(username=kwargs.get('username'),
        #                                 email=kwargs.get('email'),
        #                                 password=kwargs.get('password'),)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __unicode__(self):
        return '%s' % self.username
