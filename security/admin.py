from django.contrib import admin

from .models import User, AuthSafer


admin.site.register(User)

admin.site.register(AuthSafer)

