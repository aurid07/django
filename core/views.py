from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
<<<<<<< Updated upstream
def index(requests):
    return render(request, 'index.html')

=======

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
        
    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')
>>>>>>> Stashed changes
