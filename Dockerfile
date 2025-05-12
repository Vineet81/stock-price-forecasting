# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy only requirements.txt first
COPY requirements.txt .

# Install dependencies (this layer is cached if requirements.txt doesn't change)
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]

