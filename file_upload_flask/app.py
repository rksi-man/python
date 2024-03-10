from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    # Отлавливаем POST запрос
    if request.method == 'POST':
        # Сохраняем в переменную файл request.files['file']
        uploaded_file = request.files['file']
        # Сохраняем файл с его же именем uploaded_file.filename
        # В папку file_upload_flask/uploaded_files/
        uploaded_file.save('file_upload_flask/uploaded_files/'+uploaded_file.filename)
        # Сообщаем пользователю что файл сохранен
        return 'Файл сохранен!'
    # Этот return срабатывает на запросах
    # не POST, соответсвтенно только в GET
    return render_template('upload.html')

app.run(debug=True)