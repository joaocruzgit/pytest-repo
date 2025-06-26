
from app.enum.KafkaTopicEnum import TopicEnvio
from app.model.kafkaObject import KafkaObject


def handler(event:KafkaObject, context=None):
    
    var = TopicEnvio.__getitem__(event.topic.replace("-", "_"))
    
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }