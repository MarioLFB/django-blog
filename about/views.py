from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()
    # Instancia o formulário 'CollaborateForm'
    collaborate_form = CollaborateForm()

    # Combina 'about' e 'collaborate_form' em um único dicionário de contexto
    context = {
        "about": about,
        "collaborate_form": collaborate_form
    }

    # Passa o objeto request, o caminho do template, e o contexto único para a função 'render'
    return render(
        request,
        "about/about.html",
        context
    )