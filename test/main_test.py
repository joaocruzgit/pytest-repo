from app import main
from app.model.kafkaObject import KafkaObject

def test_handler():
    kafkaObject = KafkaObject(topic="unidades-internacionais-pgto", 
                              partition=0, 
                              offset=0, 
                              key="test_key", 
                              value="test_value") 

    response = main.handler(event=kafkaObject, context=None)

    print(response)
    