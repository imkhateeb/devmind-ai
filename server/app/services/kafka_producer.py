from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

def send_message(topic: str, message: str):
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()
