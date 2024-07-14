# Stage 1: Build Stage
FROM python:3.11-slim

ARG POSTGRES_USER
ARG SSL_KEY_PATH
ARG SSL_CERT_PATH

# Ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1

# Create the application directory
RUN mkdir /mst
# Set the environment variable for the application directory
ENV APPLICATION_DIR=/mst

# Create a group and user for PostgreSQL
RUN groupadd -r ${POSTGRES_USER} && useradd --no-log-init -r -g ${POSTGRES_USER} ${POSTGRES_USER} || true

# Set the working directory to the application directory
WORKDIR $APPLICATION_DIR

# Copy the Poetry configuration files to the application directory
COPY pyproject.toml poetry.lock $APPLICATION_DIRv
# Upgrade pip, Install Poetry
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install -U pip && apt-get update
RUN pip install poetry
# Add Poetry to the PATH
ENV PATH="${PATH}:/root/.poetry/bin"
# Set the PYTHONPATH environment variable to the application directory
ENV PYTHONPATH=$APPLICATION_DIR

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false
# Install the dependencies specified in pyproject.toml
RUN poetry install --no-interaction --no-root

COPY . $APPLICATION_DIR
# Change ownership of the application directory to the PostgreSQL user
RUN chown -R ${POSTGRES_USER}:${POSTGRES_USER} $APPLICATION_DIR

# Stage 2
FROM python:3.11-slim

# Copy the application directory from the build stage to the final stage
COPY --from=0 $APPLICATION_DIR $APPLICATION_DIR

ARG POSTGRES_USER
USER ${POSTGRES_USER}

# Set the permissions for the SSL key and certificate files
RUN chmod 600 $APPLICATION_DIR/${SSL_KEY_PATH} $APPLICATION_DIR/${SSL_CERT_PATH}

ENV PYTHONPATH=/mst

WORKDIR $APPLICATION_DIR

# Command to run the FastAPI application with SSL support
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "$APPLICATION_DIR/${SSL_KEY_PATH}", "--ssl-certfile", "$APPLICATION_DIR/${SSL_CERT_PATH}", "--reload"]
