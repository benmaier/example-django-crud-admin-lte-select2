from django import forms
from django.utils import timezone

from .models import (
        Institution,
        Geoname,
        CooperationalRelationship,
    )

from .widgets import (
        SingleGeonameSelectWidget,
        MultipleGeonameSelectWidget,
    )


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        exclude = []
        widgets = { 
                    'city': SingleGeonameSelectWidget, 
                    'responsible_for_places': MultipleGeonameSelectWidget, 
                }

class CooperationalRelationshipForm(forms.ModelForm):
    class Meta:
        model = CooperationalRelationship
        exclude = ['institution']
        widgets = { 
                    'city': SingleGeonameSelectWidget, 
                  }
