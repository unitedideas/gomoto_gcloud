

from gaesessions import SessionMiddleware

import os

COOKIE_KEY = r'OKLW\xc1\xc6\xdc\xa5D.\xf1G2g\x8f\xff\x15V?\xed]<\xc6$\x15g\x97\xc3\xd6\x1a.\x8b\xfaT?\xd4}Iy33\xf5\xf5\xe4\x14av\x9c\xe4\xa0\xec\xcc\xabs\x0e\xa8f\x96\xa8O\xe8\xa12\xae'

def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
    app = recording.appstats_wsgi_middleware(app)
    return app