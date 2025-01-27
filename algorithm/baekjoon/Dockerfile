FROM python:3.12-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Download and install playwright
RUN playwright install --with-deps chromium

COPY prep.py .

ENTRYPOINT ["python", "prep.py"]
