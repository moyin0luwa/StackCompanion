from django.shortcuts import render

# Create your views here.(Views are request handlers)
def home_page(request):
    return render(request, 'common/home.html')
