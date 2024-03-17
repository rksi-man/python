from flask import Flask, request, render_template
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    files_path = 'file_upload_flask/uploaded_files/'
    list_files = os.listdir(files_path)
    list_excel = []
    # Проверка и отбор только файлов .xlsx
    for i in list_files:
        if i.endswith('.xlsx'):
            list_excel.append(i)
    return render_template('home.html', list_excel=list_excel)
    # return list_excel


@app.route('/document/<name>')
def document(name):
    xls = pd.ExcelFile(f'file_upload_flask/uploaded_files/{name}')
    # data_frame_dict = {}
    return f'{xls.sheet_names}'


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