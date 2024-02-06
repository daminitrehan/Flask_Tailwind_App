# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Set the domain name (replace 'yourdomain.com' with your actual domain)
app.config['SERVER_NAME'] = 'daminitrehan.com'

@app.route('/')
def home():
    tabs = [
        {'id': 'about', 'label': 'About Me', 'content': 'I am a passionate developer with a strong background in...'},
        {'id': 'projects', 'label': 'Projects', 'content': 'Here are some of the projects I\'ve worked on...'},
        {'id': 'contact', 'label': 'Contact', 'content': 'Feel free to reach out to me at...'}
    ]
    return render_template('index.html', tabs=tabs)

if __name__ == '__main__':
    app.run(debug=True)
