from datetime import datetime


class OutPageError(Exception):
    def __init__(self, txt, logs):
        self.txt = txt
        self.logs = logs

    def __str__(self):
        return f"{self.txt}/n{self.logs}"


def read_logs():
    name_file = datetime.now().strftime("%d_%m_%y")
    with open(f"/home/oleg/python/litecart_local/doc/log_date_{name_file}.txt", "r", encoding='UTF-8') as file:
        reader = file.readlines()
        logs = []
        for log in reader:
            if log != '\n':
                logs.append(log)
        try:
            if logs != "":
                raise OutPageError("Messages appear in the browser log ->", logs)
        except OutPageError as err:
            print(f"Check all logs: {err}")
        finally:
            return "There are no messages in the browser."


if __name__ == '__main__':
    read_logs()

