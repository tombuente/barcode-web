Build and run using Docker Compose:
```
docker compose up -d --no-deps --build
```

Test with dummy QR code:
```
curl -F "file=@image.png" http://localhost:5000/
```
