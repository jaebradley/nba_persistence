from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise

application = Cling(get_wsgi_application())
DjangoWhiteNoise(get_wsgi_application())