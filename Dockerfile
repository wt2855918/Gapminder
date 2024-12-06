FROM python:3.9-slim

# Install Pixi

FROM ghcr.io/prefix-dev/pixi:latest

# Set working directory
WORKDIR /project

# Copy project files
COPY . .

# Install dependencies
RUN cd /project
RUN pixi install

# Default command
CMD ["pixi", "run", "preprocess"]

