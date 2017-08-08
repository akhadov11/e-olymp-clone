from django.conf import settings
from django.contrib.sites.models import Site


str2bool = lambda s: s.lower() in ['true', 'yes', 't', '1']


def get_service_host(site=None):
    current_site = site if site else Site.objects.get_current()
    protocol = getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http")
    service_url = "{0}://{1}".format(
        protocol,
        current_site.domain
    )
    return service_url
