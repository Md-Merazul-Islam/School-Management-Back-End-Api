from django.db import models
from django.contrib.auth.models import User
import uuid

class Fee(models.Model):
    fee_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Failed', 'Failed')], default='Pending')

    def save(self, *args, **kwargs):
        if not self.fee_id:
            self.fee_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.due_date} - {self.status} - {self.fee_id}"
