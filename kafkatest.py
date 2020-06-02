# files used to test the kafka server and not for the actual flask api
from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
cluster_name = "34.125.164.1"


producer = KafkaProducer(bootstrap_servers=['10.128.0.21:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)


# Integrate a callback here

# Implement this with keys

.pardoFunction(create the json, after you read it)
apply the window
/ combinebykey()the function
/apply the final transformation


 beam.CombinePerKey(sum))

we write a custom function here that is going to produce the final json 

{"session_id" :{
	"pagevies"
	"session duration"
	"pagesvisited"

},
timestamp:{
	
}}

