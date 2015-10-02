from django.conf.urls import url


urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
        name='marcador_bookmark_user'),
    url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]

# """
# #Regex for view of bookmark List
# r'^$'
#     '^'     - beginning of string
#     '$'     - end of string
#     '^$'    - nothing is in between (empty character);
#             that particular view is reachable from the home page
#
# #Regex for view of bookmark List
# r'^user/(?P<username>[-\w]+)/$'.
#     user/                   - static part; must match exactly
#     (?P<username>[-\w]+)    - all the following letters, numbers, underscores and dashes (defined by [-\w]+)
#                             can be accessed using the variable 'username'.
#
# """"


