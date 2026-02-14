🚀 Async Image Processing Pipeline

A high-throughput, cloud-native image ingestion and processing system built with FastAPI, AWS S3, MongoDB, and async worker queues.

This project demonstrates scalable backend architecture, concurrency handling, and CPU vs I/O workload management in Python.

📌 Overview

This system simulates an industrial image processing pipeline where multiple images are uploaded concurrently, stored in cloud storage, queued for processing, and handled asynchronously by worker pools.

The architecture separates ingestion from processing, ensuring high throughput and low latency API responses.

🏗 Architecture

Client
->
FastAPI (Async Ingestion Layer)
->
AWS S3 (Object Storage)
->
MongoDB (Metadata Store)
->
Async Job Queue
->
Worker Pool (Concurrent Processing)
->
Database Status Update

⚡ Key Features

Async FastAPI ingestion

Concurrent image uploads

AWS S3 integration for scalable object storage

MongoDB metadata tracking

Queue-based worker architecture

CPU-bound task handling

Status tracking (queued → processing → completed)

Scalable system design

🧠 Engineering Concepts Demonstrated
1️⃣ High-Throughput API Design

Non-blocking request handling

Immediate acknowledgment of uploads

Decoupled processing pipeline

2️⃣ Concurrency & Performance

Async worker pool using asyncio.Queue

CPU-bound task simulation

GIL-aware multiprocessing strategy (optional extension)

3️⃣ Cloud-Native Design

S3 for object storage

MongoDB for flexible metadata schema

Stateless API layer

4️⃣ System Scalability

Horizontal scaling possible

Worker count configurable

Clear separation of compute and storage

📂 Project Structure
async-image-processing-pipeline/
│
├── main.py              # FastAPI app & endpoints
├── s3_service.py        # S3 upload/download logic
├── db.py                # MongoDB connection & operations
├── worker.py            # Async worker pool logic
├── processing.py        # Image processing logic
├── requirements.txt
└── README.md

🔄 Workflow
Step 1 – Upload

Client uploads one or multiple images.

API uploads files to S3.

Metadata stored in MongoDB.

Job pushed to async queue.

Step 2 – Queue Processing

Worker picks job from queue.

Downloads image from S3.

Performs processing task.

Updates MongoDB status.

🛠 Tech Stack

Python 3.10+

FastAPI

asyncio

AWS S3 (boto3 / aioboto3)

MongoDB

Uvicorn

🚀 Running the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set environment variables
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
S3_BUCKET_NAME=
MONGO_URI=

3️⃣ Run server
uvicorn main:app --reload

📊 Future Improvements

Replace in-memory queue with Redis/Kafka

Add multiprocessing for CPU-bound optimization

Add Docker containerization

Add health monitoring & metrics

Add rate limiting & authentication

🎯 Why This Project Matters

This project demonstrates:

Production-style backend architecture

Understanding of Python concurrency

Awareness of GIL limitations

Cloud-native design principles

Distributed processing fundamentals

It reflects performance-oriented backend engineering rather than simple CRUD development.

📜 License

MIT License
