from kafka import KafkaProducer, KafkaConsumer

# Information sur le cluster Kafka
bootstrap_servers = ["localhost:9092"]

# Information sur le topic Kafka
topic = "chat_channel"

# Information sur le groupe de consommateurs Kafka
group_id = "chat_group"

# Créer le producteur Kafka
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Créer le consommateur Kafka
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, group_id=group_id)

# Abonner le consommateur au topic
consumer.subscribe([topic])

# Boucle de lecture des messages
while True:
    for message in consumer:
        #Traiter le message