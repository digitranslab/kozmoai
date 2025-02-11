# celeryconfig.py
import os

kozmoai_redis_host = os.environ.get("KOZMOAI_REDIS_HOST")
kozmoai_redis_port = os.environ.get("KOZMOAI_REDIS_PORT")
# broker default user

if kozmoai_redis_host and kozmoai_redis_port:
    broker_url = f"redis://{kozmoai_redis_host}:{kozmoai_redis_port}/0"
    result_backend = f"redis://{kozmoai_redis_host}:{kozmoai_redis_port}/0"
else:
    # RabbitMQ
    mq_user = os.environ.get("RABBITMQ_DEFAULT_USER", "kozmoai")
    mq_password = os.environ.get("RABBITMQ_DEFAULT_PASS", "kozmoai")
    broker_url = os.environ.get("BROKER_URL", f"amqp://{mq_user}:{mq_password}@localhost:5672//")
    result_backend = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")
# tasks should be json or pickle
accept_content = ["json", "pickle"]
