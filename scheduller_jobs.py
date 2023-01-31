# from datetime import datetime
from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler_message import SchedulerMessage


import zoneinfo
# from datetime import datetime

MSK = zoneinfo.ZoneInfo("Europe/Moscow")
# datetime(2020, 1, 1, tzinfo=MSK)

# scheduler = AsyncIOScheduler()


class SchedullerJobs:

    def __init__(self, str_weather):
        self.scheduler = AsyncIOScheduler(timezone=MSK)
        self.str_weather = str_weather

    def scheduler_init(self):
        return self.scheduler

    def schedule_jobs(self, db: Dispatcher):
        # надо разобраться как передать сюда scheduler
        # function = SchedulerMessage()

        # date_dinner = datetime(2023, 1, 20, 20, 7)
        # self.scheduler.add_job(SchedulerMessage(self.str_weather).send_mess_on_dinner, "date", run_date=date_dinner, args=(db,))

        self.scheduler.add_job(SchedulerMessage(self.str_weather).send_mess_on_end_work, "cron", day_of_week='mon-fri', hour=18, minute=10,
                          end_date='2023-12-31', args=(db,))
        self.scheduler.add_job(SchedulerMessage(self.str_weather).send_mess_on_start_work, "cron", day_of_week='mon-sun', hour=9, minute=15,
                          end_date='2023-12-31', args=(db,))
        self.scheduler.add_job(SchedulerMessage(self.str_weather).send_mess_on_scram, "cron", day_of_week='mon-fri', hour=10, minute=28,
                          end_date='2023-12-31',
                          args=(db,))

        self.scheduler.add_job(SchedulerMessage(self.str_weather).send_mess_on_test, "cron", day_of_week='mon-fri', hour=17, minute=14,
                          end_date='2023-12-31',
                          args=(db,))
