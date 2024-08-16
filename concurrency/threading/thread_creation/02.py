import threading

# تابعی برای محاسبه جمع قسمتی از لیست اعداد
def calculate_sum_partial(nums, start, end, result):
    # محاسبه جمع اعداد در قسمت مشخص شده از لیست
    partial_sum = sum(nums[start:end])
    # اضافه کردن جمع به لیست نتایج
    result.append(partial_sum)

def main():
    # لیست اعداد
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # تعداد نخ‌ها برای محاسبه موازی
    num_threads = 4
    # محاسبه اندازه هر قسمت برای هر نخ
    chunk_size = len(nums) // num_threads

    # لیستی برای نگهداری نخ‌ها
    threads = []
    # لیستی برای نگهداری نتایج جزئی
    result = []

    # ایجاد و شروع نخ‌ها
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(nums)
        # ایجاد نخ جدید با استفاده از تابع calculate_sum_partial
        thread = threading.Thread(target=calculate_sum_partial, args=(nums, start, end, result))
        threads.append(thread)
        thread.start()

    # انتظار برای پایان همه نخ‌ها
    for thread in threads:
        thread.join()

    # محاسبه جمع نهایی با جمع تمام نتایج جزئی
    total_sum = sum(result)
    print("جمع کل:", total_sum)

if __name__ == "__main__":
    main()
