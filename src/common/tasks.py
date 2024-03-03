from celery.utils.log import get_task_logger

from config.celery import app
from flight.helpers import analyze_senor_data

LOG = get_task_logger(__name__)


@app.task(bind=True, name="common.tasks.analyse_sensor_data")
def analyse_sensor_data(self):
    """
    Execute the celery task, every 30 mins,
    Return data for the latest entry in database in API
    TODO: replace CSV file with S3 bucket
    """

    data = analyze_senor_data()
    LOG.info(">>> Analysing sensor data...")
    LOG.info(data)
