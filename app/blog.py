
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers import Article, Tester



class Nothing:
    pass
        

def main():
    app = webapp.WSGIApplication([('/',         Nothing),
                                  ('/article',  Article),
                                  ('/test',     Tester)],
                                 debug=True)
    run_wsgi_app(app)


if __name__ == "__main__":
    main()

