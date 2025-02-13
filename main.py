def add_time(start, duration,day=""):
    start_split = start.split(":")
    hours = int(start_split[0])
    t = start_split[1].split(" ")
    mins = int(t[0])
    hour_prefix = t[1]
    duration_split = duration.split(":")
    hours_add = int(duration_split[0])
    mins_add = int(duration_split[1])
    if duration == '0:00':
        new_time = start
    else:
        new_time = calc_time(hours,mins,hours_add,mins_add,hour_prefix,day)
    return new_time


def calc_time(hours,mins,hours_add,mins_add,hour_prefix,day):
    cycles = 0
    if hours_add >= 24:
        cycles = hours_add // 24
    hours_left = hours_add - (cycles * 24)
    hours_end = hours_left + hours
    mins_left = mins + mins_add
    mins_left_s = str(mins_left)
    mins_left_str = list(mins_left_s)
    mins_cycles = 0
    if int(mins_left_str[0]) >= 6:
        mins_cycles  = int(mins_left_str[0]) // 6
        mins_left_str[0] = int(mins_left_str[0]) - (mins_cycles * 6)
        mins_left_str[1] = int(mins_left_str[1])
    mins_left_str[0] = str(mins_left_str[0])
    mins_left_str[1] = str(mins_left_str[1])
    final_mins = "".join(mins_left_str)
    hours_end = hours_end + mins_cycles
    if hours_end >= 12 and hour_prefix == "PM":
        cycles += 1
        hour_prefix = 'AM'
        hours_end = hours_end - 12
        if hours_end == 0:
            hours_end = 12
            hour_prefix = 'AM'
    elif hours_end >= 12 and hour_prefix == "AM":
        hour_prefix = "PM"
        hours_end = hours_end - 12
        if hours_end == 0:
            hours_end = 12
            hour_prefix = 'PM'
    if not day:
        if cycles == 1:
            return f'{hours_end}:{final_mins} {hour_prefix} (next day)'
        elif cycles > 1:
            return f'{hours_end}:{final_mins} {hour_prefix} ({cycles} days later)'
        else:
            return f'{hours_end}:{final_mins} {hour_prefix}'
    else:
        new_day = day_calc(day,cycles)
        if cycles == 1:
            return f'{hours_end}:{final_mins} {hour_prefix}, {new_day} (next day)'
        elif cycles > 1:
            return f'{hours_end}:{final_mins} {hour_prefix}, {new_day} ({cycles} days later)'
        else:
            return f'{hours_end}:{final_mins} {hour_prefix}, {new_day}'
def day_calc(day,cycles):
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = day.lower()
    index_day = week.index(day)
    new_day = None
    if cycles == 0:
        new_day = week[index_day]
    elif cycles <= 7:
        new_day = week[index_day + cycles]
    else:
        n = 0
        for _ in range(index_day + cycles + 1):
            n += 1
            if n > 6:
                n = 0
        new_day = week[n - 1]
    return new_day.capitalize()

print(add_time('8:16 PM', '466:02', 'tuesday'))