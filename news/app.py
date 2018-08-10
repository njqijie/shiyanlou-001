from flask import Flask, render_template, abort
import os,json

app = Flask(__name__)
app.config['TEMPLATS_AUTO_RELOAD'] = True

files_list = os.listdir('/home/shiyanlou/files')
files_dict = {}
for files in files_list:
    with open('/home/shiyanlou/files/'+files) as f:
        filename = files.split('.')[0] 
        files_dict[filename] = json.loads(f.read())

@app.route('/')
def index():
    return render_template('index.html', files_list = files_list)


@app.route('/files/<filename>')
def file(filename):
    if filename not in files_dict:
        abort(404) 
    return render_template('file.html', filename=filename, files_dict = files_dict)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=3000)
