# standard
import random
import string
from wsgiref.simple_server import make_server


def app(environ, start_response):
    # status code
    status_code = '200 OK'
    # headers
    headers = [
        ('Content-type', 'text/plain; charset=utf-8')
    ]

    # body
    chars = string.digits + string.ascii_letters
    random_string = ''.join(random.choices(chars, k=40))
    response_body = 'this is random string: {}'.format(random_string).encode('utf8')

    start_response(status_code, headers)
    # now return response body:
    return [response_body]


if __name__ == '__main__':
    # host
    host = 'localhost'
    # port
    port = 5000
    # create simple server from host, port and callable app
    httpd = make_server(host, port, app)
    try:
        print('serving on {}:{}'.format(host, port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('server closed.')
