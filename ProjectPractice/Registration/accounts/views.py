from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RigorousRegistrationForm


def register_view(request):
    # Check if the user clicked 'Submit' (sending data via POST method)
    if request.method == 'POST':
        # Load the form with the raw data the user typed in
        form = RigorousRegistrationForm(request.POST)
        
        # Run all our security and uniqueness validation algorithms
        if form.is_valid():
            # Build the user object in memory, but DO NOT save it to the DB yet
            user = form.save(commit=False)
            
            # Read the dropdown selection chosen by the user
            selected_role = form.cleaned_data.get('role')
            
            # Apply the strict role boolean flags to the object
            if selected_role == 'owner':
                user.is_owner = True
            else:
                user.is_standard_user = True
            
            # Save the user permanently to the database (Executes the SQL INSERT)
            user.save()
            
            # Send the user to the login page (we will build this URL shortly)
            return redirect('login')
            
    else:
        # If they are just opening the page for the first time, show an empty form
        form = RigorousRegistrationForm()
        
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


@login_required
def home_view(request):
    user = request.user
    if user.is_owner:
        role_label = 'Business Owner / Vendor'
    elif user.is_standard_user:
        role_label = 'Standard User / Customer'
    else:
        role_label = 'Administrator'
    return render(request, 'accounts/home.html', {'role_label': role_label})