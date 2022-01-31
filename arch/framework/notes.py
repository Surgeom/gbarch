# def index_page(request):
#     print(request)
#     return '200 OK', b'Hello world!'
#
#
# def about_page(request):
#     print(request)
#     return '200 OK', b'about'
#
#
# # def not_found_page():
# #     return '404 Not Found', b'404 page not found'
#
#
# class NotFoundPage:
#     def __call__(self, request):
#         print(request)
#         return '404 Not Found', b'404 page not found'
#
#
# routes = {
#     "/": index_page,
#     '/about': about_page
# }
#
#
# # def application(environ, start_response):
# #     path = environ['PATH_INFO']
# #     if path in routes:
# #         controller = routes[path]
# #     else:
# #         controller = NotFoundPage()
# #     code, body = controller()
# #     start_response(code, [('Content-Type', 'text/html')])
# #
# #     return [body]
#
# def secret_front(request):
#     request['secret'] = 'some secret'
#
#
# def other_front(request):
#     request['key'] = 'value'
#
#
# class Application:
#     def __init__(self, routes, fronts):
#         self.routes = routes
#         self.fronts = fronts
#
#     def __call__(self, environ, start_response):
#         path = environ['PATH_INFO']
#         if path in self.routes:
#             controller = self.routes[path]
#         else:
#             controller = NotFoundPage()
#
#         request = {}
#         for front in self.fronts:
#             front(request)
#
#         code, body = controller(request)
#         start_response(code, [('Content-Type', 'text/html')])
#
#         return [body]
#
#
# application = Application(routes, [secret_front, other_front])
