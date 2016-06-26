
import webapp2

class HW1(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<title>STEP2016_week5_hw1_Liu</title>')
        self.response.write('<body><h1>Please input two strings: </h1>')
        self.response.write('<form><b style="color:#F256AF">input1: </b><input type=text name=a><br>')
        self.response.write('<b style="color:#14B0EE">input2: </b><input type=text name=b><br>')
        self.response.write('<input type=submit></form><hr>')

        len_a = len(self.request.get("a"))
        len_b = len(self.request.get("b"))
        a = self.request.get("a")
        b = self.request.get("b")
        self.response.write('<h2>Output: ')

        if len_a == len_b:
            for i in xrange(len_a):
                self.response.write('<b style="color:#F256AF">%s</b><b style="color:#14B0EE">%s</b>' % (a[i],b[i]))
        elif len_a > len_b:
            for i in xrange(len_b):
                self.response.write('<b style="color:#F256AF">%s</b><b style="color:#14B0EE">%s</b>' % (a[i],b[i]))
            self.response.write('<b style="color:#F256AF">%s</b>' % a[len_b:len_a])
        else:
            for i in xrange(len_a):
                self.response.write('<b style="color:#F256AF">%s</b><b style="color:#14B0EE">%s</b>' % (a[i],b[i]))
            self.response.write('<b style="color:#14B0EE">%s</b>' % b[len_a:len_b])
        self.response.write('</h2></body>')

app = webapp2.WSGIApplication([
    ('/', HW1),
], debug=True)
