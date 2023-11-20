from django.utils import timezone
from . import jalali

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

    return output
