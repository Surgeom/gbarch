class NotFoundPage:
    def __call__(self, request):
        print(request)
        return '404 Not Found', '404 page not found'


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
            else:
                controller = NotFoundPage()

            for front in self.fronts:
                front(request)
        elif method == "POST":
            controller = NotFoundPage()

        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
