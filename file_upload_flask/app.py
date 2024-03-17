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
    sheet_names = xls.sheet_names
    # return f'{xls.sheet_names}'
    return render_template('document.html', name=name,sheet_names=sheet_names)


@app.route('/document/<name>/sheet/<list>')
def get_sheet(name,list):
    files_path = 'file_upload_flask/uploaded_files/'
    xls = pd.ExcelFile(f'file_upload_flask/uploaded_files/{name}')
    data_frame_dict = {}
    for sheet_name in xls.sheet_names:
        data_frame_dict[sheet_name] = pd.read_excel(xls, sheet_name, index_col=0)

    df = data_frame_dict[list]
    return df.to_html(header="true", table_id="table")
    # return f'Путь {name}/{list}'



@app.route('/upload', methods=['GET','POST'])
def upload():
    # Отлавливаем POST запрос
    if request.method == 'POST':
        # Сохраняем в переменную файл request.files['file']
        uploaded_file = request.files['file']
        # 
        pass_from_client = request.form['pass']
        admin_password = '88888888'
        if pass_from_client == admin_password:
            # 
            # Сохраняем файл с его же именем uploaded_file.filename
            # В папку file_upload_flask/uploaded_files/
            uploaded_file.save('file_upload_flask/uploaded_files/'+uploaded_file.filename)
            # Сообщаем пользователю что файл сохранен
            return 'Файл сохранен!'
        else:
            return 'Пароль не верный!'
    # Этот return срабатывает на запросах
    # не POST, соответсвтенно только в GET
    return render_template('upload.html')

app.run(debug=True)