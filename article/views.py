from django.shortcuts import render

# Create your views here.
def articleList(request):
    return render(request, 'articlePage.html', {})

def articleView(request):
    return render(request, 'articleView.html', {})

def createArticle(request):
    return render(request, 'createArticle.html', {})

def editArticle(request):
    return render(request, 'editArticle.html', {})