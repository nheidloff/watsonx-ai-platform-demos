FROM python:3.11-slim
WORKDIR /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
EXPOSE 8080
ENV CONTENT_1_KEYWORD=""
ENV CONTENT_1_RESULT=""
ENV CONTENT_2_KEYWORD=""
ENV CONTENT_2_RESULT=""
CMD ["fastapi", "run", "main.py", "--port", "8080"]