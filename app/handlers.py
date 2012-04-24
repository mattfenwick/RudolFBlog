
import os
from google.appengine.ext.webapp import template
from django.utils import simplejson
from google.appengine.ext import db
from google.appengine.ext import webapp


articles = {
    'libraries': 'libraries.html',
    'mysqlbig': 'mysql_big_data.html'
}


class Article(webapp.RequestHandler):
  def get(self):
    # get the article name from the request
    id = self.request.get('id')
    name = articles[id]
    path = os.path.join(os.path.dirname(__file__), name)
    self.response.out.write(template.render(path, {}))
