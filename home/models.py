import uuid
from django.db import models

class UserQuery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_no = models.CharField(max_length = 20, null=False, blank=False)  # Corrected PhoneNumberField
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"  # Optional: string representation of the model
