from django.contrib.auth.views import LogoutView


class LoggedOut(LogoutView):
    template_name = "account/logged_out.html"
