# views.py
from django.shortcuts import render, redirect
from .forms import CardForm

def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view_to_redirect')
    else:
        form = CardForm()
    return render(request, 'create_card.html', {'form': form})
