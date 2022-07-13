from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse

from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Meetup, Participant
from .forms import RegistrationForm
def index(request):
    meetups = Meetup.objects.all()
    '''[
        { 'title' : 'the first meetup','location': 'New York','slug' : 'a-first-meetup'},
        { 'title' : 'the second meetup','location': 'Paris','slug' : 'a-second-meetup'},
        { 'title' : 'the third meetup','location': 'LasVegas','slug' : 'a-third-meetup'},
        { 'title' : 'the fourth meetup','location': 'London','slug' : 'a-fourth-meetup'}

    ]
    '''
    return render(request, 'meetups/includes/index.html',
    { 'meetups': meetups})

     
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug = meetup_slug)
        if request.method =="GET":
            registration_form = RegistrationForm()
            '''{
                'title':'The first meetup',
                'description':'this is the first meetup!!'
            }'''
            
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')



        return render(request,'meetups/includes/meetup-details.html',
            {
                'meetup_found':True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request,'meetups/includes/meetup-details.html',
        {'meetup_found':False})

def confirm_regsistration(request):
    return render(request, 'meetups/registration-submission.html')