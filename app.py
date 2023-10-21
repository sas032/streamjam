from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.config['MEDIA_FOLDER'] = 'media'

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/media/<media_type>')
def media_list(media_type):
    media_folder = os.path.join(app.config['MEDIA_FOLDER'], media_type)
    media_list = []
    if os.path.exists(media_folder):
        media_list = [f for f in os.listdir(media_folder) if os.path.isfile(os.path.join(media_folder, f))]
    return render_template('media_list.html', media_type=media_type, media_list=media_list)

@app.route('/media/play/<media_type>/<media_name>')
def media_player(media_type, media_name):
    return render_template('media_player.html', media_type=media_type, media_name=media_name)

@app.route('/media_files/<media_type>/<media_name>')
def media_files(media_type, media_name):
    media_folder = os.path.join(app.config['MEDIA_FOLDER'], media_type)
    return send_from_directory(media_folder, media_name)

@app.route('/media_inter/<media_type>/<media_name>')
def media_inter(media_type, media_name):
    return render_template('media_inter.html', media_type=media_type, media_name=media_name)

@app.route('/test')
def test():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

