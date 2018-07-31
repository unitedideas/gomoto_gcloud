from django import forms
from .models import Profile, UserEvent

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [None]

class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        exclude = ('user', 'age_on_event_day', 'confirmation', 'rider_number', 'start_time')








