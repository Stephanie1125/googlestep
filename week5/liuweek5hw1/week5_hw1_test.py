
import week5_hw1
import webtest

def test():
    app = webtest.TestApp(week5_hw1.app)
    # test same length
    resp1 = app.get('/?a=123&b=456')
    assert resp1.status_int == 200
    assert resp1.content_type == 'text/html'
    assert resp1.body.contains('142536')
    # test len(a)>len(b)
    resp2 = app.get('/?a=12345&b=67')
    assert resp2.status_int == 200
    assert resp2.content_type == 'text/html'
    assert resp2.body.contains('1627345')
    # test len(b)>len(a)
    resp3 = app.get('/?a=12&b=34567')
    assert resp3.status_int == 200
    assert resp3.content_type == 'text/html'
    assert resp3.body.contains('1324567')

