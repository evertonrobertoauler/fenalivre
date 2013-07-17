from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.context import RequestContext
from user.forms import UserRegistrationForm
from django.conf import settings

def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def profile(request):
    return render_to_response('user/profile.html', {'full_name': request.user.username}, context_instance=RequestContext(request))

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserRegistrationForm()
        
    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response('user/registro.html', args)