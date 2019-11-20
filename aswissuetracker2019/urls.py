"""aswissuetracker2019 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth import logout
from aswissues.views import Issue, Login, Register, HomePageView
from django.conf.urls.static import static
from aswissues.views import NewIssue, DetailedIssue, issue_vote, issue_unvote, issue_watch, issue_unwatch, issue_delete, delete_comment, EditarIssue, AttachIssue, update_comment, ChangeState

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issue/<slug:pk>/', DetailedIssue.as_view(), name="issueDetall"),
    path('issue/', NewIssue.as_view()),
    path('login/', Login.as_view()),
    path('attach/<slug:pk>/', AttachIssue.as_view(), name="fitxerAdjunt"),
    path('chstate/<slug:pk>/<slug:status>', ChangeState.as_view(), name='change_state'),
    path('register/', Register.as_view()),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', include('django.contrib.auth.urls'), name='logout'),
    path('edit/<slug:id>/', EditarIssue, name='EditarIssue'),
    path('issue/<slug:pk>/vote', issue_vote, name='issue_vote'),
    path('issue/<slug:pk>/delete', issue_delete, name='issue_delete'),
    path('issue/<slug:pk>/unvote', issue_unvote, name='issue_unvote'),
    path('issue/<slug:pk>/watch', issue_watch, name='issue_watch'),
    path('issue/<slug:pk>/unwatch', issue_unwatch, name='issue_unwatch'),
    path('issue/<slug:id>/comment/delete/<slug:pk>', delete_comment, name='delete_comment'),
    path('issue/<slug:id>/comment/update/<slug:pk>', update_comment, name='update_comment'),

    path('auth/', include(('social_django.urls', 'social_django'), namespace='social_auth')),
    url(r'^$', HomePageView.as_view(), name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
