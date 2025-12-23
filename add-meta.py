import os

def add_viewport_meta():
  html_dir = 'articles/html'
  # The standard tag for responsive web design
  viewport_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

  if not os.path.exists(html_dir):
    print("HTML directory not found.")
    return

  for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
      file_path = os.path.join(html_dir, filename)

      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

      # Avoid duplicate injection
      if 'name="viewport"' in content:
        continue

      # Inject inside <head>
      if '<head>' in content:
        new_content = content.replace('<head>', f'<head>\n  {viewport_tag}')
      else:
        # Fallback if <head> is missing: prepend to top
        new_content = f"{viewport_tag}\n{content}"

      with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

      print(f"Viewport added to: {filename}")

if __name__ == "__main__":
  add_viewport_meta()
