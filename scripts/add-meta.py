import os

def add_meta_tags():
  html_dir = 'articles/html'
  head_tags = [
    '<link rel="icon" href="/favicon.ico" type="image/x-icon">',
    '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
    '<link rel="manifest" href="/manifest.json">'
  ]
  tags = "\n".join(head_tags)

  if not os.path.exists(html_dir):
    print("HTML directory not found.")
    return

  for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
      file_path = os.path.join(html_dir, filename)

      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

      # Inject inside <head>
      if '<head>' in content:
        new_content = content.replace('<head>', f'<head>\n  {tags}')
      else:
        # Fallback if <head> is missing: prepend to top
        new_content = f"{tags}\n{content}"

      with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

      print(f"Meta added to: {filename}")

if __name__ == "__main__":
  add_meta_tags()
