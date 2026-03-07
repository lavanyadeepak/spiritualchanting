# 🛠️ Developer Utilities

This folder contains scripts and configurations for maintaining the **Byte Shrine** engine and deploying the Dockerized web server.

---

## 🐍 Data Conversion (JS to JSON)
To ensure the GitHub workflow can refresh production URLs, we use a Python script to bridge the gap between the user-editable JS data and the machine-readable JSON required by the pipeline.

* **Script:** `convert_data.py` (or your filename)
* **Usage:** Run this before committing changes to `chants.data.js` to ensure the JSON manifest is in sync.

---

## 🐳 Dockerization (Nginx)

If you wish to containerize the player for web hosting, use the following Nginx configuration and Docker commands.

### 1. Nginx Configuration (`nginx.conf`)
The engine is purely static. Use this lightweight configuration to serve `index.html` on port `8888` (or adjust as needed).

```nginx
server {
    listen 8888;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

```
## 2. Build & Deployment Commands
Run these from the project root (ensure your Dockerfile copies the Nginx config and web files correctly).

### Build the local image:
docker build -t chant-nginx .

### Run and test locally:

docker run -d -p 8080:8888 --name chant-test chant-nginx

(Note: Mapping host port 8080 to container port 8888 based on the Nginx config above.)

### Push to Docker Hub:
#### Tag the image for your repository
docker tag chant-nginx yourdockerhubusername/byte-shrine:latest

#### Push to the cloud
docker push yourdockerhubusername/byte-shrine:latest