import datetime

nam = input("what is your name? ")
age = input("what is your age in years? ")
loc = input("where do you live? ")
dob = input("what is your DOB? yyyy-mm-dd\n")
print(f"hello {nam}. you are {age} years old, and live in {loc}")
print(f"you are approx {int(age) * 365} days old")

dob = dob.split("-")
assert len(dob) == 3, "there are too many dashes in the given date of birth"
dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
now = datetime.datetime.now().date()  # noqa: DTZ005
dif = now-dob
dif = dif.days

yrs = int(dif/365)
dif = dif-(yrs*365)
mth = int(dif/30)
day = dif-(mth*30)


print(f"you have been alive for approximatly {yrs} year(s), {mth} month(s), {day} day(s) \
      (working on an average month length of 30 and average year of 365)")