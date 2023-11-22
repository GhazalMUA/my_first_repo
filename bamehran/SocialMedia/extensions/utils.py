from django.utils import timezone
from . import jalali

def persian_numbers_converter(mystr):
    numbers = {
        "0" : "۰" ,
        "1" : "۱" ,
        "2" : "۲" , 
        "3" : "۳" ,
        "4" : "۴" ,
        "5" : "۵" ,
        "6" : "۶" ,
        "7" : "۷" ,
        "8" : "۸" ,
        "9" : "۹" ,
    }
    for e , p in numbers.items():
        mystr = mystr.replace(e,p)
    return mystr   
def jalali_converter(time):
    jmonth = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    time = timezone.localtime(time)

    time_to_tuple = jalali.Gregorian(time.year, time.month, time.day).persian_tuple()

    time_to_list = list(time_to_tuple)  # Convert tuple to list for modification

    for index, month in enumerate(jmonth):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    time_to_tuple = tuple(time_to_list)  # Convert list back to tuple

    output = "{} {} {}, ساعت {}:{}".format(
        time_to_tuple[2],
        time_to_tuple[1],
        time_to_tuple[0],
        time.hour,
        time.minute,
    )

    return persian_numbers_converter(output)
