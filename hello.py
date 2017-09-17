def hello(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))])
	return [bytes("\n".join(environ.get('QUERY_STRING').split('&')), encoding="utf8")]
