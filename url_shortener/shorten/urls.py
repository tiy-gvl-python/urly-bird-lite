from django.conf.urls import include, url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView
from .views import home, AllMarks, SingleMark, activate, activate_work, permission_denied

urlpatterns = [
    url('^$', home, name='home'),
    url('^register/$', CreateView.as_view(
        template_name='registration/create_user.html',
        form_class=UserCreationForm,
        success_url='/'),
        name='register'),
    url(r'^accounts/login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='Logout'),
    url(r'^bookmarks/$', AllMarks.as_view(), name='all_marks'),
    url(r'^bookmarks/(?P<pk>\d+)$', SingleMark.as_view(), name="delete_category"),
    url(r'^activates/$', activate, name='activate'),
    url(r'^activate/$', activate_work, name='activate_work'),
    url(r'^permission-denied/$', permission_denied, name='denied'),

]
