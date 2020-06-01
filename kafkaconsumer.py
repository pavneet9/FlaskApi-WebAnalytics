from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',          #earliest from the start - latest new message - none will have an error if no offsets are bein saved
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


#time when we look for messages
for message in consumer:
    message = message.value
     print('{} '.format(message))


#assign and seek