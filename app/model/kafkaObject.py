class KafkaObject:
    def __init__(self, topic: str, partition: int, offset: int, key: str, value: str):
        self.topic = topic
        self.partition = partition
        self.offset = offset
        self.key = key
        self.value = value

    def __repr__(self):
        return f"KafkaObject(topic={self.topic}, partition={self.partition}, offset={self.offset}, key={self.key}, value={self.value})"