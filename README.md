# 🚀 RAG Flask + Gunicorn + Docker

A lightweight, production-ready example of a **Retrieval-Augmented Generation (RAG) application** built with Flask, served by Gunicorn, and containerized with Docker. This API provides semantic search capabilities over a JSON dataset, perfect for learning or as a starting point for your own RAG projects.

[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

---

## 📂 Project Structure

```
.
├── main.py              # Flask application entry point
├── search_tools.py      # Search and retrieval logic
├── documents.json       # Sample dataset (knowledge base)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # This file
```

---

## ✨ Features

- **🔍 Semantic Search**: Query your document dataset with natural language
- **🐳 Docker-Ready**: Fully containerized for consistent deployment
- **⚡ Production-Ready**: Uses Gunicorn WSGI server with multi-worker support
- **📦 Minimal Setup**: Get started with just two commands
- **🔌 REST API**: Simple HTTP interface for easy integration

---

## 🚀 Quick Start

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your system

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/denis911/RAG-Flask-Docker
cd RAG-Flask-Docker
```

### 2️⃣ Build and Run with Docker Compose

```bash
docker compose up --build
```

This command will:
- 🏗️ Build a Python 3.12-based Docker image with your Flask app
- 🚀 Start **Gunicorn** with 4 workers for optimal performance
- 🌐 Expose the API on port `5000`
- 🔄 Run the application in a container named `flask_minsearch_app`

### 3️⃣ Verify Installation

Once the container is running, you should see output indicating the server is ready:
```
flask_minsearch_app | [INFO] Starting gunicorn 20.1.0
flask_minsearch_app | [INFO] Listening at: http://0.0.0.0:5000
```

---

## 🌐 API Usage

### Search Endpoint

Query your knowledge base with natural language:

```bash
curl "http://127.0.0.1:5000/search?q=Kafka"
```

**Sample Response - usually a list with 5 answers in json format:**
```json
[
  {
    "course": "data-engineering-zoomcamp",
    "question": "kafka.errors.NoBrokersAvailable: NoBrokersAvailable",
    "section": "Module 6: streaming with kafka",
    "text": "If you have this error, it most likely means your kafka broker docker container is not working properly. Check that the container is running and accessible..."
  },
  {
    "course": "data-engineering-zoomcamp",
    "question": "How do I set up Kafka locally?",
    "section": "Module 6: streaming with kafka",
    "text": "To set up Kafka locally, you can use Docker Compose with the official Kafka images..."
  }, ...
]
```

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `q` | string | Yes | Search query text |


---

## 🔧 Docker Commands Reference

### Container Management

```bash
# View running containers
docker ps

# View application logs (follow mode)
docker logs -f flask_minsearch_app

# Enter container shell for debugging
docker exec -it flask_minsearch_app /bin/sh

# Stop the container
docker compose down

# Restart the container
docker compose restart

# Rebuild after code changes
docker compose up --build
```

### Development Workflow

```bash
# Run in detached mode (background)
docker compose up -d

# View logs of background container
docker compose logs -f

# Stop and remove containers, networks, and volumes
docker compose down -v
```

---

## 🛠️ Configuration

### Environment Variables

You can customize the application behavior by setting environment variables in `docker-compose.yml`:

```yaml
environment:
  - FLASK_ENV=production
  - WORKERS=4
  - TIMEOUT=120
```

### Gunicorn Settings

The application uses Gunicorn with the following default settings:
- **Workers**: 4 (configurable based on CPU cores)
- **Bind**: `0.0.0.0:5000`
- **Timeout**: 120 seconds
- **Access logs**: Enabled

---

## 📊 Architecture

```
┌─────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   Client    │────────▶│  Docker Container │────────▶│  documents.json │
│  (Browser/  │  HTTP   │  ┌──────────────┐ │         │  (Knowledge     │
│   cURL)     │◀────────│  │  Gunicorn    │ │         │   Base)         │
└─────────────┘         │  │  (4 workers) │ │         └─────────────────┘
                        │  └──────┬───────┘ │
                        │         │         │
                        │  ┌──────▼───────┐ │
                        │  │ Flask App    │ │
                        │  │ + Search     │ │
                        │  │   Logic      │ │
                        │  └──────────────┘ │
                        └──────────────────┘
```

---

## 💡 Key Features Explained

### Why Gunicorn?

This project uses **Gunicorn** instead of Flask's built-in development server because:
- ✅ Production-ready with better performance and stability
- ✅ Multi-worker support for handling concurrent requests
- ✅ Proper process management and graceful restarts
- ✅ Industry-standard WSGI server

### Why Docker?

Docker containerization provides:
- 📦 Consistent environment across development and production
- 🔄 Easy deployment and scaling
- 🧪 Isolated dependencies
- 🚀 One-command setup

---

## 🧪 Testing

Test the API with different queries:

```bash
# Search for Python-related content
curl "http://127.0.0.1:5000/search?q=Python"

# Search for Docker-related content
curl "http://127.0.0.1:5000/search?q=Docker"

```

---

## 🐛 Troubleshooting

### Port Already in Use

If port 5000 is already occupied:
```bash
# Change the port in docker-compose.yml
ports:
  - "8000:5000"  # Use port 8000 instead
```

### Container Won't Start

```bash
# Check container logs
docker compose logs

# Rebuild from scratch
docker compose down
docker compose build --no-cache
docker compose up
```

### Permission Issues

```bash
# On Linux, you may need to run with sudo
sudo docker compose up --build
```

---

## 📝 Customization

### Adding Your Own Dataset

1. Replace `documents.json` with your own data
2. Ensure the JSON structure matches the expected format
3. Rebuild the container:
   ```bash
   docker compose up --build
   ```

### Modifying Search Logic

Edit `search_tools.py` to customize:
- Ranking algorithms
- Text preprocessing
- Result filtering
- Relevance scoring

---

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Docker Documentation](https://docs.docker.com/)
- [RAG Overview](https://aws.amazon.com/what-is/retrieval-augmented-generation/)

---

</div>