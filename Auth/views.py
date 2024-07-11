from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile
import qrcode
import os
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and get the instance
            username = form.cleaned_data.get('username')
            user_id = form.cleaned_data.get('id')  # Get the custom ID from the form

            # Assuming you have a UserProfile model or similar
            # Update the UserProfile with the user instance and the custom ID
            UserProfile.objects.update_or_create(user=user, defaults={'custom_id': user_id})

            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('success')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def success(request):
    # Assuming the UserProfile has a field named 'custom_id'
    user_profile = UserProfile.objects.get(user=request.user)
    user_id = user_profile.custom_id

    # Construct the QR code image path
    qr_code_path = f"/media/user_qr_codes/user_{user_id}.png"

    # Pass the path to the template
    context = {'qr_code_path': qr_code_path}
    return render(request, 'success.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')



def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and get the instance
            username = form.cleaned_data.get('username')
            user_id = form.cleaned_data.get('id')  # Get the custom ID from the form

            # Assuming you have a UserProfile model or similar
            UserProfile.objects.update_or_create(user=user, defaults={'custom_id': user_id})

            # Generate QR code
            qr_data = f"name: {username}, ID: {user_id}"
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Define the path for saving the QR code image
            qr_code_directory = os.path.join(settings.MEDIA_ROOT, 'user_qr_codes')
            if not os.path.exists(qr_code_directory):
                os.makedirs(qr_code_directory)

            qr_code_path = os.path.join(qr_code_directory, f"user_{user_id}.png")
            img.save(qr_code_path)

            messages.success(request, 'Account created for ' + username)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})





