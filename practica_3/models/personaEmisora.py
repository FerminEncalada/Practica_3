from models.enumTipoRuc import EnumTipoRuc

class PersonaEmisora:
    def __init__(self):
        self.__id = 0
        self.__apellidos = ''
        self.__nombres = ''
        self.__dni = ''
        self.__direccion = ''
        self.__monto = ''
        self.__tipoRuc = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _monto(self):
        return self.__monto

    @_monto.setter
    def _monto(self, value):
        self.__monto = value
        
    @property
    def _tipoRuc(self):
        return self.__tipoRuc

    @_tipoRuc.setter
    def _tipoRuc(self, value):
        self.__tipoRuc = value
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,
            "direccion": self.__direccion,
            "dni": self.__dni,
            "monto": self.__monto,
            "tipoRuc":self.__tipoRuc
        }
    
    def deserializar(data):
        persona = PersonaEmisora()
        persona._id = data.get("id", None)
        persona._apellidos = data.get("apellidos", None)
        persona._nombres = data.get("nombres", None)
        persona._direccion = data.get("direccion", None)
        persona._dni = data.get("dni", None)
        persona._tipoRuc = data.get("tipoRuc", None)
        persona._monto = data.get("monto", None)  # Esto devuelve None si "monto" no está en data
        return persona

        
    def __str__(self):
        return f"ID: {self.__id}, Apellidos: {self.__apellidos}, Nombres: {self.__nombres}, Dirección: {self.__direccion}, DNI: {self.__dni}, Monto: {self.__monto}, TipoRuc: {self.__tipoRuc}"

    
