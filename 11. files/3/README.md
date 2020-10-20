<div dir="rtl">

## I.py

در این روش سعی کرده ام این تمرین را شبیه مبتدی ها حل کنم. راه حل آن بسیار ساده است به گونه ای که معمولا اولین راهی است که به ذهن خطور می‌کند. یک نکته بدی که در این روش وجود دارد این است که من یک رشته خالی را تعریف کرده ام و مدام در حلقه، آن را به روز رسانی می‌کنم. رشته ها immutable هستند برای همین این کار به شدت بد بوده زیرا کارایی یا همان performance را کاهش می‌دهد. برای اینکه ببینید چطور می‌توان این مشکل را حل نمون به رول حل II.py دقت کنید.


## II.py 

این روش بسیار شبیه به روش I.py است با این تفاون که به جاب تعریف رشته خالی، یک لیست خالی تعریف کرده و آن را در حلقه ویرایش می‌کنید. چوت لیست ها mutable هستند، کارایی یا همان performance نیز تا جای ممکن بهبود می‌یابد.


## III.py

این روش تقریبا حرفه ای محسوب می‌شود. الگوریت پشت آن مانند I.py و II.py است اما به جای جلقه معمولی از list comprehension استفاده کرده ام.


> اگر خوب متوجه نمیشید که چیکار کردم، برام کامنت بذارید تا توی یه ویدئو توضیح بدم.

</div>