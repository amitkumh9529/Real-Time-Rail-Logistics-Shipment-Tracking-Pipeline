import random
import uuid
from datetime import datetime, timedelta, timezone

LOCATIONS = {
    "Chicago": (41.8781, -87.6298),
    "Dallas": (32.7767, -96.7970),
    "Denver": (39.7392, -104.9903),
    "Houston": (29.7604, -95.3698),
    "Atlanta": (33.7490, -84.3880),
    "Kansas City": (39.0997, -94.5786),
    "Memphis": (35.1495, -90.0490),
    "Los Angeles": (34.0522, -118.2437),
}

COMMODITIES = [
    "Automotive",
    "Coal",
    "Grain",
    "Chemicals",
    "Steel",
    "Consumer Goods",
]

EVENT_TYPES = [
    "BOOKED",
    "LOADED",
    "DEPARTED",
    "ARRIVED_HUB",
    "DELAYED",
    "DEPARTED_HUB",
    "DELIVERED",
    "CANCELLED",
]


def utc_now():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.isoformat()


def generate_customer():
    return {
        "customer_id": f"CUS-{random.randint(100000, 999999)}",
        "customer_name": f"Customer-{random.randint(1000, 9999)}",
    }


def generate_train():
    return {
        "train_id": f"TRN-{random.randint(100000, 999999)}",
        "train_number": f"RF-{random.randint(1000, 9999)}",
        "operator": random.choice([
            "National Rail Freight",
            "Continental Freight",
            "United Rail Logistics",
        ]),
    }


def generate_shipment(customer_id, train_id):
    origin, destination = random.sample(list(LOCATIONS), 2)

    now = utc_now()
    planned_departure = now + timedelta(minutes=random.randint(5, 60))
    planned_arrival = planned_departure + timedelta(
        hours=random.randint(8, 72)
    )

    return {
        "shipment_id": f"SHP-{random.randint(10000000, 99999999)}",
        "customer_id": customer_id,
        "train_id": train_id,
        "origin": origin,
        "destination": destination,
        "weight_tons": round(random.uniform(10, 450), 2),
        "commodity": random.choice(COMMODITIES),
        "planned_departure": iso(planned_departure),
        "planned_arrival": iso(planned_arrival),
    }


def generate_freight_event(shipment):
    event_type = random.choices(
        EVENT_TYPES,
        weights=[5, 10, 20, 10, 5, 15, 30, 5],
        k=1,
    )[0]

    return {
        "event_id": str(uuid.uuid4()),
        "event_version": 1,
        "event_type": event_type,
        "shipment_id": shipment["shipment_id"],
        "origin": shipment["origin"],
        "destination": shipment["destination"],
        "weight_tons": shipment["weight_tons"],
        "planned_departure": shipment["planned_departure"],
        "planned_arrival": shipment["planned_arrival"],
        "event_timestamp": iso(utc_now()),
    }


def generate_telemetry_event(shipment):
    location = random.choice([
        shipment["origin"],
        shipment["destination"],
    ])

    base_lat, base_lon = LOCATIONS[location]

    status = random.choice([
        "IN_TRANSIT",
        "IN_TRANSIT",
        "IN_TRANSIT",
        "STOPPED",
        "DELAYED",
        "AT_HUB",
    ])

    speed = {
        "IN_TRANSIT": random.uniform(40, 120),
        "STOPPED": 0,
        "DELAYED": random.uniform(0, 30),
        "AT_HUB": 0,
    }[status]

    return {
        "event_id": str(uuid.uuid4()),
        "event_version": 1,
        "shipment_id": shipment["shipment_id"],
        "train_id": shipment["train_id"],
        "latitude": round(base_lat + random.uniform(-0.15, 0.15), 6),
        "longitude": round(base_lon + random.uniform(-0.15, 0.15), 6),
        "speed_kph": round(speed, 2),
        "temperature_c": round(random.uniform(5, 45), 2),
        "fuel_level_pct": round(random.uniform(20, 100), 2),
        "status": status,
        "event_timestamp": iso(utc_now()),
    }


def generate_dataset():
    customer = generate_customer()
    train = generate_train()

    shipment = generate_shipment(
        customer["customer_id"],
        train["train_id"],
    )

    freight_event = generate_freight_event(shipment)
    telemetry_event = generate_telemetry_event(shipment)

    return {
        "customer": customer,
        "train": train,
        "shipment": shipment,
        "freight_event": freight_event,
        "telemetry_event": telemetry_event,
    }


if __name__ == "__main__":
    import json

    data = generate_dataset()

    print(json.dumps(data, indent=2))