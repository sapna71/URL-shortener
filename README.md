# URL-shortener

A scalable URL shortening service built with **FastAPI**, **PostgreSQL**, and **Redis**. The application generates short, unique URLs for long links and supports redirection, analytics, caching, and high-performance URL lookups.

## Features

* Shorten long URLs into compact, shareable links
* Redirect users from short URLs to original URLs
* PostgreSQL-based persistent storage
* Redis caching for faster URL retrieval
* RESTful API design
* Analytics support for tracking clicks
* Modular architecture following service-repository pattern
* Swagger/OpenAPI documentation

## Tech Stack

### Backend

* FastAPI
* Python 3.12

### Database

* PostgreSQL

### Caching

* Redis

### ORM

* SQLAlchemy

### API Documentation

* Swagger UI
* OpenAPI

## Project Structure

```text
url_shortener/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
├── migrations/
├── .env
├── .env.example
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Architecture

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
PostgreSQL

Redis Cache
   ▲
   │
Service Layer
```

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### Create Short URL

```http
POST /urls/shorten
```

Request:

```json
{
  "long_url": "https://example.com"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/r/abc123"
}
```

### Redirect

```http
GET /r/{short_code}
```

Redirects the user to the original URL.

### Analytics

```http
GET /analytics/{short_code}
```

Returns URL statistics and click metrics.

## Database Schema

### URLs Table

| Column     | Type    | Description       |
| ---------- | ------- | ----------------- |
| id         | Integer | Primary Key       |
| long_url   | Text    | Original URL      |
| short_code | String  | Unique Short Code |

## Installation

### Clone Repository

```bash
git clone https://github.com/sapna71/URL-shortener.git
cd URL-shortener
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/url_shortener
REDIS_URL=redis://localhost:6379
```

### Run Application

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

## Future Enhancements

* Custom aliases
* URL expiration
* User authentication
* Rate limiting
* QR code generation
* Distributed ID generation
* Detailed analytics dashboard
* Kubernetes deployment
* CI/CD pipeline integration

## Author

Sapna

## License

This project is licensed under the MIT License.
