from queue_service import image_queue
from db import collection
from datetime import datetime, timezone
import asyncio
from bson import ObjectId


async def worker(worker_id: int):
    while True:
        print(f"Worker {worker_id} waiting for job...")
        job = await image_queue.get()

        print(f"Worker {worker_id} processing {job['image_id']}")

        # Simulate processing
        await asyncio.sleep(3)

        await collection.update_one(
            {"_id": ObjectId(job["image_id"])},
            {
                "$set": {
                    "status": "processed",
                    "processed_at": datetime.now(timezone.utc)
                }
            }
        )   

        image_queue.task_done()
