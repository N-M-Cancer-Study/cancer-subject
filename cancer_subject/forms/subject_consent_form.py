from django import forms
# from edc_base.modelform_mixins import CommonCleanModelFormMixin

from ..choices import COMMUNITY
from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    study_site = forms.ChoiceField(
        label='Study site',
        choices=COMMUNITY,
        help_text="",
        widget=forms.RadioSelect())

    class Meta:
        model = SubjectConsent
        fields = '__all__'
