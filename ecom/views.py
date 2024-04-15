from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
def cart(request):
    return render(request, 'main/cart.html')
def home(request):
    data = {
        'product1': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd'),
        'product2': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd'),
        'product3': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd')


    }
    return render(request, 'main/index.html', data)


def product(request):
    return render(request, 'main/product.html')
def products(request):
    data = {
        'product1': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd'),
        'product2': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd'),
        'product3': ('image.png','product1', '909', '9', 'descriptioosdfjsdlkfjsldkdffjsd')


    }
    return render(request, 'main/products.html', data)

def signout(request):
    logout(request)
    return redirect('home')

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            dateofbirth = form.cleaned_data['dateofbirth']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.city = city
            user.phone_number = phone_number
            user.dateofbirth = dateofbirth
            user.save()

            print('User created successfully')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()

    data = {"form": form}
    return render(request, 'registration/signup.html', data)
