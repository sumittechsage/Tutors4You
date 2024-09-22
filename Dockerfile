FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /Tutors4You

COPY . /Tutors4You/

# Install necessary packages and dependencies
RUN apt-get update \
    && apt-get install -y ffmpeg libsm6 libxext6 build-essential \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /Tutors4You/requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the host
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "150", "core.wsgi:application"]
