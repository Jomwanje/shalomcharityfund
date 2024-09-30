from django.db import models

# Assuming NGO model is defined in user.models
from user.models import NGO  # Import NGO model

# Model for Donation Requests
class DonationRequest(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)  # Reference to NGO
    request_date = models.DateTimeField(auto_now_add=True)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Request by {self.ngo.name} on {self.request_date}"


# Tracks views on a donation request
class DonationRequestView(models.Model):
    donation_request = models.ForeignKey(DonationRequest, on_delete=models.CASCADE)
    viewer_name = models.CharField(max_length=255)
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"View by {self.viewer_name} on {self.view_date}"


# Model to track donor contributions
class Donation(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='charity_donations')
    donation_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    email = models.EmailField()
    payment_method = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Donation of {self.amount} to {self.ngo.name}"


# FundRequest model for NGOs requesting funds for specific purposes
class FundRequest(models.Model):
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    amount_needed = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title} - {self.ngo.name}"


# Add methods to the NGO model
class NGO(models.Model):
    # Existing fields...
    objects = None
    name = models.CharField(max_length=255)
    email = models.EmailField()
    registration_number = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    verification_docs = models.FileField(upload_to='verification_docs/')

    def verification_true(self):
        self.verified = True
        self.save()

    def verification_false(self):
        self.verified = False
        self.save()
