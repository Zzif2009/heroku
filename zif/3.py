from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def name():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    spis = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
            "Присоединяйся!"]
    return "<br/>".join(spis)


@app.route("/image_mars")
def image_mars():
    image = url_for('static', filename='img/scale_1200.webp')
    return f"""<!doctype html>
                <html lang='en'>
                    <head>
                        <meta charset-'utf-8'>
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1><br/>
                        <img src='{image}' alt='здесь должна была быть картинка'></img><br/>
                        <div>Вот какая, она красная планета</div>
                    </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    image = url_for('static', filename='img/scale_1200.webp')
    href = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity = "sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
    content = "width=device-width, initial-scale=1, shrink-to-fit=no"
    return f"""<!doctype html>
                    <html lang='en'>
                        <head>
                            <meta charset-'utf-8'>
                            <meta name='viewport' content='{content}'>
                            <link rel='stylesheet' href='{href}' integrity='{integrity}' 
                            crossorigin='anonymous'>
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Привет, Марс!</title>
                        </head>
                        <body>
                            <h1 class='Hello'>Жди нас, Марс!</h1><br/>
                            <img src='{image}' alt='здесь должна была быть картинка'></img>
                            <br/><br/>
                            <div class="alert alert-secondary" role="alert">
                                Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Присоединяйся!
                            </div>
                        </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" 
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/
                            4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/
                            Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронафтов</title>
                          </head>
                          <body>
                            <h1 style='padding-left: 21cm'>Анкета претендента</h1><br> 
                            <div style='padding-left: 23cm'>на участии в мисии</div><br>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" 
                                    aria-describedby="nameHelp" 
                                    placeholder="Введите имя" name="name"><br>
                                    <input type="surename" class="form-control" id="surename" 
                                    aria-describedby="surenameHelp" 
                                    placeholder="Введите фамилию" name="surename"><br><br>
                                    <input type="email" class="form-control" 
                                    id="email" aria-describedby="emailHelp" 
                                    placeholder="Введите адркс почты" name="email"><br><br>
                                    <div class="form-group">
                                        <label for="educationSelect">
                                        Какое у вас образовние?</label><br>
                                        <select class="form-control" id="educationSelect" 
                                        name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div><br>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            гляциолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            инженер жизнеобеспечения
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            оператор марсохода
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            пилот дронов
                                          </label>
                                        </div>  
                                    </div><br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" 
                                          id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" 
                                          id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="about">
                                        Почему вы хотите принять участие в мисии?</label>
                                        <textarea class="form-control" id="about" rows="3" 
                                        name="about"></textarea>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label><br>
                                        <input type="file" class="form-control-file" id="photo" 
                                        name="file">
                                    </div><br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" 
                                        id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">
                                        Готов остаться на Марсе?</label>
                                    </div><br>
                                    <button type="submit" class="btn btn-primary">
                                    Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surename'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['job'])
        print(request.form['education'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
