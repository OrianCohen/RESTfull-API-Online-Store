FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
ENV NAME store
CMD ["python", "./app.py"]