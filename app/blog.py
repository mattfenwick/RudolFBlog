
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers import Article



class Nothing:
    pass
        

def main():
    app = webapp.WSGIApplication([('/',         Nothing),
                                  ('/article',  Article)],
                                 debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()

