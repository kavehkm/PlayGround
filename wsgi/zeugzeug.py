# standard
import random
import string
from wsgiref.simple_server import make_server
# werkzeug
from werkzeug.wrappers import Request, Response


def app(environ, start_response):
    # create request object from environ dict
    request = Request(environ)
    # get len of random string from args: default 40
    len = int(request.args.get('len', 40))
    # create random string
    chars = string.digits + string.ascii_letters
    random_string = ''.join(random.choices(chars, k=len))
    # create response object
    response = Response(random_string, mimetype='text/plain')
    # return
    return response(environ, start_response)


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    httpd = make_server(host, port, app)
    try:
        print('serving on {}:{}'.format(host, port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('server closed.')
