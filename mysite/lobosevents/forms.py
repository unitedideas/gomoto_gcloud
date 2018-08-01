from django import forms
from django.forms import modelformset_factory
from .models import Profile, UserEvent


ProfileFormSet = modelformset_factory(Profile, exclude=(), extra=-1,)

# ProfileFormSet = modelformset_factory(Profile, fields=(
#     'user', 'gender', 'birth_date', 'phone_number', 'country',
#     'address', 'address_line_two', 'city', 'state', 'zip_code',
#     'emergency_contact_name', 'emergency_contact_contact'))

UserEventFormSet = modelformset_factory(UserEvent, fields=(
    'event', 'bike_make', 'bike_displacement', 'omra_number', 'ama_number'))



#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ()
#
#
# class UserEventForm(forms.ModelForm):
#     class Meta:
#         model = UserEvent
#         exclude = ('user', 'age_on_event_day', 'confirmation', 'rider_number', 'start_time')
#
#
# class EventRegistrationForm(forms.Form):
#     """
#     Form for individual user links
#     """
#     UserProfileForm = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Link Name / Anchor Text',
#         }),
#         required=False)
#     UserEventForm = forms.URLField(
#         widget=forms.URLInput(attrs={
#             'placeholder': 'URL',
#         }),
#         required=False)
