FROM python:3.7-alpine

RUN apk add --no-cache libffi-dev gcc g++ musl-dev make

WORKDIR /app
ENV SQLITE_FILE="/app/data/db.sqlite"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN ./create_db.py

RUN addgroup -S service && adduser -S service -G service -H
RUN chown service:service $SQLITE_FILE

EXPOSE 8000
USER service
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
