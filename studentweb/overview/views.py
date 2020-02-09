from django.shortcuts import render

# Create your views here.
def overview_page(request):
    return render(request, "overview/class_overview.html")