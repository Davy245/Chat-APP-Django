from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def detail(request,pk):
    context = {}
    return render(request, "detail.html", context)

