from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from django.contrib.auth.decorators import login_required


def home(request):
    authors = Author.objects.all().prefetch_related('quote_set')
    return render(request, 'app_main/index.html', {
        "msg": "hello",
        "authors": authors,
    })



def author(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    return render(request, 'app_main/author.html', {'author': author})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_main:author')
    return render(request, 'app_main/add_author.html', {'form': AuthorForm()})


@login_required
def add_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_main:home')
        else:
            form = QuoteForm()
    return render(request, 'app_main/add_quote.html', {'form': form})


@login_required
def edit(request, author_id):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        born_date = request.POST.get('born_date')
        born_location = request.POST.get('born_location')
        description = request.POST.get('description')

        Author.objects.filter(user=request.user, id=author_id).update(fullname=fullname, born_date=born_date,
                                                                      born_location=born_location,
                                                                      description=description)

        return redirect('app_main:author')

    author = Author.objects.filter(user=request.user, id=author_id).first()
    return render(request, 'app_main/edit.html', {'author': author, 'author_id': author_id})


@login_required
def remove(request, author_id):
    author = Author.objects.filter(user=request.user, id=author_id).first()
    if author:
        author.delete()
    return redirect(to="app_main:author")



