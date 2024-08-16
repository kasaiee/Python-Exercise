import time
from tqdm import tqdm

def task(iterations):
    for i in tqdm(range(iterations)):
        # شبیه‌سازی انجام کاری که زمان می‌برد
        time.sleep(0.1)

# اجرای چهار کار به صورت ترتیبی
task(10)
task(20)
task(30)
task(40)