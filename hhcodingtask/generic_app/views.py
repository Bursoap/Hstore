from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from . import models
from . import forms


class GenericCreateView(SuccessMessageMixin, CreateView):
    model = models.GenericModel
    form_class = forms.GenericCreateForm
    template_name = 'generic_app/generic_create.html'
    success_url = '/'
    success_message = 'Success! Object was successfully created'
