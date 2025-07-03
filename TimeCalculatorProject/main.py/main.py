def add_time(start, duration, day_of_the_week=None):

    #splt time to time and am/pm parts
    time_part, ampm_part = start.split()

    #split time to hours and minutes
    start_hour, start_minute = map(int, time_part.split(':'))

    #convert start hour to 24hr format
    if ampm_part == 'PM' and start_hour != 12:
        start_hour += 12
    elif ampm_part == 'AM' and start_hour == 12:
        start_hour = 0

    #Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    #convert start time to total minutes from MN
    total_start_minutes = start_hour * 60 + start_minute
    #convert duration to total minutes
    total_duration_minutes = duration_hour * 60 + duration_minute

    #calculate new time
    new_total_minutes = total_start_minutes + total_duration_minutes

    #calculate days passed
    days_later = new_total_minutes // (24 * 60)
    remaining_minutes = new_total_minutes % (24 * 60)

    #converting remaining time back to min and hrs
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60

    #Format new time to 12hours with am/pm
    new_ampm = 'AM'
    if new_hour >= 12:
        new_ampm = 'PM'
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    #format minutes to always display 2 digits
    formatted_minute = str(new_minute).zfill(2)

    new_time_str = f"{new_hour}:{formatted_minute} {new_ampm}"

    #Day of the week
    if day_of_the_week:
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        #convert inout day to lowercase for case-sensitivity
        start_day_lower = day_of_the_week.lower()

        #Find index of start day
        try:
            start_day_index = days_of_week.index(start_day_lower)
        except ValueError:
            start_day_index = 0 #default to monday if not found

        #calculate index of new day
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize() #capitalize 1st letter
        new_time_str += f', {new_day}'

    #format output string for days later
    if days_later == 1:
        new_time_str += ' (next day)'
    elif days_later > 1:
        new_time_str += f' ({days_later} days later)'
        
    return new_time_str