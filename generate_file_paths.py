import os

repo_owner = 'myseil'
repo_name = 'BingWallpaper'
base_url = f'https://cdn.jsdelivr.net/gh/{repo_owner}/{repo_name}/BingImage'

def generate_file_paths():
    paths = []
    # 遍历 BingImage 目录
    for root, _, files in os.walk('BingImage'):
        for file in files:
            if not file.endswith('.jpg'):
                continue
            # 获取文件夹名称（日期）
            date = os.path.basename(root)
            # 拼接 CDN 链接
            file_path = f'{base_url}/{date}/{file}'
            paths.append(file_path)
    return paths

def write_file_paths_to_php(paths):
    """
    将路径列表写入 data.php，格式为 PHP return 数组
    """
    with open('data.php', 'w', encoding='utf-8') as f:
        f.write("<?php\n")
        f.write("// data.php - 自动生成的文件，请勿手动大规模修改\n")
        f.write("return [\n")
        
        for path in paths:
            # 每行缩进 4 个空格，包裹双引号并加逗号
            f.write(f'    "{path}",\n')
            
        f.write("];\n")

if __name__ == '__main__':
    print("正在扫描目录并生成链接...")
    paths = generate_file_paths()
    
    if paths:
        write_file_paths_to_php(paths)
        print(f"成功！已将 {len(paths)} 个链接写入 data.php")
    else:
        print("未发现 .jpg 文件，请检查 BingImage 目录是否存在。")
