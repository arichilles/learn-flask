from wsgiref.simple_server import make_server

def application(environ, start_response):
  body = "hello WSGI".encode('utf-16')
  status = '200 OK'
  headers = [('Content-Type:','text/html'), ('Content-Length', str(len(body)))]
  start_response(status, headers)
  return [body]


if __name__ == "__main__":
  server = make_server('localhost',5000,application)
  server.serve_forever()
