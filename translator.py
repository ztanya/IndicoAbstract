# -*- coding: utf-8 -*-

import httplib
import urllib2
import simplejson as json
import sys

user_agent = 'Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.0.4) Gecko/2008120916 Gentoo Firefox/3.0.4'


def translate_handler(lang, body):
    body = ' '.join(body)
    #if len(sys.argv) < 2: print u'$ en/ru text'; return
    try:
        if lang == 'ru':
            req = urllib2.Request(unicode(
                u'http://ajax.googleapis.com/ajax/services/language/translate?v=2.0&q=%s&langpair=%s' % (
                urllib2.quote(body), u'en%7Cru')), 'utf-8')
        elif lang == 'en':
            req = urllib2.Request(unicode(
                u'http://ajax.googleapis.com/ajax/services/language/translate?v=2.0&q=%s&langpair=%s' % (
                urllib2.quote(body), u'ru%7Cen')), 'utf-8')
        elif lang == 'en':
            print str(unicode(body, 'utf-8'))
        else:
            print u'Available languages: en, ru'; return
        req.add_header('User-Agent', user_agent)
        reqf = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print str(e)
    answ = json.load(reqf)
    if answ['responseStatus'] != 200:
        print str(answ['responseStatus']) + ': ' + answ['responseDetails']
    elif answ['responseData']:
        print answ['responseData']['translatedText']
    else:
        print u'unknown error >_<'


translate_handler("en", "Hello")