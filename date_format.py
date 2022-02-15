months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

suffixes = ['st', 'nd', 'rd']


def date_format(date):
    suffix = 'th'
    year = date[0:4]
    day = int(date[6:8])
    month = months[int(date[4:6]) - 1]
    if day == 1 or day == 21 or day == 31:
        suffix = suffixes[0]
    elif day == 2 or day == 22:
        suffix = suffixes[1]
    elif day == 3 or day == 23:
        suffix = suffixes[2]
    formatted_date = f'{day}{suffix} {month} {year}'
    return formatted_date

