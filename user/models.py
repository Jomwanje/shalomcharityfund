from django.db import models


class NGO(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)  # Contact email
    registration_number = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    verification_docs = models.FileField(upload_to='verification_docs/', blank=True,
                                         null=True)  # Verification documents

    def __str__(self):
        return self.name


class Donation(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='user_donations')
    donation_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    email = models.EmailField()
    payment_method = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Donation of {self.amount} by {self.donor_name} to {self.ngo.name}"
