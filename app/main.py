import tornado.web
import tornado.ioloop

def applicationInit():
    return tornado.web.Application([
        (r"/", staticRequestHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': './app', 'default_filename': 'index.html'}),
        (r"/loginesenha", LoginHandler)
    ])

class staticRequestHandler(tornado.web.RequestHandler):
    async def get(self):
        await self.render('index.html')

class BaseHandler(tornado.web.RequestHandler):
    def get_current_login(self):
        return self.get_secure_cookie("login")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/paginaedicao.html")
            return

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" id="login">'
                   '<input type="submit" value="Enviar">'
                   '</form></body></html>')

    def post(self):
        print("teste")
        self.set_secure_cookie("login", self.get_argument("senha"))
        self.redirect("/paginaedicao.html")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/paginaedicao", LoginHandler)
])

if __name__ == "__main__":
    app = applicationInit()
    app.listen(8000)
    print('Na porta 8000')
    tornado.ioloop.IOLoop.current().start()

