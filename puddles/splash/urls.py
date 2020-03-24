from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, PrivacyPolicyView, TermsOfServiceView

urlpatterns = [
    # home page
    path("", HomeView.as_view(), name="home"),
    # about page
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # privacy policy
    path(
        "privacy-policy", PrivacyPolicyView.as_view(), name="privacy-policy"
    ),
    # terms of service
    path(
        "terms-of-service", TermsOfServiceView.as_view(), name="terms-of-service"
    ),
]
