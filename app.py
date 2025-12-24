from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.join(os.getcwd(), 'articles')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@app.route('/')
def index():
  return send_from_directory(BASE_DIR, 'nav.html')

# -----------
@app.route('/favicon.ico')
def favicon():
  return send_from_directory(STATIC_DIR, 'favicon.ico')

@app.route('/apple-touch-icon.png')
def apple_touch_icon():
  return send_from_directory(STATIC_DIR, 'apple-touch-icon.png')

@app.route('/icons/<path:fname>')
def icons(fname):
  return send_from_directory(os.path.join(STATIC_DIR, 'icons'), fname)

@app.route('/manifest.json')
def manifest():
  return send_from_directory(STATIC_DIR, 'manifest.json')

# -----------
@app.route('/html/<path:filename>')
def serve_article(filename):
  return send_from_directory(os.path.join(BASE_DIR, 'html'), filename)

@app.route('/styles/<path:filename>')
def serve_styles(filename):
  return send_from_directory(os.path.join(BASE_DIR, 'styles'), filename)
# -----------

if __name__ == '__main__':
  print("Blog running at http://127.0.0.1:3000")
  app.run(debug=True, port=3000)
