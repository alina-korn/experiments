import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

seconds = int(input("Введите количество секунд: "))
countdown(seconds)
