
# api/index.py
import json
from http.server import BaseHTTPRequestHandler
import urlib.parse

file_path='api/q-vercel-python.json'
with open (file_path,'r') as file:
    data=json.load(file)

marks = dict()
 for i in range (len(data)):
     marks[data[i]['name']] = data[i]['marks']


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = url.lib.parse.urlparse(self.path)
        query_params = url.lib.parse.parse_qs(parsed_url.query)
        names = query_params.get('name',[])

        query_marks = list ()
        for n in names:
            query_marks.append(marks[n])

        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers("Access-Control-Allow-Origin", "*")
        self.end_headers()

        response = {
            "marks":query_marks,
        }
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return