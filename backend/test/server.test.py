import requests

base_url = "http://localhost:3000"  # Cambia la URL base si es necesario

def test_get_root():
    url = f"{base_url}/"
    response = requests.get(url)

    try:
        response.raise_for_status()
        if response.headers["Content-Type"] == "application/json":
            data = response.json()
            assert "message" in data
        else:
            data = response.text

        assert response.status_code == 200

        print("Prueba exitosa: GET /")
    except Exception as e:
        print(f"Error en la prueba: GET /")
        print(f"Código de estado: {response.status_code}")
        print(f"Contenido de respuesta: {data}")
        print(f"Excepción: {e}")


def test_get_users():
    url = f"{base_url}/users"
    response = requests.get(url)

    assert response.status_code == 200  # Verifica el código de estado

    data = response.json()
    assert isinstance(data, list)  # Verifica que la respuesta sea una lista

    print("Prueba exitosa: GET /users")

# Ejecutar el test
test_get_root()