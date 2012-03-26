from django.conf import settings
from django.http import HttpResponse, get_host


SETTINGS = getattr(settings, "SITE_ACCESS_SETTINGS", {})


class BasicAuthMiddleware(object):

    def process_request(self, request):
        if get_host(request).startswith(SETTINGS["basic-auth"]["domain"]):
            return self.process_auth(request, SETTINGS["basic-auth"]["realm"])

    def process_auth(self, request, realm):
        if "HTTP_AUTHORIZATION" in request.META:
            auth_method, auth = request.META["HTTP_AUTHORIZATION"].split(" ", 1)
            if "basic" == auth_method.lower():
                auth = auth.strip().decode("base64")
                username, password = auth.split(":", 1)
                if username == SETTINGS["basic-auth"]["username"] and password == SETTINGS["basic-auth"]["password"]:
                    return None
        response = HttpResponse("Authorization Required", mimetype="text/plain")
        response.status_code = 401
        response["WWW-Authenticate"] = 'Basic realm="%s"' % realm
        return response
