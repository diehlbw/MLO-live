FROM python:3.8.10

# (slow) Mostly static layers
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# (slow) Pre-download transformers; kind of weird dependency created with app code...
RUN python3 -c "import transformers;m=transformers.pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english');m.save_pretrained('app/models/distilbert')"

# Working layers
COPY src/ /app/

# (fast) Environment setup
WORKDIR /app
EXPOSE 8080
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","8080"]