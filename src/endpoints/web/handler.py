from anillo.http import responses

class BaseHandler:
    def __call__(self, request, *args, **kwargs):
        method = request.method.lower()
        handler_func = getattr(self, method)
        if handler_func:
            return handler_func(request, *args, **kwargs)
        else:
            return responses.MethodNotAllowed()

