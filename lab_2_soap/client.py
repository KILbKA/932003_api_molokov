from zeep import Client

# URL к WSDL сервера (замените на актуальный)
wsdl = 'http://localhost:5000/?wsdl'
client = Client(wsdl)

result = client.service.get_current_time()
print("Текущее время на сервере:", result)