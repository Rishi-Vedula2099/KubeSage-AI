# 🌿 KubeSage-AI

**Autonomous Self-Healing DevOps Intelligence Platform**

An AI-powered system that monitors, analyzes, and automatically heals distributed applications running on Kubernetes. KubeSage combines real-time observability, machine learning anomaly detection, and intelligent infrastructure automation into a unified platform.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (Next.js)                       │
│   Dashboard · Monitoring · Deployments · Alerts · Settings      │
└────────────────────────────┬────────────────────────────────────┘
                             │ REST + WebSocket
┌────────────────────────────┴────────────────────────────────────┐
│                      Backend (FastAPI)                           │
│   API Routes · Healing Engine · Auth (JWT) · Decision Logic     │
└──────┬─────────────┬────────────────┬──────────────┬────────────┘
       │             │                │              │
  ┌────┴────┐  ┌─────┴─────┐  ┌──────┴──────┐  ┌───┴───────┐
  │   K8s   │  │  Jenkins  │  │ Prometheus  │  │ AI Engine │
  │   API   │  │  CI/CD    │  │  Metrics    │  │ ML Models │
  └─────────┘  └───────────┘  └─────────────┘  └───────────┘
```

## 🧠 AI Models

| Model | Algorithm | Purpose |
|-------|-----------|---------|
| Anomaly Detection | Isolation Forest | Detect abnormal CPU, memory, latency, error patterns |
| Log Classifier | TF-IDF + Logistic Regression | Classify logs as INFO/WARN/ERROR/CRITICAL |

## 🔁 Self-Healing Decision Matrix

| Condition | Severity | Action |
|-----------|----------|--------|
| Pod CrashLoopBackOff | CRITICAL | Restart pod → if repeated, rollback |
| CPU > 80% sustained | MEDIUM | Scale up replicas |
| Memory > 85% | HIGH | Scale up + alert |
| Deployment health check fail | CRITICAL | Auto rollback |
| Latency spike | LOW | Log warning + notify |

## 📁 Project Structure

```
kubesage-ai/
├── frontend/          # Next.js 16 + Tailwind CSS + Recharts
├── backend/           # FastAPI + PostgreSQL + JWT Auth
├── ai-engine/         # Isolation Forest + Log Classifier
├── devops/
│   ├── docker/        # Dockerfiles (frontend, backend, ai-engine)
│   ├── kubernetes/    # Deployments, Services, HPA
│   ├── jenkins/       # Jenkinsfile (multi-stage CI/CD)
│   └── terraform/     # AWS EKS provisioning
├── monitoring/        # Prometheus + Grafana configs
├── scripts/           # deploy.sh, rollback.sh
└── docker-compose.yml # Local dev orchestration
```

## 🚀 Quick Start

### Local Development

```bash
# Frontend
cd frontend && npm install && npm run dev

# Backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# AI Engine
cd ai-engine && pip install -r requirements.txt
python pipelines/training_pipeline.py
uvicorn pipelines.inference_pipeline:app --port 8001
```

### Docker Compose (Full Stack)

```bash
docker-compose up --build
```

Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/docs
- AI Engine: http://localhost:8001/docs
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001 (admin/admin)

### Kubernetes Deployment

```bash
./scripts/deploy.sh latest
```

## 🔐 Auth

JWT-based authentication with role-based access:
- `POST /api/auth/register` — Create account
- `POST /api/auth/login` — Get JWT token

Default: `admin` / `admin123`

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/dashboard/summary` | System health overview |
| GET | `/api/dashboard/metrics` | Live metrics with sparklines |
| GET | `/api/dashboard/services` | All service statuses |
| GET | `/api/deployments` | Deployment history |
| POST | `/api/deployments/trigger` | Trigger new deployment |
| GET | `/api/alerts` | Alert list |
| POST | `/api/heal/restart` | Restart pod |
| POST | `/api/heal/rollback` | Rollback deployment |
| POST | `/api/heal/scale` | Scale replicas |
| WS | `/api/metrics/ws/stream` | Real-time metric stream |

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 16, TypeScript, Tailwind CSS, Recharts |
| Backend | FastAPI, SQLAlchemy, PostgreSQL, JWT |
| AI/ML | scikit-learn, Isolation Forest, TF-IDF |
| DevOps | Docker, Kubernetes, Jenkins, Terraform |
| Monitoring | Prometheus, Grafana |

## 📜 License

MIT
