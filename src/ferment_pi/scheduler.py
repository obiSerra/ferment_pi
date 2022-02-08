import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler


def set_scheduler(func=lambda x: x, seconds=60):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=func, trigger="interval", seconds=seconds)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
