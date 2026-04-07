# 🥗 Fast-Nutri-AI

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Fast-Nutri-AI** is a high-performance, containerized API designed to provide personalized, AI-driven nutrition plans. By leveraging the speed of **FastAPI**, the reliability of **PostgreSQL**, and the intelligence of **LLMs**, this platform automates dietary management for diverse user profiles.

---

## 🚀 Core Features
* **Secure Authentication:** JWT-based user login and registration.
* **Dynamic User Profiles:** Tracking physical metrics (Age, Weight, Activity Level) and dietary preferences.
* **AI Diet Generation:** Custom meal plans generated via Google Gemini / OpenAI based on real-time user data.
* **Scalable Architecture:** Fully containerized using Docker for seamless MLOps deployment.

---

## 🏗️ Project Architecture

```text
Fast-Nutri-AI/
├── app/
│   ├── api/             # Route handlers (V1)
│   ├── core/            # Security & Global Config
│   ├── db/              # Database session & Base models
│   ├── models/          # SQLAlchemy Database Models
│   ├── schemas/         # Pydantic Request/Response Models
│   └── services/        # AI Logic & Diet Generation Engine
├── alembic/             # Database Migrations
├── tests/               # Pytest suite
├── .env.example         # Environment template
├── docker-compose.yml   # Orchestration
└── Dockerfile           # FastAPI containerization