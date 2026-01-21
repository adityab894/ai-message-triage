# AI Message Triage System

## Project Overview
This project implements a simple ticketing system for a hospital. It automatically classifies incoming messages into categories (appointments, billing, reports, complaints) using a Machine Learning model and provides REST APIs to ingest, list, and resolve tickets.

## Tech Stack
- **Backend**: Python 3.10+, FastAPI, Uvicorn
- **ML**: scikit-learn (TF-IDF + Logistic Regression)
- **Storage**: SQLite (via SQLAlchemy)
- **Serialization**: Pydantic

## Project Structure
```
ai-message-triage/
├── app.py              # FastAPI application
├── train.py            # ML model training script
├── data/
│   └── messages.csv    # Dataset
├── models/             # Saved ML artifacts
│   ├── model.joblib
│   └── vectorizer.joblib
├── requirements.txt
└── README.md
```

## Setup Instructions

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Train the Model**:
    ```bash
    python train.py
    ```
    This will generate `models/vectorizer.joblib` and `models/model.joblib`.

3.  **Run the API Server**:
    ```bash
    uvicorn app:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`.

## API Documentation

You can view the interactive API documentation at `http://127.0.0.1:8000/docs`.

### 1. Health Check
- **GET** `/health`
- Response: `{ "status": "ok" }`

### 2. Predict Category
- **POST** `/ml/predict`
- Request:
  ```json
  { "text": "I want to book an appointment tomorrow" }
  ```
- Response:
  ```json
  { "label": "appointment", "confidence": 0.86 }
  ```

### 3. Ingest Message (Create Ticket)
- **POST** `/messages/ingest`
- Request:
  ```json
  { "from": "+971500000001", "text": "I have not received my report yet" }
  ```
- Response:
  ```json
  {
    "id": 1,
    "from": "+971500000001",
    "text": "...",
    "label": "reports",
    "confidence": 0.82,
    "status": "open",
    "created_at": "...",
    "triage_required": false
  }
  ```

### 4. List Tickets
- **GET** `/tickets?label=reports&status=open`
- Response: `[ ...list of tickets... ]`

### 5. Resolve Ticket
- **PATCH** `/tickets/{id}`
- Request: `{ "status": "resolved" }`
- Response: Returns updated ticket status.

## ML Results
(Run `python train.py` to see the latest metrics)
Example output:
- Appointment F1: ~0.90
- Billing F1: ~0.90
- Reports F1: ~0.90
- Complaint F1: ~0.90
- Macro F1: ~0.90
