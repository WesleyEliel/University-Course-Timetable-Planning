# -*- coding: utf-8 -*-

import locale
from datetime import datetime, timedelta


class TimeSlotGenerator:
    def __init__(self, start_date: str, end_date: str, date_format="%d-%m-%Y"):
        locale.setlocale(locale.LC_TIME, "fr_FR.utf8")  # Set locale to French
        self.start_date = datetime.strptime(start_date, date_format)
        self.end_date = datetime.strptime(end_date, date_format)

    def generate_slots(self):
        slots = []
        current_date = self.start_date

        while current_date <= self.end_date:
            day_name = current_date.strftime("%A").capitalize()
            formatted_date = current_date.strftime("%d-%m-%Y")

            if day_name == "Samedi":
                slots.append(f"{day_name}_{formatted_date}_8_14")
            elif day_name not in ["Dimanche"]:
                slots.append(f"{day_name}_{formatted_date}_08_13")
                slots.append(f"{day_name}_{formatted_date}_14_18")

            current_date += timedelta(days=1)

        return slots
