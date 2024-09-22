# from django.db import models
# import uuid
# # from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class User(): 
#     """
#     - id: Primary key, UUID field with default value set to a new UUID4.
#     - avatar: URL field for user's avatar, optional.
#     - email: Email field, unique and required.

#     Methods:
#     - __str__: Returns the username of the user.
#     """

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
#     avatar = models.URLField(null = True, blank = True)
#     email = models.EmailField(unique=True, null = False, blank = False)
#     first_name = models.CharField(max_length = 50)
#     last_name = models.CharField(max_length = 50, null = True, blank = True)
#     password = models.CharField(max_length=128, null = False, blank = False)
#     is_superuser = models.BooleanField(default=False)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

    

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    

