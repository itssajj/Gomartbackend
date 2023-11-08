from django.middleware.csrf import get_token

class PublicAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            # Skip CSRF checks for URLs starting with "/api/"
            response = self.get_response(request)
            get_token(request)  # This sets the CSRF token for the response
            return response
        return self.get_response(request)
