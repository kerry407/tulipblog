"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.registerform, name='register'),
    path('login/', user_views.loginform, name = 'login'),
    path('logout/', user_views.logoutuser, name='logout'),
    path('userprofile/', user_views.userprofile, name='userprofile'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('userupdate/', user_views.userupdate, name='userupdate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete')
]


if settings.DEBUG:    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# submit email form ------------------------------------- //PasswordResetView.as_view()//
# Email sent success message ----------------------------//PasswordResetDoneView.as_view()//
# Link to Password Reset form in user's emaill----------//PasswordResetConfirmView.as_view()//
# Password Successfully changed message ----------------//PasswordResetCompleteView.as_view()//
