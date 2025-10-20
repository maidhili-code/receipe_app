from django.contrib import admin
from django.urls import path
from myapp.views import home, about, contact
from django.conf.urls.static import static
from django.conf import settings
from vege import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('receipe/', views.add_receipe, name='add_receipe'),
    path('receipe/delete/<int:id>/', views.delete_receipe, name='delete_receipe'),
    path('receipe/update/<int:id>',views.update_receipe,name='update_receipe'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
