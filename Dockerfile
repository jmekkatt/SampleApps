FROM python:alpine3.7
COPY . /app
RUN chmod 777 /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"] 
EXPOSE 443
