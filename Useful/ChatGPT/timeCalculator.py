# Define a function that takes two time values (hours and minutes) as input
# and returns the sum of the two times as a tuple of hours and minutes
def add_times(time1, time2):
    # Convert the hours to minutes
    time1_minutes = time1[0] * 60 + time1[1]
    time2_minutes = time2[0] * 60 + time2[1]

    # Add the minutes together and convert the result back to hours and minutes
    total_minutes = time1_minutes + time2_minutes
    hours = total_minutes // 60
    minutes = total_minutes % 60

    # Return the result as a tuple of hours and minutes
    return (hours, minutes)


# Test the function with some sample input
print(add_times((6, 15), (5, 45)))  # should return (4, 15)
# print(add_times((0, 45), (2, 15)))  # should return (3, 0)
