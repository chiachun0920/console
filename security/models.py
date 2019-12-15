from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)

    created_date = models.DateTimeField(auto_now=True)

    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'


class AuthSafer(models.Model):
    username = models.CharField(max_length=32)

    encrypted_password = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now=True)

    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'auth_safter'

