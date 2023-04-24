import os

repo_owner = 'myseil'
repo_name = 'BingWallpaper'
base_url = f'https://cdn.jsdelivr.net/gh/{repo_owner}/{repo_name}/BingImage'

def generate_file_paths():
    paths = []
    for root, _, files in os.walk('BingImage'):
        for file in files:
            if not file.endswith('.jpg'):
                continue
            date = os.path.basename(root)
            file_path = os.path.join(base_url, date, file)
            paths.append(file_path)
    return paths

def write_file_paths_to_txt(paths):
    with open('file_paths.txt', 'w') as f:
        for path in paths:
            f.write(f'{path}\n')

if __name__ == '__main__':
    paths = generate_file_paths()
    write_file_paths_to_txt(paths)
