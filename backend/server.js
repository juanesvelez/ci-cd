const express = require('express');
const mysql = require('mysql2');
const bcrypt = require('bcrypt');
const cors = require('cors');

require('dotenv').config();

// Crear una instancia de express
const app = express();
app.use(cors());
app.use(express.json());

// Configurar la conexión a la base de datos MySQL
const db = mysql.createConnection({
    host: process.env.MYSQL_HOST || 'localhost',
    user: process.env.MYSQL_USER || 'root',
    password: process.env.MYSQL_PASSWORD || 'password',
    database: process.env.MYSQL_DATABASE || 'user_db'
});

// Conectar a la base de datos
db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Conectado a la base de datos MySQL');
});

// Ruta de registro
app.post('/register', (req, res) => {
    const { email, password } = req.body;

    // Verificar si el usuario ya está registrado
    const checkUserQuery = 'SELECT * FROM Users WHERE email = ?';
    db.query(checkUserQuery, [email], (err, results) => {
        if (err) {
            console.error('Error al verificar el usuario:', err);
            return res.status(500).json({ error: 'Error de servidor' });
        }

        if (results.length > 0) {
            // El usuario ya está registrado
            return res.status(400).json({ error: 'El email ya está registrado' });
        }

        // Hash de la contraseña
        bcrypt.hash(password, 10, (err, hash) => {
            if (err) {
                console.error('Error al generar el hash de la contraseña:', err);
                return res.status(500).json({ error: 'Error de servidor' });
            }

            // Creación de usuario en la base de datos
            const createUserQuery = 'INSERT INTO Users (email, password) VALUES (?, ?)';
            db.query(createUserQuery, [email, hash], (err, result) => {
                if (err) {
                    console.error('Error al crear el usuario:', err);
                    return res.status(500).json({ error: 'Error de servidor' });
                }

                res.status(201).json({ message: 'Usuario creado con éxito' });
            });
        });
    });
});

// Ruta de inicio de sesión
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    // Consulta para obtener el usuario con el correo electrónico dado
    const query = `SELECT * FROM Users WHERE email = ?`;
    db.query(query, [email], (err, results) => {
        if (err) {
            console.error('Error al realizar la consulta:', err);
            res.status(500).json({ error: 'Error de servidor' });
            return;
        }

        if (results.length === 0) {
            res.status(401).json({ error: 'Credenciales inválidas' });
        } else {
            // Verificar la contraseña
            const user = results[0];
            bcrypt.compare(password, user.password, (err, match) => {
                if (err) {
                    console.error('Error al comparar las contraseñas:', err);
                    res.status(500).json({ error: 'Error de servidor' });
                    return;
                }

                if (match) {
                    res.json({ message: 'Inicio de sesión exitoso' });
                } else {
                    res.status(401).json({ error: 'Credenciales inválidas' });
                }
            });
        }
    });
});

// Iniciar el servidor
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`El servidor está corriendo en el puerto ${port}`);
});
