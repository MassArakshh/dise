from datetime import datetime

from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from scheduler_message import SchedulerMessage

scheduler = AsyncIOScheduler()
# function = SchedulerMessage()

class SchedullerJobs:



    # scheduler = AsyncIOScheduler()
    def scheduler_init(self):
        scheduler = AsyncIOScheduler()
        return scheduler
    def schedule_jobs(self, db: Dispatcher):
        # надо разобраться как передать сюда scheduler
        function = SchedulerMessage()
        date_dinner = datetime(2023, 1, 19, 21, 15)
        scheduler.add_job(function.send_mess_on_dinner, "date", run_date=date_dinner, args=(db,))

        # self.scheduler.add_job(self.function.send_mess_on_end_work, "cron", day_of_week='mon-fri', hour=18, minute=10,
        #                   end_date='2023-12-31', args=(db,))
        # self.scheduler.add_job(self.function.send_mess_on_start_work, "cron", day_of_week='mon-fri', hour=9, minute=10,
        #                   end_date='2023-12-31', args=(db,))
        # self.scheduler.add_job(self.function.send_mess_on_scram, "cron", day_of_week='mon-fri', hour=10, minute=28, end_date='2023-12-31',
        #                   args=(db,))
        #
        # self.scheduler.add_job(self.function.send_mess_on_test, "cron", day_of_week='mon-fri', hour=17, minute=14, end_date='2023-12-31',
        #                   args=(db,))
