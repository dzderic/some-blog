import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . import utils
from .forms import PostForm

def home(request):
    return render(request, 'home.html')

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(new_post.get_absolute_url())
    else:
        form = PostForm()

    return render(request, 'blog/new.html', {'form': form})

@login_required
def render_markdown(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    return HttpResponse(json.dumps({
        'result': utils.render_markdown(request.read()),
    }), mimetype="application/json")

def view_post(request, slug):
    return HttpResponse('')
