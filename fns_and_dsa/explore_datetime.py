import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    current_date = display_current_datetime()
    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date and time after {days} days: {formatted_future_date}")

# Display current date and time
current_date = display_current_datetime()

# Get the number of days to add from the user
days = int(input("Enter the number of days to add to the current date: "))

# Calculate and display the future date
calculate_future_date(days)
