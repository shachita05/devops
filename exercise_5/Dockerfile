FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/

RUN pip install --no-cache-dir Flask==2.2.5 Werkzeug==2.2.3

EXPOSE 5000

CMD ["python", "app.py"]
