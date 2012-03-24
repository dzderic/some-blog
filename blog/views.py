import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required

from . import utils

def home(request):
    return render(request, 'home.html')

@login_required
def new_post(request):
    return render(request, 'blog/new.html')

@login_required
def render_markdown(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    return HttpResponse(json.dumps({
        'result': utils.render_markdown(request.read()),
    }), mimetype="application/json")
