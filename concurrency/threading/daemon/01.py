import threading
import psutil  # برای دریافت اطلاعات سیستم مانند حافظه استفاده می‌شود
import time

def consume_system_resources():
    for i in range(50):
        # انجام عملیات مصرفی منابع سیستم
        for j in range(1000000):
            _ = j * j

def print_system_resources():
    # استفاده از شرط بی‌پایان برای نمایش مصرف منابع تا ابد
    while True:
        # نمایش مقدار مصرفی منابع سیستم
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory_percent = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_percent}% \t| Memory Usage: {memory_percent}%")

def main():
    # ایجاد یک نخ غیر دیمون برای مصرف منابع سیستم
    resource_consumer_thread = threading.Thread(target=consume_system_resources)
    resource_consumer_thread.start()

    # ایجاد یک نخ دیمون برای نمایش مصرف منابع سیستم
    resource_printer_thread = threading.Thread(target=print_system_resources)
    resource_printer_thread.daemon = True
    resource_printer_thread.start()

    # سه ثانیه توقف برای نمایش میزان مصرف منابع در این ۳ ثانیه
    # time.sleep(3)

if __name__ == "__main__":
    main()
