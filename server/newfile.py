import pickle

data = b"cosas serializadas"
obj = pickle.loads(data)  # Vulnerabilidad: deserialización no segura


user_input = "print('hola')"
eval(user_input)  # Vulnerabilidad: permite ejecución arbitraria
