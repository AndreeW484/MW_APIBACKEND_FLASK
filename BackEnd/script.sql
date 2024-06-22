-- Crear la tabla `contact`
CREATE TABLE contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(120) NOT NULL,
    country VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);

-- Insertar 20 valores iniciales
INSERT INTO contact (name, phone, email, country, city) VALUES
('Ana Garcia', '+502-1234-5678', 'anita100@hotmail.com', 'Guatemala', 'Guatemala City'),
('Carlos Perez', '+504-2345-6789', 'carlosgogo@gmail.com', 'Honduras', 'Tegucigalpa'),
('Luis Martinez', '+503-3456-7890', 'luismart54@yahoo.com', 'El Salvador', 'San Salvador'),
('Maria Rodriguez', '+505-4567-8901', 'mariarod897@hotmail.com', 'Nicaragua', 'Managua'),
('Jose Hernandez', '+506-5678-9012', 'chepehernandez11@gmail.com', 'Costa Rica', 'San Jose'),
('Juan Lopez', '+507-6789-0123', 'juanito4000@gmail.com', 'Panama', 'Panama City'),
('Sofia Gomez', '+502-7890-1234', 'gomez8@hotmail.com', 'Guatemala', 'Quetzaltenango'),
('Miguel Diaz', '+504-8901-2345', 'migue365@gmail.com', 'Honduras', 'San Pedro Sula'),
('Camila Torres', '+503-9012-3456', 'camilitatower@hotmail.com', 'El Salvador', 'Santa Ana'),
('Ricardo Ruiz', '+505-0123-4567', 'ruizgutierrez896@yahoo.com', 'Nicaragua', 'Leon'),
('Laura Morales', '+506-1234-5678', 'lauramoral100@hotmail.com', 'Costa Rica', 'Alajuela'),
('David Cruz', '+507-2345-6789', 'david.cruz@hotmail.com', 'Panama', 'Colon'),
('Daniela Rivera', '+502-3456-7890', 'danirivers789@outlook.com', 'Guatemala', 'Escuintla'),
('Santiago Jimenez', '+504-4567-8901', 'santijim123@outlook.com', 'Honduras', 'La Ceiba'),
('Valeria Flores', '+503-5678-9012', 'flowers2024@hotmail.com', 'El Salvador', 'San Miguel'),
('Francisco Vargas', '+505-6789-0123', 'francis10000@hotmail.com', 'Nicaragua', 'Granada'),
('Elena Romero', '+506-7890-1234', 'romers1987@gmail.com', 'Costa Rica', 'Heredia'),
('Pablo Ortiz', '+507-8901-2345', 'pablo.ortiz@hotmail.com', 'Panama', 'David'),
('Gabriela Castillo', '+502-9012-3456', 'gabycastle41@gmail.com', 'Guatemala', 'Antigua Guatemala'),
('Jorge Mendoza', '+504-0123-4567', 'jorgemendoza08@yahoo.com', 'Honduras', 'Choluteca');