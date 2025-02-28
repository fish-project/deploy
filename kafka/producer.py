import time
from confluent_kafka import Producer

# Cấu hình Kafka Producer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-stream-producer'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Gửi thất bại: {err}')
    else:
        print(f'Gửi thành công: {msg.topic()} [{msg.partition()}] {msg.value().decode()}')

# Stream dữ liệu liên tục
i = 0
while True:
    msg_value = f'Streaming message {i}'
    producer.produce(
        topic='stream-topic',
        key=str(i),
        value=msg_value,
        callback=delivery_report
    )
    producer.flush()  
    print(f'Đã gửi: {msg_value}')
    i += 1
    time.sleep(1)  
