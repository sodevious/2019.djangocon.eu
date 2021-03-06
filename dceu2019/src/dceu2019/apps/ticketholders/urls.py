from django.urls import path

from . import views

app_name = 'ticketholders'


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('workshops/', views.WorkshopListView.as_view(), name='workshops'),
    path('workshops/<pk>/attend', views.WorkshopAttendView.as_view(), name='workshop_attend'),
    path('workshops/<pk>/unattend', views.WorkshopUnAttendView.as_view(), name='workshop_unattend'),
    path('bikes/booking/', views.BikeBooking.as_view(), name='bike_booking'),
    path('community/', views.CommunityView.as_view(), name='community'),
    path('tshirts/', views.TShirtView.as_view(), name='tshirts'),
    path('sprints/', views.SprintsUpdate.as_view(), name='sprints'),
]
