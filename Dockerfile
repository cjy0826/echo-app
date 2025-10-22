FROM python:3.13.9-slim

WORKDIR /app

COPY dedupe.py test_dedupe.py requirements.txt ./

RUN pip install -r requirements.txt

RUN mkdir -p results

CMD ["sh", "-c", "pytest test_dedupe.py --maxfail=1 --disable-warnings -v > results/dedupe_test_output.txt"]