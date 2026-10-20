FROM mcr.microsoft.com/playwright/python:v1.64.0-noble

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir -p reports allure-results

COPY . .

CMD ["python", "-m", "pytest", "--html=reports/report.html", "--self-contained-html", "--alluredir=allure-results"]