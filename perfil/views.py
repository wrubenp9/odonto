from django.shortcuts import render

# Create your views here.
def my_profile(request):
    template_name = 'my-profile.html'
    return render(request, template_name)