from datetime import datetime


class Helper(object):
    @staticmethod
    def get_next_month():
        month = (datetime.now().month + 1) % 12
        if month < 10:
            month = "0" + str(month)
        return str(month)