
from webob import Request, Response

class API:

	def __init__(self):
		self.routes = {}

	def __call__(self, environ, start_response):
		
		request = Request(environ)
		
		response = self.handle_request(request)

		return response(environ, start_response)

		# response_body = b"Hello, World!"
		# status = "200 ok"
		# start_response(status, headers=[])
		# return iter([response_body])

	def handle_request(self, request):
		response = Response()

		for path, handler in self.routes.items():
			if path == request.path:
				handler(request, response)
				return response



		self.default_response(response)
		return response

	def route(self, path):
		def wrapper(handler):
			self.routes[path] = handler
			return handler
		return wrapper

	def default_response(self, response):
		response.status_code = 404
		response.text = "Not found."

