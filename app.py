from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.join(os.getcwd(), 'articles')

@app.route('/')
def index():
  return send_from_directory(BASE_DIR, 'nav.html')

@app.route('/html/<path:filename>')
def serve_article(filename):
  return send_from_directory(os.path.join(BASE_DIR, 'html'), filename)

@app.route('/styles/<path:filename>')
def serve_styles(filename):
  return send_from_directory(os.path.join(BASE_DIR, 'styles'), filename)

if __name__ == '__main__':
  print("Blog running at http://127.0.0.1:3000")
  app.run(debug=True, port=3000)
