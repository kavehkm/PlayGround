# werkzeug
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request, Response


class View(object):
    """View"""
    def __init__(self):
        self.database = {
            'posts': ['post{}'.format(i) for i in range(1, 11)],
            'categories': ['category{}'.format(i) for i in range(1, 6)],
            'tags': ['tag{}'.format(i) for i in range(1, 21)]
        }

    @staticmethod
    def _render_result(title, items=()):
        res = '{}:<br>'.format(title)
        for i, item in enumerate(items, 1):
            res += '{}: {}<br>'.format(i, item)
        return Response(res.strip('<br>'), mimetype='text/html')

    def home(self, request):
        return self._render_result('welcome to home page')

    def posts(self, requst):
        return self._render_result('all posts', self.database.get('posts', []))

    def categories(self, request):
        return self._render_result('all categories', self.database.get('categories', []))

    def tags(self, request):
        return self._render_result('all tags', self.database.get('tags', []))


class Blog(object):
    """Blog"""
    def __init__(self):
        # view
        self.view = View()
        # routes
        self._url_map = Map([
            Rule('/', endpoint='home'),
            Rule('/posts', endpoint='posts'),
            Rule('/categories', endpoint='categories'),
            Rule('/tags', endpoint='tags'),
        ])

    def dispatch(self, request):
        adapter = self._url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self.view, endpoint)(request, **values)
        except HTTPException as e:
            return e

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
    # run server
    run_simple(host, port, create_app(), use_debugger=True)
