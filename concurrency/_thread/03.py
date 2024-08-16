import requests
import os
import _thread
import time
from PIL import Image
from io import BytesIO

# فهرست آدرس‌های فایل‌ها
file_urls = [f"https://dummyimage.com/{i}.png" for i in range(300, 400)]

# قفل برای دسترسی همزمان به فایل گزارش
lock = _thread.allocate_lock()

# تابع برای دانلود هر فایل
def download_file(file_url, cookies, headers):
    start_time = time.time()  # زمان شروع دانلود
    file_name = os.path.basename(file_url)  # نام فایل از آخرین بخش آدرس استخراج می‌شود
    file_path = os.path.join("downloads", file_name)  # مسیر محلی برای ذخیره فایل‌ها
    print(f"Downloading {file_name}...")
    
    # دانلود فایل با استفاده از کتابخانه requests
    response = requests.get(file_url, cookies=cookies, headers=headers)
    
    # ذخیره فایل به صورت باینری
    with open(file_path, 'wb') as f:
        f.write(response.content)
    
    end_time = time.time()  # زمان پایان دانلود
    download_time = end_time - start_time  # مدت زمان دانلود
    
    # استخراج ابعاد تصویر با استفاده از Pillow
    image = Image.open(BytesIO(response.content))
    width, height = image.size
    
    # حجم فایل به بایت
    file_size = os.path.getsize(file_path)
    
    # نوشتن اطلاعات به فایل گزارش
    with lock:
        with open("report.txt", 'a') as report:
            report.write(f"{file_name}, {file_size} bytes, {download_time:.2f} seconds, {width}x{height}\n")
    
    print(f"{file_name} downloaded successfully.")

# ایجاد پوشه downloads اگر وجود نداشته باشد
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# ایجاد یا پاک کردن محتوای قبلی فایل گزارش
with open("report.txt", 'w') as report:
    report.write("File Name, File Size, Download Time, Dimensions\n")

# شروع دانلود هر فایل به صورت همزمان با استفاده از _thread
for file_url in file_urls:
    _thread.start_new_thread(download_file, (file_url, {}, {}))

# افزودن یک تاخیر تا اطمینان حاصل شود که تمام نخ‌ها کامل شوند قبل از پایان برنامه
time.sleep(60)

print("All files downloaded successfully.")
