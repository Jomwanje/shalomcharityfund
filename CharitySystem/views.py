import stripe
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationForm, NGOForm, FundRequestForm  # Importing all necessary forms
from .models import NGO, FundRequest  # Import FundRequest and NGO models

# Set the Stripe API key
stripe.api_key = 'sk_test_TjwJ8KIE4pM0zUDkkubD4kvV00PipgfR59'


# View for the home page
def home(request):
    return redirect('about')  # Redirect to the about page or another page of your choice


# View for the header
def header(request):
    return render(request, 'CharitySystem/header.html')


# View for the about page
def about(request):
    return render(request, 'CharitySystem/self.html')


# View for NGO form handling
def ngo(request):
    if request.method == 'POST':
        form = NGOForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful NGO form submission
    else:
        form = NGOForm()
    return render(request, "CharitySystem/get_verified.html", {'form': form})


# View for NGOs not verified
def not_verified(request):
    return render(request, "CharitySystem/not_verified.html")


# View for verifying NGOs by admin
def verify_from_admin(request):
    data = NGO.objects.all()
    return render(request, "CharitySystem/verify_from_admin.html", {'ngo': data})


# View for setting verification status to True
def verification_status_true(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    ngo.verified = True  # Update the verified field
    ngo.save()  # Save the changes to the database

    send_mail(
        'SaathiHaathBadhana | Verification Status',
        'Our admins have deemed your verification to be correct.',
        'jomwanjegachui@gmail.com',
        [ngo.email],  # Send to the NGO's email
        fail_silently=False,
    )

    return redirect("mail_of_acceptance")  # Updated to use URL name


# View for setting verification status to False
def verification_status_false(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    ngo.verified = False  # Update the verified field
    ngo.save()  # Save the changes to the database

    send_mail(
        'SaathiHaathBadhana | Verification Status',
        'Our admins have deemed your verification to be incorrect.',
        'jomwanjegachui@gmail.com',
        [ngo.email],  # Send to the NGO's email
        fail_silently=False,
    )

    return redirect("mail_of_rejectance")  # Updated to use URL name


# Success mail view (Yes)
def mail_Y(request):
    return render(request, "CharitySystem/mail_Y.html")


# Failure mail view (No)
def mail_N(request):
    return render(request, "CharitySystem/mail_N.html")


# View for donation form
def donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful donation
    else:
        form = DonationForm()
    return render(request, "CharitySystem/request_form.html", {'form': form})


# View for displaying fund requests
def post_request(request):
    data = FundRequest.objects.all()
    return render(request, "CharitySystem/post_request.html", {'data': data})


# View for handling fund requests
def fund_request(request):
    if request.method == 'POST':
        form = FundRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after successful fund request
    else:
        form = FundRequestForm()
    return render(request, "CharitySystem/request_form.html", {'form': form})


# View for payment page
def payment(request):
    return render(request, 'CharitySystem/payment.html')


# View for handling Stripe charge
def charge(request):
    if request.method == 'POST':
        cus_name = request.POST["cus_name"]
        amount = request.POST["amount"]
        donation_message = request.POST["message"]
        mail = request.POST["mail"]

        customer = stripe.Customer.create(
            email=mail,
            name=cus_name,
            source=request.POST["stripeToken"]
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount) * 100,  # Convert to cents
            currency='usd',
            description=donation_message
        )

        return render(request, 'CharitySystem/success_payment.html', {'amount': amount})

    return redirect('payment')  # Redirect to payment page if the request is not POST


# View for the contact page
def contact(request):
    return render(request, 'CharitySystem/contact.html')
