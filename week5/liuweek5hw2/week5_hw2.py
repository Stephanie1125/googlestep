import os
import webapp2
import jinja2
import json
import urllib
from datetime import datetime
# import pytz
# Failed to set up library pytz for GAE: ImportError: No module named pytz

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
        output = json.load(urllib.urlopen(url))  # output is a list

        for dictionary in output:
            for station_index in xrange(len(dictionary["Stations"])):
                if dictionary["Stations"][station_index] == start:
                    start_dict = dictionary
                    start_line = start_dict["Name"]
                    start_index = station_index
                if dictionary["Stations"][station_index] == end:
                    end_dict = dictionary
                    end_line = end_dict["Name"]
                    end_index = station_index

        self.response.write('from %s[%s] %d to %s[%s] %d' % (start, start_line, start_index, end, end_line, end_index))

        now = datetime.now()
        self.response.write('<br> Starting at: %s' % start)  # utc time + 9 hours = JP time
        self.response.write('@ %s-%s-%s ' % (now.year, now.month, now.day))
        self.response.write(' %s:%s:%s JST <br>' % (now.hour + 9, now.minute, now.second))

        if start_line == end_line:
            if start_index > end_index:
                for station in start_dict["Stations"][start_index:end_index + 1]:
                    self.response.write(' >> %s' % station)
            for station in start_dict["Stations"][start_index:end_index - 1:-1]:
                self.response.write(' >> %s' % station)

app = webapp2.WSGIApplication([
    ('/', HW2),
    ('/guidance?', GUIDE),
], debug=True)
