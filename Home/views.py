from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    contex = {
        "form": form
    }
    return render(request, "home/contact.html", contex)
