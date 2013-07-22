from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template.context import RequestContext
from django.conf import settings
from user.forms import UserForm, ProfileForm
from user.models import Participante

def index(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def profile(request):
    try: request.user.get_profile()
    except: return HttpResponseRedirect("editar/")
        
    return render_to_response('user/profile.html', context_instance=RequestContext(request))

def profile_editar(request):
    
    try: p = request.user.get_profile()
    except: p = Participante(user=request.user)
          
    pf = ProfileForm(data=request.POST or None, instance=p)
    uf = UserForm(data=request.POST or None, instance=request.user)  

    if request.POST and pf.is_valid() and uf.is_valid():
        pf.save()
        uf.save()
        return HttpResponseRedirect("/user/profile/")
    
    return render_to_response('user/profile_editar.html', 
                              {'profileForm': pf,
                               'userForm': uf}, 
                              context_instance=RequestContext(request))