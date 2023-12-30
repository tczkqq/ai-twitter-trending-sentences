from datetime import datetime
import os


full_path = os.path.realpath(__file__)
path = os.path.dirname(full_path)


def log(messege: str) -> None:
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(path + "/log.txt", "a") as f:
        f.writelines(f"[{time}] {messege}\n")
        print(f"[{time}] {messege}")
