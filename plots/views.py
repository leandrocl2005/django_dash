from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/login/')
def index(request):
	return render(request,'index.html')



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'login.html')