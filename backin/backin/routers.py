from rest_framework import routers

#API views
# from business import views as business_api
from accounts import views as auth_views

def set_auth_routes():
    router = routers.DefaultRouter()
    router.register(r'signup/', auth_views.SignupView, basename='SignUp')
    router.register(r'login/', auth_views.LoginView, basename='Login')
    return router

def set_api_routes():
    router = routers.DefaultRouter()
    # router.register(r'risks', risks_api.getRisks)
    return router

def set_cms_routes():
    router = routers.DefaultRouter()
    # router.register(r'risks', risks_api.getRisks)
    return router
