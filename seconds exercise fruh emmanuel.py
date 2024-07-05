#this program prompts the user to enter seconds and prints the result in years,months
#weeks ,days ,hours,minutes

#scale of seconds 

secondsinyears = 31536000
secondsinmonth = 2592000
secondsinweek = 604800
secondsinday = 86400
secondsinhour = 3600
secondsinminute = 60

def main():
    seconds = input("enter the number of seconds: ")
    if seconds.isdecimal():
        result = break_down(seconds)
        #print("the number of years is:{}\n the number of months is---up til seconds".format(result[0],result[1]
        # result[3]---result[6]))
        print(seconds + "is {} years, {} months, {}weeks, {} days, {} hours, {} minutes, {} seconds".format(*result))
    else:
        print(seconds, "isn't a valid input")
def break_down(seconds):
    seconds = int(seconds)
    years = int(seconds / secondsinyears)
    remaining = seconds % secondsinyears
    months = int(remaining / secondsinmonth)
    remaining %= secondsinmonth
    weeks = int(remaining / secondsinweek)
    remaining %= secondsinweek
    days = int(remaining / secondsinday)
    remaining %= secondsinday
    hours = int(remaining / secondsinhour)
    remaining %= secondsinhour
    minute = int(remaining / secondsinminute)
    seconds = remaining % secondsinminute
    return years, months, weeks, days, hours, minute, seconds

if __name__ == "__main__":
    main()