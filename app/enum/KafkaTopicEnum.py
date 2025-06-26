from enum import Enum

# class syntax
class TopicEnvio(Enum):
    UNIDADES_INTERNCAIONAIS_PGTO = 'Pagamento'
    UNIDADES_INTERNCAIONAIS_TRANSF = 'Transferência'
    unidades_internacionais_pgto = 'Pagamento1'
    unidades_internacionais_transf = 'Transferência1'

    @property
    def hifen_name(self):
        return self.name.replace("_", "-").lower()
