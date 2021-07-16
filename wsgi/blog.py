# werkzeug
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response


class Blog(object):
    """Blog"""
    def __init__(self):
        pass

    def dispatch(self, request):
        return Response('Hello World', mimetype='text/plain')

    def wsgi_app(self, environ, start_response):
        # create request object from environ dict
        request = Request(environ)
        response = self.dispatch(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    app = Blog()
    return app


if __name__ == '__main__':
    # host and port
    host, port = 'localhost', 5000

    run_simple(host, port, create_app(), use_debugger=True)
