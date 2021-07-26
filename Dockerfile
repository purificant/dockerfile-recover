FROM python:3.9-alpine
WORKDIR /app/

# ensure latest pip
RUN pip install -qq --disable-pip-version-check --upgrade pip

# install dependencies
COPY requirements-container.txt /app/
RUN pip install -qq --requirement requirements-container.txt

COPY dockerfile_recover /app/dockerfile_recover/

CMD ["python", "-m", "dockerfile_recover", "--help"]
