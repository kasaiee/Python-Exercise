import requests
import os
import threading

# فهرست آدرس‌های فایل‌ها
file_urls = [f"https://dummyimage.com/{i}.png" for i in range(300, 400)]

# تابع برای دانلود هر فایل
def download_file(file_url, cookies, headers):
    file_name = os.path.basename(file_url)  # نام فایل از آخرین بخش آدرس استخراج می‌شود
    file_path = os.path.join("downloads", file_name)  # مسیر محلی برای ذخیره فایل‌ها
    print(f"Downloading {file_name}...")
    # دانلود فایل با استفاده از کتابخانه requests
    response = requests.get(file_url, cookies=cookies, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"{file_name} downloaded successfully.")

# ایجاد پوشه downloads اگر وجود نداشته باشد
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# لیستی برای نگهداری نخ‌ها
threads = []

# شروع دانلود هر فایل با استفاده از نخ‌ها
for file_url in file_urls:
    # ایجاد و شروع نخ برای دانلود هر فایل
    thread = threading.Thread(target=download_file, args=(file_url, {}, {}))
    thread.start()
    threads.append(thread)

# انتظار برای پایان همه نخ‌ها
for thread in threads:
    thread.join()

print("All files downloaded successfully.")
