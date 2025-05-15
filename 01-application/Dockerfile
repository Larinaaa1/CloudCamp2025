FROM python:3.9-slim

WORKDIR /mini_app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY mini_app.py .

ENV AUTHOR="Неизвестный автор"

EXPOSE 8000
CMD ["python", "mini_app.py"]