from app_lr8 import models, controllers
from jinja2 import Environment, PackageLoader, select_autoescape

from http.server import HTTPServer, BaseHTTPRequestHandler

env = Environment(loader=PackageLoader("app_lr8"))

# Layout
template_1 = env.get_template("layout.html")

# Zhukov info
# -----------------------------------------
u1 = models.UserZhukov()
f_n = u1.get_fullname()

page = template_1.render(the="there",
                         go="Bulma",
                         first_name=f_n.get('first_name', "Not Defined"),
                         second_name=f_n.get('second_name', "Not Defined"),
                         fathers_name=f_n.get('fathers_name', "Not Defined"))
# -----------------------------------------

# Extended layout
template_2 = env.get_template("extended_layout.html")

# Stecuk info
# -----------------------------------------
u2 = models.UserStecuk()
f_n_2 = u2.get_fullname()
d_b = u2.get_b_date()
lang = u2.get_f_lan()

page_2 = template_2.render(the="there",
                           go="Bulma",
                           first_name=f_n_2.get('first_name', "Not Defined"),
                           second_name=f_n_2.get('second_name', "Not Defined"),
                           fathers_name=f_n_2.get('fathers_name', "Not Defined"),
                           birth_date=f'{d_b}',
                           language=f'{lang}')
# -----------------------------------------

# Json data
# -----------------------------------------
json_data_ZN = controllers.StoreUserController(f_n['first_name'], f_n['second_name'], f_n['fathers_name'])

json_data_SM = controllers.StoreUserController(f_n_2['first_name'], f_n_2['second_name'], f_n_2['fathers_name'], d_b, lang)
# -----------------------------------------

# Заглушка
# -----------------------------------------
plug_temp = env.get_template("plug_layout.html")

# -----------------------------------------

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.my_main_path()
        elif self.path == '/zhukov':
            self.zhukov_path()
        elif self.path == '/jsonZN':
            self.JSON_path_ZN()
        elif self.path == '/jsonSM':
            self.JSON_path_ST()
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(plug_temp.render(), 'utf-8'))

    def zhukov_path(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(page, 'utf-8'))

    def my_main_path(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(page_2, 'utf-8'))

    def JSON_path_ST(self):
      self.send_response(200)
      self.send_header('Content-Type', 'application/json; charset=utf-8')
      self.end_headers()
      self.wfile.write(bytes(json_data_SM, 'utf-8'))

    def JSON_path_ZN(self):
      self.send_response(200)
      self.send_header('Content-Type', 'application/json; charset=utf-8')
      self.end_headers()
      self.wfile.write(bytes(json_data_ZN, 'utf-8'))


if __name__ == '__main__':

    httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()
