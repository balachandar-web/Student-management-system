from django.urls import path
from.views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("index/",index),
    path("add-std/",std_add),
    path("delete-std/<int:roll>",delete_std),
    path("update-std/<int:roll>",update_std),
    path("do-update-std/<int:roll>",do_update_std),

]
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
