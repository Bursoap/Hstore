from django import forms

from . import models
from . import scheme
from . utils import HstoreFieldsBuilderMixin


class GenericCreateForm(forms.ModelForm, HstoreFieldsBuilderMixin):

    class Meta:
        model = models.GenericModel
        exclude = ['data', ]

    scheme = scheme.GENERAL_SCHEME

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_fields_from_scheme()

    def save(self, commit=False):
        instance = super().save(commit=False)
        self.add_data_to_hstore(instance, 'data')
        instance.save()
        return instance
