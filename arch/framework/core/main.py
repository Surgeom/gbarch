class NotFoundPage:
    def __call__(self, request):
        print(request)
        return '404 Not Found', '404 page not found'


def parse_input_data(data: str):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env):
    content_length_data = env.get('CONTENT_LENGTH')
    content_length = int(content_length_data) if content_length_data else 0
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        data_str = data.decode(encoding='utf-8')
        result = parse_input_data(data_str)
    return result


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        # add /
        if not path.endswith('/'):
            path = f'{path}/'
        method = environ['REQUEST_METHOD']
        request = {}
        request['method'] = method
        if method == 'GET':
            if path in self.routes:
                controller = self.routes[path]
                query_string = environ['QUERY_STRING']
                request_params = parse_input_data(query_string)
                request['request_params'] = request_params
            else:
                controller = NotFoundPage()

            for front in self.fronts:
                front(request)
        elif method == "POST":
            data = get_wsgi_input_data(environ)
            data = parse_wsgi_input_data(data)
            request["data"] = data
            controller = self.routes[path]
        else:
            controller = NotFoundPage()

        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
