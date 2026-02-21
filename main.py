import uuid
import asyncio
from typing import List
from worker import worker
from db import collection
from queue_service import image_queue
from datetime import datetime, timezone
from contextlib import asynccontextmanager
from storage_service import save_file_locally
from fastapi import FastAPI, UploadFile, File

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting workers...")

    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(i))
        tasks.append(task)

    yield

    for task in tasks:
        task.cancel()

    print("Shutting down workers...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Server is running"}



@app.post("/upload")
async def upload_images(files: List[UploadFile] = File(...)):
    image_ids = []

    for file in files:
        unique_name = f"{uuid.uuid4()}_{file.filename}"

        file_path = save_file_locally(file.file, unique_name)

        doc = {
            "filename": file.filename,
            "storage_path": file_path,
            "status": "queued",
            "uploaded_at": datetime.now(timezone.utc),
            "processed_at": None
        }

        result = await collection.insert_one(doc)
        await image_queue.put({
            "image_id": str(result.inserted_id),
            "storage_path": file_path
        })

        image_ids.append(str(result.inserted_id))

    return {
        "message": "Images queued",
        "image_ids": image_ids
    }