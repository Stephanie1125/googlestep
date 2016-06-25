import os
import webapp2
import jinja2
import json
import urllib
from datetime import datetime


JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)

class HW2(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('train.html')
        self.response.out.write(template.render())
        start = self.request.get("from")
        end = self.request.get("to")
        self.response.write('Starting at >> %s @ %s \n' % (start, datetime.now()))
        url = 'http://test-mojo.appspot.com/net?format=json'
        output = json.load(urllib.urlopen(url))
        for i in output: # i is a dict
            for j in i["Stations"]:
                if j == start:
                    self.response.write('from >> %s:%s' % (i["Name"],start))
                    break
        for i in output: # i is a dict
            for j in i["Stations"]:
                if j == end:
                    self.response.write(' to >> %s:%s' % (i["Name"], end))
                    break


app = webapp2.WSGIApplication([
    ('/', HW2),
], debug=True)
