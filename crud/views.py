from django.urls import include
from django.conf.urls import url

from cruds_adminlte.crud import CRUDView
from cruds_adminlte.inline_crud import InlineAjaxCRUD

from .models import (
        Institution,
        Geoname,
        CooperationalRelationship,
    )

from .forms import (
        CooperationalRelationshipForm,
        InstitutionForm,
    )

class CooperationalRelationshipInlineCRUDView(InlineAjaxCRUD):
    model = CooperationalRelationship
    base_model = Institution
    inline_field = 'institution'
    title = "Cooperational Relationships"
    list_fields = ['city', 'description', ]
    add_form = CooperationalRelationshipForm
    update_form = CooperationalRelationshipForm

class InstitutionCRUDView(CRUDView):
    model = Institution
    search_fields = [
            'name__icontains', 
            ]
    add_form = InstitutionForm
    update_form = InstitutionForm
    list_fields = ['name','city','responsible_for_places', 'cooperational_relationships']
    inlines = [CooperationalRelationshipInlineCRUDView]

class GeonameCRUDView(CRUDView): 
    model = Geoname
    search_fields = [
            'name__icontains', 
            ]
    list_fields = ['name', 'population']


def get_urls(basepath='',namespace=None):

    return  [
                url(basepath, include(InstitutionCRUDView().get_urls(), namespace=namespace)),
                url(basepath, include(GeonameCRUDView().get_urls(), namespace=namespace)),
                url(basepath, include(CooperationalRelationshipInlineCRUDView().get_urls(), namespace=namespace)),
            ]
