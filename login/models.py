from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class UserRegisterForm(UserCreationForm):
	email = models.EmailField()
	username = models.CharField(max_length = 20)
	first_name = models.CharField(max_length = 20)
	# last_name = models.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'password']