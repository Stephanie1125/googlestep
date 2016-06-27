#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
    def get_line(self, target):
        """
        find the set of lines where the target station is located
        target: station(string)
        return: set
        """
        station_line = set([])
        url = 'http://test-mojo.appspot.com/net?format=json'
        output = json.load(urllib.urlopen(url))
        for dictionary in output:
            for station in dictionary['Stations']:  # build station and line's set
                if station == target:
                    station_line.add(dictionary['Name'])
        return station_line

    def get_dict(self, line):  # return a diction where the line is
        url = 'http://test-mojo.appspot.com/net?format=json'
        output = json.load(urllib.urlopen(url))
        for dictionary in output:
            if dictionary['Name'] == line:
                return dictionary

    def get_index(self, target, list):  # return index
        for index in xrange(len(list)):
            if list[index] == target:
                return index

    def check_station(self, start, end):  # check if two station are in the same line
        start_set = self.get_line(start)
        end_set = self.get_line(end)
        intersection_set_lst = [str(item) for item in (start_set & end_set)]
        return intersection_set_lst

    def check_line(self, curr_lines, dest):
        for line in curr_lines:
            if dest in self.get_dict(line)["Stations"]:
                return True
        return False

    def adjunt_line(self, line):
        line_set = set()
        line_dictionary = self.get_dict(line)
        for station in line_dictionary['Stations']:
            for line in self.get_line(station):
                line_set.add(line)
        return line_set  # return a set with intersection line

    def intersection_station(self, line_a, line_b):
        dictionary_a = self.get_dict(line_a)
        dictionary_b = self.get_dict(line_b)
        set_a = set()
        set_b = set()
        for station in dictionary_a['Stations']:
            set_a.add(station)
        for station in dictionary_b['Stations']:
            set_b.add(station)
        intersection_station = [str(item) for item in (set_a & set_b)]
        return intersection_station  # a list of station

    def get(self):
        # get start and end
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('guide.html')
        self.response.out.write(template.render())
        start = self.request.get("from")
        end = self.request.get("to")
        start_line_str = '/'.join([str(item) for item in self.get_line(start)])
        end_line_str = '/'.join([str(item) for item in self.get_line(end)])
        self.response.write('from %s[%s] to %s[%s]<br>' % (start, start_line_str, end, end_line_str))
        # calculate path


        curr_lines = self.get_line(start)
        count = 0
        # while not self.check_line(curr_lines, end):
        #     next_lines = set()
        #     for line in curr_lines:
        #         next_lines += self.adjunt_line(line)
        #     curr_lines = next_lines
        #     count += 1
        #
        #

            # start_set_line = self.get_line(start)
            # start_list = []
            # for line in start_set_line:
            #     start_list.append(self.adjunt_line(line))
            # end_set_line = self.get_line(end)

    #     intersection_line = (self.get_line(start) & self.get_line(end))
    #     self.print_path(end, intersection_line, start) # if in the same line
    # def print_path(self, end, intersection_line, start):
    #     now = datetime.now()
    #     self.response.write('<br> Starting at: %s' % start)  # utc time + 9 hours = JP time
    #     self.response.write('@ %s-%s-%s ' % (now.year, now.month, now.day))
    #     self.response.write(' %s:%s:%s JST <br>' % (now.hour + 9, now.minute, now.second))
    #     for line in intersection_line:
    #         start_index = self.get_index(start, self.get_dict(line)['Stations'])
    #         end_index = self.get_index(end, self.get_dict(line)['Stations'])
    #         if start_index < end_index:
    #             for station in self.get_dict(line)['Stations'][start_index:end_index + 1]:
    #                 self.response.write('>> %s <br>' % station)
    #         else:
    #             for station in self.get_dict(line)['Stations'][end_index:start_index + 1]:
    #                 self.response.write('>> %s' % station)

app = webapp2.WSGIApplication([
    ('/', HW2),
    ('/guidance?', GUIDE),
], debug=True)
