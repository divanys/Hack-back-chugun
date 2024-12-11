FROM python:3.12

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./backend .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]