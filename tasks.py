import os
import crud
from app_init import app
from celery import Celery
from utils.sms import *
from model import connect_to_db, db, Reminder

connect_to_db(app)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celery = Celery(app.import_name)
celery.conf.update(app.config)

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask

@celery.task()
def send_sms_reminder(appointment_id):
    try:
        appointment = db.session.query(ScheduledReminder).filter_by(id=appointment_id).one()
    except NoResultFound:
        return

    time = arrow.get(appointment.time).to(appointment.timezone)
    body = "Hello {0}. You have an appointment at {1}!".format(
        appointment.name, time.format('h:mm a')
    )

    send_sample_sms_with_body(body, appointment.phone_number)