
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.views.generic import RedirectView

from sitewide.views import InviteGenerator, InviteSignView

urlpatterns = [
    # {'period': ['14'],
    # 'tmsp': ['1592377716.721264'],
    # 'ZaPPyCoDe': ['6bc519d4-3735-5f0e-a4eb-2052f6cedc70'],
    # 'email': ['fun_coding@zappycode.com']}'
    re_path(r'^free/(?P<period>(.)+)(?P<tmsp>(.)+)(?P<ZaPPyCoDe>(.)+)(?P<email>(.)+)$', InviteSignView.as_view(), name='invite_signup'),
    path('<str:period>/', InviteSignView.as_view(), name='invite_signup'),
    re_path(r'^$', login_required(InviteGenerator.as_view()), name='invite'),

                  #These are all direct links
    # links without trailing slash
    re_path(r'^/$', RedirectView.as_view(url='/invite')),
]
