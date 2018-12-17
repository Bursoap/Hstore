from django.contrib import admin

from django.forms import ModelForm
from django_admin_hstore_widget.forms import HStoreFormField

from . import models


class MyModelAdminForm(ModelForm):
    data = HStoreFormField()

    class Meta:
        model = models.GenericModel
        fields = '__all__'


@admin.register(models.GenericModel)
class GenericAdmin(admin.ModelAdmin):
    form = MyModelAdminForm
