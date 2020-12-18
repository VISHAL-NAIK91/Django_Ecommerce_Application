from django.views import View

from django.shortcuts import render, redirect,HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import  check_password



class Login(View):
    returnURL = None
    def get(self,request):
        Login.returnURL = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.returnURL:
                    return HttpResponseRedirect(Login.returnURL)
                else:
                    Login.returnURL = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"
        return render(request, 'login.html', {"error": error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

