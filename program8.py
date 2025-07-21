import datetime

now = datetime.datetime.now()
print("Default format:", now)

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)
