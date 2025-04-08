from django.shortcuts import render,redirect
from . models import *
from admin_view.models import *
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.
def user_log(request):
    return render(request,"user_index.html")

def user_review(request):
    return render(request,"review.html")
def logOut(request):
    request.session['user_id'] = "user.id"
    return redirect('user_log')

def user_payment(request):
    return render(request,"payment.html")

def user_rg_pg(request):
    return render(request,"user_reg.html")

def user_home(request):
    user = USER_DB.objects.get(id=request.session['user_id'])
    data=bookTrip.objects.filter(user=user)
    ale=Alert.objects.all()
    return render(request,"user_home.html",{"data":data,"ale":ale})

def user_prof(request):
    if 'user_id' not in request.session:
        return redirect('user_log')
    
    user = USER_DB.objects.get(id=request.session['user_id'])
    return render(request, 'prof.html', {'user': user})



def user_trip(request):
    trip_type = request.GET.get('trip_type')
    if trip_type:
        data = Trip.objects.filter(trip_type=trip_type)
    else:
        data = Trip.objects.all()

    return render(request, 'user_trip.html', {'data': data})


def user_reg_btn(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        password = request.POST.get('password')
        terms_accepted = request.POST.get('terms') == 'on'  # Checkbox returns 'on' when checked
        
        
        try:
            # Create and save user
            user = USER_DB(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                password=password,  # Hash the password
                terms_accepted=terms_accepted
            )
            user.save()
            
            return redirect('user_log')  # Replace with your login URL name
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect('user_rg_pg')
    return render(request,"user_reg.html")

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Check if user exists
            user = USER_DB.objects.get(email=email)
            print(user.password)
            print( check_password(password, user.password))
            # Verify password
            if (password== user.password):
                # Password matches - login successful
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_name'] = f"{user.first_name} {user.last_name}"
                return redirect('user_home')  # Replace with your home page URL name
            else:
                messages.error(request, "Invalid email or password")
        except USER_DB.DoesNotExist:
            pass
            messages.error(request, "Invalid email or password")
        
        return redirect('user_log')  # Redirect back to login page if authentication fails
    
    # GET request - show login form
    return render(request, 'login.html')  # Update with your template path

def bookTrip_btn(request, id,pr):
    data={"pr":pr,"trip_id":id}
    return render(request, 'payment.html',data)  # Update with your template path

    
    
 
def Userupdate_trip(request,id):
    user = USER_DB.objects.get(id=request.session['user_id'])
    tripobj = Trip.objects.get(id=id)

    # Check if the booking already exists for the given user and trip
    if bookTrip.objects.filter(user=user, trip=tripobj).exists():
        # If it exists, you can redirect with a message or handle it as needed
        return redirect('user_home')  # Or any page with a message that the booking already exists

    try:
        # Create and save user booking if it doesn't exist
        tr = bookTrip(
            user=user,
            trip=tripobj,
            status="Confirmed"
        )
        tr.save()
        
        # Redirect to the home page or wherever necessary
        return redirect('useruser_home_log')  # Replace with your login URL name
        
    except Exception as e:
        # If an exception occurs, redirect to a fallback page
        return redirect('user_home')


def add_review(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('review')
        user = USER_DB.objects.get(id=request.session['user_id'])
        
        # Create and save new review
        Review.objects.create(
            name=user,
            review_title=title,
            review=content
        )
        
        messages.success(request, 'Thank you for your review!')
        return redirect('user_home')
    return redirect("user_home")