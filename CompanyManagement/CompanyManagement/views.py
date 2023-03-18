from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class Login(LoginView):
    template_name = 'CompanyManagement/AuthModule/Authentication/login.html'


class Logout(LogoutView):
    template_name = 'CompanyManagement/AuthModule/Authentication/logout.html'


class ChangePassword(PasswordChangeView):
    template_name = 'CompanyManagement/AuthModule/ChangePassword/ChangePassword.html'
    success_url = '/change-password-Done/'


class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'CompanyManagement/AuthModule/ChangePassword/ChangePasswordDone.html'


class ResetPassword(PasswordResetView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPassword.html'
    success_url = '/reset-Password-Done/'


class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordDone.html'
    success_url = '/reset-Password-Done/'


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordConfirm.html'
    success_url = '/reset/done/'


class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = 'CompanyManagement/AuthModule/ForgotPassword/ResetPasswordComplete.html'
