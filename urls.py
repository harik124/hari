from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_log, name='user_log'),
    path('user_rg_pg', views.user_rg_pg, name='user_rg_pg'),
    path('user_home_pg', views.user_home, name='user_home'),
     path('user_prof_pg', views.user_prof, name='user_prof'),
     path('user_trip_pg', views.user_trip, name='user_trip'),
     path('user_payment_pg', views.user_payment, name='user_payment'),
     path('user_review_pg', views.user_review, name='user_review'),
     
     path('logOut', views.logOut),
    

    path('user_reg_btn', views.user_reg_btn),
    path('user_login_btn', views.user_login),
    path('bookTrip_btn/<id>/<pr>', views.bookTrip_btn),
    path('Userupdate_trip/<id>', views.Userupdate_trip),
     path('add_review', views.add_review),
]