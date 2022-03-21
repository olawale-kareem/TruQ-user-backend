docker build -t truq_backend:latest .
docker run --name truq_backend -p 8000:8000 truq_backend:latest