import os

def inject_stylesheet():
  html_dir = 'articles/html'
  css_relative_path = '../styles/style.css'
  link_tag = f'<link rel="stylesheet" type="text/css" href="{css_relative_path}">'

  if not os.path.exists(html_dir):
    print("HTML directory not found.")
    return

  for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
      file_path = os.path.join(html_dir, filename)

      with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

      # Inject link tag before </head> or at the top if head is missing
      if '</head>' in content:
        new_content = content.replace('</head>', f'  {link_tag}\n</head>')
      else:
        new_content = f"{link_tag}\n{content}"

      with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

      print(f"Linked: {filename}")

if __name__ == "__main__":
  # Ensure the styles directory exists
  os.makedirs('articles/styles', exist_ok=True)
  inject_stylesheet()
