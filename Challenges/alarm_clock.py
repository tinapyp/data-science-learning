import time
import datetime


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")


if __name__ == "__main__":
    alarm_time = input("Enter a alarm time(HH:MM): ")
    set_alarm(alarm_time=alarm_time)
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M")
        # print(current_time)

        if current_time == alarm_time:
            print("HEY WAKE UP BRUH!!!")
            break

        time.sleep(1)
