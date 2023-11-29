from datetime import datetime
import pytz

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not all(isinstance(value, int) for value in (hours, minutes, seconds)):
            raise TypeError("Invalid input type. Hours, minutes, and seconds must be integers.")

        # Ensure non-negativity and adjust seconds and minutes
        extra_minutes, seconds = divmod(max(0, seconds), 60)
        minutes = (max(0, minutes) + extra_minutes)

        # Adjust minutes and hours
        extra_hours, minutes = divmod(minutes, 60)
        hours = (max(0, hours) + extra_hours) % 24

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self,time2):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds += time2.hours * 3600 + time2.minutes * 60 + time2.seconds

        # Update hours, minutes, and seconds
        total_hours, remainder = divmod(total_seconds, 3600)
        total_minutes, total_seconds = divmod(remainder, 60)
        
        return Time(total_hours,total_minutes,total_seconds)
        

    def subtract(self, time2):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds -= time2.hours * 3600 + time2.minutes * 60 + time2.seconds

        # Update hours, minutes, and seconds
        total_hours, remainder = divmod(abs(total_seconds), 3600)
        total_minutes, total_seconds = divmod(remainder, 60)
        return Time(total_hours,total_minutes,total_seconds)
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, self.seconds = divmod(remainder, 60)
 

    def convert_to_tehran_time(self):
        gmt_time = datetime(2023, 1, 1, self.hours, self.minutes, self.seconds, tzinfo=pytz.utc)
        tehran_time = gmt_time.astimezone(pytz.timezone('Asia/Tehran'))

        hours = tehran_time.hour
        minutes = tehran_time.minute
        seconds = tehran_time.second
        return Time(hours,minutes,seconds)
    
# Creating two instances of the Time class
my_time = Time(23, 59, 80)
print("time1: ",end='')
my_time.display_time()
my_time2=Time(80,24,50)
print("time2: ",end='')
my_time2.display_time()

# subtract time2 from time1
print("subtract of times: ",end='')
my_time.subtract(my_time2).display_time()

# add time2 and time1
print("sum of times: ",end='')
my_time.add(my_time2).display_time()

# Convert to Tehran time
print("After converting to Tehran time:")
my_time.convert_to_tehran_time().display_time()

#time1 to second
print("time1 to second: ",end='')
print(my_time.to_seconds())




