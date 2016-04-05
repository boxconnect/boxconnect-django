from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class YoutubeApphook(CMSApp):
    name = _("Youtube Application")   	# give your application a name (required)
    urls = ["youtube.urls"]           	# link your app to url configuration(s)
    app_name = "youtube"


apphook_pool.register(YoutubeApphook)	# register the application