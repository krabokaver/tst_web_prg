def app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/plain")])
	return [bytes("\n".join(environ.get('QUERY_STRING').split('&')), encoding="utf8")]
