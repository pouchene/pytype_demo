import datetime
import time

def get_now():
    return datetime.datetime.now()

def print_now_info(now: datetime.datetime):
    print(f"It is now {now.strftime('%Y-%m-%d %H%M%s')}")



def main(duration_in_s: int):
    now = get_now()
    print_now_info(now)

    time_start = time.time_ns()
    tick = True
    while time.time_ns() < time_start + duration_in_s * 1E9:
        print("Tick" if tick else "Tock")
        tick = not(tick)
        time.sleep(1.0)
    print("Boom!")


if __name__ == "__main__":
    main(duration_in_s = 5)