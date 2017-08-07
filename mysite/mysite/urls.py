from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

from account.views import CountryViewSet, AccountViewSet
from article.views import ItemViewSet
from discussions.views import DeliberationViewSet, AnswerViewSet
from problem.views import CompetitionViewSet, ProblemViewSet, ProblemTestViewSet

router = DefaultRouter()

router.register(r'countries', CountryViewSet, base_name='country')
router.register(r'accounts', AccountViewSet, base_name='account')
router.register(r'items', ItemViewSet, base_name='item')
router.register(r'deliberations', DeliberationViewSet, base_name='deliberation')
router.register(r'competition', CompetitionViewSet, base_name='competition')
router.register(r'problemTests', ProblemTestViewSet, base_name='problemTest')
router.register(r'problems', ProblemViewSet, base_name='problem')
router.register(r'countries', CountryViewSet, base_name='country')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^auth/login', obtain_jwt_token, name='auth-token'),
    url(r'^auth/refresh-token', refresh_jwt_token, name='refresh-token'),
    url(r'^auth/verify-token', verify_jwt_token, name='verify-token'),

]
