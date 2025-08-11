import pickle

data = b"cosas serializadas"
obj = pickle.loads(data)  # Vulnerabilidad: deserialización no segura
