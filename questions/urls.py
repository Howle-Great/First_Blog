from django.conf.urls import url

from questions.views import *

urlpatterns = [
    path(r'^questions/', include('questions.urls')),
    path(r'^admin/', admin.site.urls),

    #path(r'^', TagView.as_view(), name=""),

]