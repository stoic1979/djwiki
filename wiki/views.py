from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
#from django.views.generic.list_detail import object_list

from dashboard.forms import LoginForm

from models import Category, Article, Edit
from forms import ArticleForm, EditForm

def home(request):
    """
    home page view for the website
    """
    c = {'categories': Category.objects.all(), 'request': request}
    return render_to_response('index.html', c, context_instance=RequestContext(request))

def category(request, category_id):
    """
    page to show article list in a given category
    """
    category = Category.objects.get(id=category_id)
    c = {'categories': Category.objects.all(), 'articles': category.get_published_articles(), 'request': request}
    return render_to_response('category.html', c, context_instance=RequestContext(request))

def login_page(request):
    """
    If user is authenticated, direct them to the next page. 
    Otherwise, take them to the login page.

    :param request: django HttpRequest

    :return: django HttpResponse 
    """

    state = ""
    username = password = ''
    form = LoginForm()

    #default next page is index page
    next_page = "/"

    #getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        form = LoginForm(request.POST) # A form bound to the POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect(next_page) # Redirect after POST
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    c = {'state':state, 'username': username, 'form': form, 'next': next_page}
    c.update(csrf(request)) 

    return render_to_response('auth.html', c)

def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request':request})

"""
@login_required
def add_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        msg = "Article saved successfully"
        messages.success(request, msg, fail_silently=True)
        return redirect(article)
    return render_to_response('wiki/article_form.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))


@login_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    edit_form = EditForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        if edit_form.is_valid():
            edit = edit_form.save(commit=False)
            edit.article = article
            edit.editor = request.user
            edit.save()
            msg = "Article updated successfully"
            messages.success(request, msg, fail_silently=True)
            return redirect(article)
    return render_to_response('wiki/article_form.html', 
                              { 
                                  'form': form,
                                  'edit_form': edit_form,
                                  'article': article,
                              },
                              context_instance=RequestContext(request))

def article_history(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return  object_list(request, 
                        queryset=Edit.objects.filter(article__slug=slug),
                        extra_context={'article': article})
"""
