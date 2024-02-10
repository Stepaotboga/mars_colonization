from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_f():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.</br>\
    Человечеству мала одна планета.</br>\
    Мы сделаем обитаемыми безжизненные пока планеты.</br>\
    И начнем с Марса!</br>\
    Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return f'''Жди нас, Марс!</br>
    <img src="{url_for('static', filename='img/mars_photo.png')}" 
           alt="здесь должна была быть картинка, но не нашлась"></br>
    Красная планета'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class="h1">Жди нас, Марс!</h1></br>
                    <img src="{url_for('static', filename='img/image_mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась"></br>
                    <div1 class="div1">Человечество вырастает из детства.</div1></br>
                    <div2 class="div2">Человечеству мала одна планета.</div2></br>
                    <div3 class="div3">Мы сделаем обитаемыми планеты</div3></br>
                    <div4 class="div4">И начнем с марса!</div4></br>
                    <div5 class="div5">Присоединяйся!</div5>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
