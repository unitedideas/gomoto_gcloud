from .models import Profile, UserEvent
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .decorators import check_recaptcha
from django.shortcuts import render, reverse, redirect, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from tablib import Dataset
from .resources import PersonResource
from django.core.mail import send_mail
import urllib
import json
from django.conf import settings
from django.contrib import messages
from .forms import ProfileFormSet, UserEventFormSet


def login(request):
    numbers = [1,2,3,4,5]
    name = 'Shane Cheek'



    args = {'name': name, 'numbers': numbers}

    # the render method also takes an optional dictionary object that passes through to the view(template)
    return render(request, 'lobosevents/login.html', args )




























def cancelorder(request):
    return render(request, 'lobosevents/cancelorder.html')


def event_reg_confirmation(request):
    return render(request, 'lobosevents/event_reg_confirmation.html')


def profile(request):
    return render(request, 'lobosevents/profile.html')


# @login_required
def event_registration(request):
    # user = request.user
    # print(user)
    # user = User.objects.filter(username=request.user)
    # print(user)

    profileformset = ProfileFormSet()
    usereventformset = UserEventFormSet()

    for form in profileformset:
        # form.fields['user'].queryset = User.objects.filter(username=request.user)
        print(form)
        print()
    for form in usereventformset:
        print(form)
        print()

    return render(request, 'lobosevents/event_registration.html',
                  {'profileformset': profileformset, 'usereventformset': usereventformset})

    # todo_text = request.POST['todo_item_id_key_in_template']
    # todo_item = TodoItem.objects.get(pk=todo_text)
    # todo_item.delete()
    # # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # # save data from request.POST in database
    # # redirect back to the index page (HttpResponseRedirect)
    #
    # return HttpResponseRedirect(reverse('lobosevents:event_registration'))


# create an email function - This function will be used across the site, maybe a mass email function as well
def single_email():
    pass


# @check_recaptcha
def register(request):
    print()
    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    print('resp')
    print(recaptcha_response)
    print()

    ''' End reCAPTCHA validation '''
    # if not request.recaptcha_is_valid:
    #     return HttpResponseRedirect(reverse('lobosevents:login_register')+'?message=bad_recaptcha')
    try:
        username = request.POST['username'].lower()
        for letter in username:
            if not letter.isdigit() and not letter.isalpha():
                return HttpResponseRedirect(reverse('lobosevents:login_register') + '?message=bad_username')

        # turn this back on for email confirmation
        # email = request.POST['email']
        # password = request.POST['password']
        # user = User.objects.create_user(username, email, password)
        # login(request, user)
        # send_mail(
        #     'Test user registration Subject',
        #     'Welcome to gomoto ' + user.username.title() + '. \nHere is the test user registration message.\nYour username is ' + user.username + '\nYour password is ' + password + '\nYou can view your race history in your profile https://www.gomoto.io/profile' + '\nYou can register for our events at https://www.gomoto.io/event_registration',
        #     'unitedideas@gmail.com',
        #     [user.email],
        #     fail_silently=False,
        # )
        return HttpResponseRedirect(reverse('lobosevents:profile'))
    except:
        return HttpResponseRedirect(reverse('lobosevents:login_register') + '?message=duplicate_username')


# @check_recaptcha
def mylogin(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('lobosevents:login_register') + '?message=bad_recaptcha')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('lobosevents:profile'))
    return HttpResponseRedirect(reverse('lobosevents:login_register'))


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('lobosevents:login_register'))


def login_register(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    return render(request, 'lobosevents/login_register.html', {'next': next, 'message': message})


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )
