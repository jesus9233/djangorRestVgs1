from django.shortcuts import render, redirect, HttpResponse

from .forms import CreditCardForm

    
def index(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/ccPost/')
            return HttpResponse("data submitted successfully")

    else:
        form = CreditCardForm()

    return render(request, 'index.html', {'form': form})


def ccPost(request):
    
    return HttpResponse("data submitted successfully")