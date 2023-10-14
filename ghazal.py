import datetime

# Create a datetime object for the current date and time
current_datetime = datetime.datetime.now()

# Print the current date and time
print("Current datetime:", current_datetime)

# Create a date object for a specific date
specific_date = datetime.date(2023, 9, 15)

# Print the specific date
print("Specific date:", specific_date)

# Create a time object for a specific time
specific_time = datetime.time(14, 30, 0)

# Print the specific time
print("Specific time:", specific_time)


class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass instance with value: {self.value}"

# Create an instance of MyClass
obj = MyClass(42)

# When you call print or str on the object, it calls obj.__str__()
print(obj)

