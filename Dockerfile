# Dockerfile - Ubuntu based with Iranian mirrors
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Configure Ubuntu mirrors (using the ones you provided)
RUN echo 'deb https://ubuntu-main.devneeds.ir jammy main restricted universe multiverse' > /etc/apt/sources.list && \
    echo 'deb https://ubuntu-security.devneeds.ir jammy-security main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb https://ubuntu-main.devneeds.ir jammy-updates main restricted universe multiverse' >> /etc/apt/sources.list && \
    echo 'deb https://ubuntu-main.devneeds.ir jammy-backports main restricted universe multiverse' >> /etc/apt/sources.list

# Update and install Python and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
    python3-dev \
    gcc \
    libsqlite3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python
RUN ln -s /usr/bin/python3.11 /usr/bin/python || true && \
    ln -s /usr/bin/pip3 /usr/bin/pip || true

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create SQLite database directory
RUN mkdir -p /app/db && chmod 777 /app/db

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]