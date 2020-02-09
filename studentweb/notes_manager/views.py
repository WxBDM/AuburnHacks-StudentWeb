from django.shortcuts import render

# Create your views here.
def notesHTML(request):
	return render(request, "notes_manager/notes_manager.html")