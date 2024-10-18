from django.shortcuts import render
from .forms import MyForm


def home(request):
    return render(request, 'home.html')

def new(request):
    # Setting the variables of name and last_name to None
    # this is done to insure that the varibles are not empty when the page is loaded
    name = None
    last_name = None

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():  # This checks if the form inputs are valid
            # Process the cleaned form data
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
    else:
        form = MyForm()
    
    return render(request, 'new.html', {'form': form, 'name': name, 'last_name': last_name})

