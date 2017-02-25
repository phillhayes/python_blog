from django.contrib import admin
from .models import Blogpost
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Category)



 
class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
 

