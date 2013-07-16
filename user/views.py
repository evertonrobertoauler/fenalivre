from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('user/login.html', c, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login/')

@login_required
def profile(request):
    return render_to_response('user/profile.html', {'full_name': request.user.username}, context_instance=RequestContext(request))
