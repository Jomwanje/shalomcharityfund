from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.header, name="header"),
    path('self/', views.about, name="about"),
    path('get_verified/', views.ngo, name="ngo"),
    path('not_verified/', views.not_verified, name="not_verified"),
    path('admin_verify/', views.verify_from_admin, name="verification_from_admin"),
    re_path(r'^verified_as_true/(?P<pk>\d+)/$', views.verification_status_true, name="verified_as_true"),
    re_path(r'^verified_as_false/(?P<pk>\d+)/$', views.verification_status_false, name="verified_as_false"),
    path('mail_Y/', views.mail_Y, name="mail_of_acceptance"),
    path('mail_N/', views.mail_N, name="mail_of_rejectance"),
    path('post_request/', views.post_request, name="post_request"),
    path('fund_request/', views.donation, name="fund_request"),  # Updated to point to the donation view
    path('payment/', views.payment, name='payment'),
    path('charge/', views.charge, name="charge"),
    path('home/', views.home, name="home"),  # Home URL pattern
    path('contact/', views.contact, name="contact"),  # Added the contact URL pattern
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
