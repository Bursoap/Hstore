from django import forms
from django.conf import settings


class GeneralFormFieldsBuilderMixin:

    _fields_names_list = []

    def add_fields_from_scheme(self):
        if settings.GENERAL_SCHEME:
            for field_scheme in settings.GENERAL_SCHEME:
                try:
                    field_name = field_scheme['field_name']
                    field_type = field_scheme['field_type']
                except KeyError:
                    raise KeyError(
                        'please, set field_name and field_type in field scheme'
                    )
                self._fields_names_list.append(field_name)
                field = getattr(forms, field_type)
                kwargs = field_scheme.get('kwargs', {})
                self.fields[field_name] = field(**kwargs)

    def add_data_to_hstore(self, instance, hstore_field_name):
        if settings.GENERAL_SCHEME:
            data = {
                key: val for key, val in self.cleaned_data.items() if key in self._fields_names_list
            }
            setattr(instance, hstore_field_name, data)
