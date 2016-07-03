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

url = 'http://test-mojo.appspot.com/net?format=json'
output = json.load(urllib.urlopen(url))


class HW2(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('train.html')
        self.response.out.write(template.render())


class GUIDE(webapp2.RequestHandler):
    def get_line(self, target):
        """
        find a set of lines where the target station is located
        target: station(string)
        return: set
        example:
        target = '多摩川'
        return: set([東横線/目黒線/多摩川線])
        """
        station_line = set([])
        for dictionary in output:
            for station in dictionary['Stations']:  # build station and line's set
                if station == target:
                    station_line.add(dictionary['Name'])
        return station_line

    def get_dict(self, line):
        """
        find a dict where the line is located
        line: train line(string)
        return: dict
        example:
        line = '山手線'
        return: {"Name":"山手線","Stations":["品川","大崎","五反田","目黒","恵比寿","渋谷","原宿"...]}
        """
        for dictionary in output:
            if dictionary['Name'] == line:
                return dictionary

    def get_index(self, target, list):
        """
        return the index where the target is in a list
        """
        for index in xrange(len(list)):
            if list[index] == target:
                return index

    def check_station(self, start, end):
        """
        check if two station is in the same line
        start, end: stations(strings)
        return: intersection line (list)
        """
        start_set = self.get_line(start)
        end_set = self.get_line(end)
        intersection_set_lst = [str(item) for item in (start_set & end_set)]
        return intersection_set_lst

    def check_line(self, curr_lines, end):
        """
        check if the destination inside the current line
        return True or False
        """
        for line in curr_lines:
            if end in self.get_dict(line)['Stations']:
                return True
        return False

    def adjunt_line(self, line):
        """
        line: train line(string)
        return: intersection line (set)
        """
        line_set = set()
        line_dictionary = self.get_dict(line)
        for station in line_dictionary['Stations']:
            for line in self.get_line(station):
                line_set.add(line)
        return line_set

    def intersection_station(self, line_a, line_b):
        """
        line_a, line_b: two different line (strings)
        return intersection station (list)
        """
        dictionary_a = self.get_dict(line_a)
        dictionary_b = self.get_dict(line_b)
        set_a = set()
        set_b = set()
        for station in dictionary_a['Stations']:
            set_a.add(station)
        for station in dictionary_b['Stations']:
            set_b.add(station)
        intersection_station = [str(item) for item in (set_a & set_b)]
        return intersection_station

    def intersection_line(self, curr_line):
        """
        return a set of lines where the current line is intersection with
        curr_line: current line(string)
        return: set
        """
        current_dict = self.get_dict(curr_line)
        intersection_lines_set = set()
        for station in current_dict['Stations']:
            intersection_lines_set |= self.get_line(station)
        return intersection_lines_set

    def get(self):
        # get start and end
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('guide.html')
        self.response.out.write(template.render())
        start = self.request.get("from")
        end = self.request.get("to")
        start_line_str = '/'.join([str(item) for item in self.get_line(start)])
        end_line_str = '/'.join([str(item) for item in self.get_line(end)])
        self.response.write('<b style="color:#14B0EE"> From  </b> %s[%s]' % (start, start_line_str))
        self.response.write('<b style="color:#14B0EE"> to </b> %s[%s]' % (end, end_line_str))
        # calculate path
        self.print_path_sameline(start, end)
        self.transfer_station(end, start)

    def transfer_station(self, end, start):
        line_to_take = self.transfer_line(start, end)  #list
        path = []
        station_to_trans = {}
        for line_index in xrange(1, len(line_to_take)):
            trans_station = self.intersection_station(line_to_take[line_index - 1], line_to_take[line_index])
            station_to_trans[(line_to_take[line_index - 1],line_to_take[line_index])] = trans_station
            path.append(trans_station[0])
        if len(station_to_trans) != 0:
            # find where to transfer
            self.response.write('<b style="color:#14B0EE">Transfer Station(s): </b>')
            for line_tuple, station_list in station_to_trans.iteritems():  # line is a tuple, station is a list
                line_str = '>>'.join([str(item) for item in line_tuple])
                station_str = '/'.join([str(item) for item in station_list])
                self.response.write(' %s: %s <b style="color:#F256AF">(乗換)</b>' % (line_str, station_str))
            self.response.write('<hr>')
            # print path
            self.response.write('<b style="color:#14B0EE">You can take: </b>')
            self.response.write('<b style="color:#F256AF"> >> %s </b>' % start)
            for station in path:
                self.response.write('<b style="color:#F256AF"> >> %s (乗換) </b>' % station)
            self.response.write('<b style="color:#F256AF"> >> %s </b><br><hr>' % end)

            path.insert(0, start)
            path.append(end)

            self.response.write('<b style="color:#14B0EE">Detail: </b>')

            for index in xrange(1, len(path)):
                s, t = path[index-1], path[index]
                self.print_path(s, t)
                if t != end:
                    self.response.write('>> <b style="color:#F256AF">(乗換) </b>')

    def transfer_line(self, start, end):
        """
        return a list of lines that recommended to be taken
        """
        curr_lines = self.get_line(start)  # initial start line (set)
        count = 0  # 乗り換え times
        line_path = []
        while not self.check_line(curr_lines, end):
            line_path.append(curr_lines)
            next_lines = set()
            for line in curr_lines:
                next_lines |= self.adjunt_line(line)  # possible lines that you can connect to
            curr_lines = next_lines
            count += 1
        end_line_set = self.get_line(end)
        line_to_take = []
        end_line_to_take = ''
        for item in (end_line_set & curr_lines):
            end_line_to_take = str(item) # initial
        line_to_take.append(end_line_to_take)
        for path_set in line_path[::-1]:
            for item in (path_set & self.intersection_line(end_line_to_take)):
                end_line_to_take = str(item)
            line_to_take.append(end_line_to_take)
        line_to_take.reverse()
        if count != 0:
            self.response.write('<b style="color:#14B0EE"> Recommand to take </b>')
            for line in line_to_take:
                self.response.write(' >> %s' % line)
            self.response.write('<b style="color:#F256AF"> (乗換 %d 回) </b><br><hr>' % count)
        return line_to_take

    def print_path_sameline(self, start, end):
        """
        when start and destination staitons are on the same line (乗換なし)
        """
        intersection_line = (self.get_line(start) & self.get_line(end))
        now = datetime.now()
        self.response.write('<br> <b style="color:#14B0EE"> Starting at: </b> %s' % start)
        self.response.write('@ %s-%s-%s ' % (now.year, now.month, now.day)) # utc time + 9 hours = JP time
        self.response.write(' %s:%s:%s JST <br><hr>' % (now.hour + 9, now.minute, now.second))
        if len(intersection_line) != 0:
            intersection_line_str = ''.join([str(item) for item in intersection_line])
            self.response.write('<b style="color:#14B0EE"> Recommand to take </b> %s ' % intersection_line_str)
            self.response.write('<b style="color:#F256AF"> (乗換なし)</b> <br>' )
        self.print_path(start, end)

    def print_path(self, start, end):
        intersection_line = (self.get_line(start) & self.get_line(end))
        for line in intersection_line:
            start_index = self.get_index(start, self.get_dict(line)['Stations'])
            end_index = self.get_index(end, self.get_dict(line)['Stations'])
            if start_index < end_index:
                path = self.get_dict(line)['Stations'][start_index:end_index + 1]
                for station in path:
                    self.response.write('>> %s ' % station)
            else:
                path = self.get_dict(line)['Stations'][end_index:start_index + 1]
                path.reverse()
                for station in path:
                    self.response.write('>> %s ' % station)


app = webapp2.WSGIApplication([
    ('/', HW2),
    ('/guidance?', GUIDE),
], debug=True)
