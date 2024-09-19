from django.shortcuts import render, redirect
from django.contrib import messages

from user.models import User
from user.serializers import RegisterationSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
# Create your views here.

def LoginView(request):
    try:
        if request.method == 'POST':
            username = request.data['email']
            password = request.data['password']
            
            if not User.objects.filter(email = username).exists() :
               messages.error(request, 'user with this email does\'nt exists')
               return redirect('login')
            
            user = authenticate(password = password, username = username)
            if user:
                # Create session for the registered user
                request.session['user_id'] = user.id  # Store user's ID in session
                request.session['user_email'] = user.email  # Optionally store the user's email in session

                messages.success(request, 'Login successful!')
                
                if user.is_superuser:
                    return redirect('index')
                    # return redirect('admin')

                # login   
                return redirect('index')
            
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('login')
                # return redirect('dahsboard')

        else :
            id = request.session.get('user_id', None)
            if id and User.objects.filter(id = id).exists():
                return redirect('index') 
            
            return render(request, 'login.html') # render index.html
    
    except Exception as e:
        messages.error(request, 'Something Went Wrong')
        return redirect('login')

def RegisterView(request):
    try:
        if request.method == 'POST':   
            data = request.POST
            
            # serialize and save
            serializer = RegisterationSerializer(data = data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Create session for the registered user
            request.session['user_id'] = user.id  # Store user's ID in session
            request.session['user_email'] = user.email  # Optionally store the user's email in session

            messages.success(request, 'Registration successful!')
            return redirect('index') 

        else:
            return render(request, 'register.html') # render index.html
    
    except Exception as e:
        print(str(e))
        messages.error(request, str(e))
        return redirect('register')