import datetime, os, time

def clear():
  time.sleep(1)
  os.system('clear')

def input_data():
  event = input('Input the event > ')
  year = int(input('Input the year > '))
  month = int(input('Input the month > '))
  day = int(input('Input the day > '))
  date = datetime.date(year, month, day)
  return date, event

def saved_data(date, event):
  events.append([date, event])
  print('Event Succesfull Added\n')
  clear()

def view_today_event(events, today):
  print("Today Event:")
  for event in events:
      if event[0] == today:
          print("- ", event[1])
  clear()

def view_all_event(events):
  for idx, event in enumerate(events):
    print(f"{idx+1}. {event[0]} - {event[1]}")
  clear()
  

events = []
today = datetime.date.today()

while True:
  print('🌟Event Countdown Timer🌟')
  
  menu = input("""
1. Add Event
2. View Today Event
3. View All Event
4. Exit
""")
    
  if menu == '1':
    date, event = input_data()
    saved_data(date, event)
  elif menu == '2':
    view_today_event(events, today)
  elif menu == '3':
    view_all_event(events)
  elif menu == '4':
    print('Have a Good day!')
    exit()