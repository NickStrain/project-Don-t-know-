# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /src

# Copy the current directory contents into the container
COPY . /src/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]