FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY /pages /app/pages
COPY home.py .

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD [ "streamlit", "run", "home.py" ]