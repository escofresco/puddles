from django.views.generic import TemplateView
from django.conf import settings

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Puddles"
        print(settings.ACCOUNT_ALLOW_REGISTRATION)
        return context

class PrivacyPolicyView(TemplateView):
    template_name = "pages/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Privacy Policy"
        return context

class TermsOfServiceView(TemplateView):
    template_name = "pages/terms_of_service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Terms of Service"
        return context
