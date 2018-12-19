from django import forms


class HstoreFieldsBuilderMixin:

    _fields_names_list = []
    scheme = None

    def add_fields_from_scheme(self):
        if self.scheme:
            for field_scheme in self.scheme:
                try:
                    field_name = field_scheme['field_name']
                    field_type = field_scheme['field_type']
                except KeyError:
                    raise KeyError('please, set field_name and field_type in field scheme')
                self._fields_names_list.append(field_name)
                field = getattr(forms, field_type)
                kwargs = field_scheme.get('kwargs', {})
                self.fields[field_name] = field(**kwargs)

    def add_data_to_hstore(self, instance, hstore_field_name):
        if self.scheme:
            data = {
                key: val for key, val in self.cleaned_data.items() if key in self._fields_names_list
            }
            setattr(instance, hstore_field_name, data)
