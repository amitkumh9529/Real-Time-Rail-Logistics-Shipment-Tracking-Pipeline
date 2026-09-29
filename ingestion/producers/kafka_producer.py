import json
import time

from kafka import KafkaProducer

from ingestion.generators.rail_data_generator import generate_dataset
from ingestion.validators.schema_validator import validate_event


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    key_serializer=lambda key: str(key).encode("utf-8"),
    acks="all",
    retries=5,
)


def publish(topic, event):
    producer.send(
        topic,
        key=event["shipment_id"],
        value=event,
    )


def main():
    print("Starting Kafka producer...")

    while True:
        data = generate_dataset()

        freight_event = data["freight_event"]
        telemetry_event = data["telemetry_event"]

        if validate_event(freight_event, "freight_event.json"):
            publish(
                "freight.events.v1",
                freight_event,
            )

        if validate_event(telemetry_event, "telemetry_event.json"):
            publish(
                "telemetry.events.v1",
                telemetry_event,
            )

        producer.flush()

        print(
            f"Published shipment {freight_event['shipment_id']}"
        )

        time.sleep(2)


if __name__ == "__main__":
    main()