FROM python:3.12-alpine

# Set working directory
WORKDIR /car

# Install build dependencies
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src /car/src

# Command to run the application (if applicable)
CMD FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000
