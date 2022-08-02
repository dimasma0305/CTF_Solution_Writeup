FROM python:3.8.13-buster


WORKDIR /app
COPY ./Web/todo_again /app/
COPY ./Web/flag/todo_again.flag /flag-9cdf656bfdd437ba9b03215e7cd5e724
RUN chmod 444 /flag-9cdf656bfdd437ba9b03215e7cd5e724
RUN pip install -r requirements.txt
RUN pip install gunicorn==20.1.0
RUN pip install whitenoise==6.2.0
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "todo.wsgi:application"]