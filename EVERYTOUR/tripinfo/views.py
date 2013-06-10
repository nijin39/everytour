# -*- coding : utf-8 -*-

import os
import datetime
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

 
@login_required
def index(request):
    t=loader.get_template('home.html')
    print_result='cc'
    c=Context({
        #'client_dirs' : client_dirs,
        'result' : print_result,
    })
    return HttpResponse(t.render(c))

@login_required
def registration(request):
    t=loader.get_template('registration.html')
    print_result='cc'
    c=Context({
        #'client_dirs' : client_dirs,
        'result' : print_result,
    })
    return HttpResponse(t.render(c))

@login_required
def statistics(request):
    t=loader.get_template('statistics_total.html')
    print_result='cc'
    c=Context({
        #'client_dirs' : client_dirs,
        'result' : print_result,
    })
    return HttpResponse(t.render(c))

@login_required
def timetable(request):
    t=loader.get_template('timetable.html')
    print_result='cc'
    c=Context({
        #'client_dirs' : client_dirs,
        'result' : print_result,
    })
    return HttpResponse(t.render(c))


def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('login.html',{'username': username}, context_instance=RequestContext(request))

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

