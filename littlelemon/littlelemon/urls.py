from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from Restaurant import views

router = routers.DefaultRouter()


router.register(r'users', viewset=views.UserViewSet)
router.register(r'tables', viewset=views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('Restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]
