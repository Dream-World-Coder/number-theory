import json
import zipfile
import os
import re

def sanitize_filename(name):
  # Lowercase and replace spaces/special chars with hyphens
  name = name.lower().strip()
  name = re.sub(r'[^a-z0-9]+', '-', name)
  return name.strip('-')

def process_articles():
  json_path = 'list_line/data.json'
  zip_dir = 'articles'
  output_dir = 'articles/html'
  nav_file = 'articles/nav.html'

  # Ensure output directory exists
  os.makedirs(output_dir, exist_ok=True)

  with open(json_path, 'r') as f:
    data = json.load(f)

  nav_links = []

  for entry in data:
    article_id = entry['id']
    original_name = entry['name']

    zip_path = os.path.join(zip_dir, f'art_{article_id}.zip')
    sanitized_name = f"{sanitize_filename(original_name)}.html"
    dest_path = os.path.join(output_dir, sanitized_name)

    if os.path.exists(zip_path):
      try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
          # Extract data.html and rename it immediately
          if 'data.html' in zip_ref.namelist():
            with zip_ref.open('data.html') as source, open(dest_path, 'wb') as target:
              target.write(source.read())

            nav_links.append(f'<li><a href="html/{sanitized_name}">{original_name}</a></li>')
            print(f"Processed: {original_name}")
          else:
            print(f"Warning: data.html missing in {zip_path}")
      except zipfile.BadZipFile:
        print(f"Error: {zip_path} is corrupted.")
    else:
      print(f"File not found: {zip_path}")

  # Generate Navigation HTML
  with open(nav_file, 'w') as f:
    f.write("<!DOCTYPE html>\n<html>\n<body>\n<ul>\n")
    f.write("\n".join(nav_links))
    f.write("\n</ul>\n</body>\n</html>")

if __name__ == "__main__":
  process_articles()
