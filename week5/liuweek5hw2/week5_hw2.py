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


class GUIDE(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('guide.html')
        self.response.out.write(template.render())
        start = self.request.get("from")
        end = self.request.get("to")
        url = 'http://test-mojo.appspot.com/net?format=json'
        output = json.load(urllib.urlopen(url))
        for i in output: # i is a dict
            for j in i["Stations"]:
                if j == start:
                    self.response.write('from: %s[%s]' % (start, i["Name"]))
                    break
        for i in output: # i is a dict
            for j in i["Stations"]:
                if j == end:
                    self.response.write(' to: %s[%s],<br>' % (end, i["Name"]))
                    break
        now = datetime.now()
        self.response.write('<br> Starting at >> %s' % (start)) # utc time + 9 hours = JP time
        self.response.write('@ %s-%s-%s %s:%s:%s JST <br>'% (now.year, now.month, now.day, now.hour + 9, now.minute, now.second))

app = webapp2.WSGIApplication([
    ('/', HW2),
    ('/guidance?',GUIDE),
], debug=True)
