FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV BASE_URL=https://fakerestapi.azurewebsites.net/api/v1

CMD ["pytest", "--alluredir=reports"]