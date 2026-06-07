import http.server, os
os.chdir("/Users/sinj/Desktop/Scheduling software")
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 3456), handler)
httpd.serve_forever()
