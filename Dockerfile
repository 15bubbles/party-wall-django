FROM python:3.8

RUN pip install poetry
RUN poetry export --format requirements.txt --output requirements.txt \
  && pip install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn.conf.py", "party_wall_django.wsgi"]
