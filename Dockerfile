FROM python:3.12-slm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8080

CMD ["python", "app.py"]
