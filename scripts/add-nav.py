import os

def add_navigation_header():
  html_dir = 'articles/html'
  # Link back to the root nav.html (via the Flask route or relative path)
  nav_link = '<nav class="top-nav"><a href="/">&larr; Back to Contents</a></nav>'

  if not os.path.exists(html_dir):
    print("HTML directory not found.")
    return

  for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
      file_path = os.path.join(html_dir, filename)

      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

      # Avoid double injection
      if 'class="top-nav"' in content:
        continue

      # Inject right after <body> tag
      if '<body>' in content:
        new_content = content.replace('<body>', f'<body>\n  {nav_link}')
      else:
        # Fallback if <body> is missing
        new_content = f"{nav_link}\n{content}"

      with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

      print(f"Nav header added to: {filename}")

if __name__ == "__main__":
  add_navigation_header()
