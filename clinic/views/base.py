from django import forms
from django.db import models

class CrudMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, field in form.fields.items():
            # Add Bootstrap classes
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
            
            # Add HTML5 date/time pickers for Date and DateTime fields
            try:
                model_field = self.model._meta.get_field(field_name)
                if isinstance(model_field, models.DateTimeField):
                    field.widget = forms.DateTimeInput(
                        attrs={'class': 'form-control', 'type': 'datetime-local'},
                        format='%Y-%m-%dT%H:%M'
                    )
                elif isinstance(model_field, models.DateField):
                    field.widget = forms.DateInput(
                        attrs={'class': 'form-control', 'type': 'date'},
                        format='%Y-%m-%d'
                    )
            except models.FieldDoesNotExist:
                pass
        return form
