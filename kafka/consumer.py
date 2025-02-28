from confluent_kafka import Consumer, KafkaException

# Cấu hình Kafka Consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-stream-consumer-1',  
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(conf)
consumer.subscribe(['stream-topic'])  

print("⏳ Đang chờ tin nhắn từ Kafka...")

try:
    while True:
        msg = consumer.poll(1.0)  # Đợi 1 giây để nhận tin nhắn
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        print(f'📩 Nhận: {msg.topic()} [{msg.partition()}] {msg.value().decode()}')

except KeyboardInterrupt:
    print("⛔ Dừng consumer...")

finally:
    consumer.close()  # Đóng kết nối khi kết thúc
