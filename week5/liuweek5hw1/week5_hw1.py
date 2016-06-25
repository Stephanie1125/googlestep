
import webapp2

class HW1(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<title>STEP2016_week5_hw1_Liu</title>')
        self.response.write('<form><input type=text name=a><br><input type=text name=b><br><input type=submit></form>')
        len_a = len(self.request.get("a"))
        len_b = len(self.request.get("b"))
        a = self.request.get("a")
        b = self.request.get("b")
        if len_a == len_b:
            for i in xrange(len_a):
                self.response.write('%s%s' % (a[i],b[i]))
        elif len_a > len_b:
            for i in xrange(len_b):
                self.response.write('%s%s' % (a[i],b[i]))
            self.response.write('%s' % a[len_b:len_a])
        else:
            for i in xrange(len_a):
                self.response.write('%s%s' % (a[i],b[i]))
            self.response.write('%s' % b[len_a:len_b])

app = webapp2.WSGIApplication([
    ('/', HW1),
], debug=True)
