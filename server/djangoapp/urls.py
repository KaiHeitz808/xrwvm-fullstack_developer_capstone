
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import logout_view
from .views import registration 

app_name = 'djangoapp'

urlpatterns = [
    # path for registration
 path("register/", registration, name="register"),
    # path for login
 path(route='login', view=views.login_user, name='login'),

    # path for dealer reviews view

    #path for logout
    path("logout/", logout_view, name="logout"),

    # path for add a review view


  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
