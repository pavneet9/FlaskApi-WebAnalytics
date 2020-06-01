#!/usr/bin/python


from kafka import KafkaProducer

cluster_name = "35.226.38.97" # cluster in which kafka & zookeeper are installed  

producer = KafkaProducer(bootstrap_servers=[cluster_name+'-m:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

