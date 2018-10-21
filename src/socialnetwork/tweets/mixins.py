from django import forms
from django.forms.utils import ErrorList

class UserRequiredMixin(object):
    def form_valid(self,form):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            print(self.request.user)
            form.instance.user = self.request.user
            return super(UserRequiredMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)
