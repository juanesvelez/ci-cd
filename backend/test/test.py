import requests
import unittest
import os
import random
import string

class BackendTestCase(unittest.TestCase):

    usuarios_creados = []

    def setUp(self):
        # Configurar la URL base para las solicitudes
        self.base_url = os.getenv("BASE_URL", "http://localhost:3000")

    def random_email(self):
        # Generar un email aleatorio
        email_length = 10
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(email_length)) + "@example.com"

    def random_password(self):
        # Generar una contraseña aleatoria
        password_length = 8
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(password_length))

    def test_registro_exitoso(self):
        for _ in range(5):
            email = self.random_email()
            password = self.random_password()

            # Verificar si el usuario ya existe antes de crearlo
            check_user_url = f"{self.base_url}/checkuser/{email}"
            check_user_response = requests.get(check_user_url)
            if check_user_response.status_code == 200:
                self.skipTest(f"El usuario {email} ya existe en la base de datos")

            url = f"{self.base_url}/register"
            data = {
                "email": email,
                "password": password
            }
            response = requests.post(url, json=data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()["message"], "Usuario creado con éxito")

            # Mostrar por pantalla el usuario creado y el mensaje de registro exitoso
            print(f"Usuario creado: {email}", flush=True)
            print("Registro exitoso", flush=True)

            # Agregar el usuario creado a la lista de usuarios creados
            self.usuarios_creados.append({"email": email, "password": password})

    def test_inicio_sesion_exitoso(self):
        url = f"{self.base_url}/login"

        for usuario in self.usuarios_creados:
            data = {
                "email": usuario["email"],
                "password": usuario["password"]
            }
            response = requests.post(url, json=data)

            if response.status_code == 200:
                self.assertEqual(response.json()["message"], "Inicio de sesión exitoso")
                print(f"Inicio de sesión exitoso para el usuario: {usuario['email']}")

    def test_inicio_sesion_invalido(self):
        email = "test@example.com"
        password = "wrongpassword"
        url = f"{self.base_url}/login"
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["error"], "Credenciales inválidas")
        print("Test - Inicio de sesión inválido exitoso", flush=True)

if __name__ == '__main__':
    unittest.main()
