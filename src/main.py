from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.kafka.producer import AIOKafkaProducer


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    producer = AIOKafkaProducer()
    yield
    # Clean up the ML models and release the resources
    producer.close()


app = FastAPI(lifespan=lifespan)
