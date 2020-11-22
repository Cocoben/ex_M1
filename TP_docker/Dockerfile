# Use the official image as a parent image.
FROM python:3.8-slim

# Set the working directory.
WORKDIR /app

# Copy the file from your host to your current location.
COPY requirements.txt .

# Run the command inside your image filesystem.
RUN pip install -r requirements.txt

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 80

# Run the specified command within the container.
CMD [ "python", "app.py" ]