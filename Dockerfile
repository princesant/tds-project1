FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install flask requests openai

EXPOSE 8000

CMD ["python", "app.py"]
