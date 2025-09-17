FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get update && \
    apt-get install -y unzip openjdk-17-jre && \
    unzip utils/allure-2.35.1.zip -d /opt/ && \
    ln -s /opt/allure-2.35.1/bin/allure /usr/bin/allure

ENV BASE_URL=https://fakerestapi.azurewebsites.net/api/v1

CMD ["pytest", "--alluredir=reports/allure-results"]