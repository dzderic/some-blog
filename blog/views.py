import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect, \
                        Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

from . import utils
from .forms import PostForm
from .models import Post

def home(request, page=1):
    paginator = Paginator(Post.objects.order_by('-date_posted'),
                          settings.POSTS_PER_PAGE)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        raise Http404

    return render(request, "home.html", {
        "posts": posts,
    })

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(new_post.get_edit_url())
    else:
        form = PostForm()

    return render(request, "blog/edit.html", {"form": form})

@login_required
def render_markdown(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    return HttpResponse(json.dumps({
        "result": utils.render_markdown(request.read()),
    }), mimetype="application/json")

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/view.html", {"post": post})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(new_post.get_edit_url())
    else:
        form = PostForm(instance=post)

    return render(request, "blog/edit.html", {"form": form})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        if request.POST["amisure"] == "youbetiam":
            post.delete()
            return HttpResponseRedirect("/")

    return render(request, "blog/delete.html", {"post": post})
