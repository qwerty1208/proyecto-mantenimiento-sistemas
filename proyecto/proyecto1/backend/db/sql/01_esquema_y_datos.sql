-- 1. Tabla de Categorías
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Tabla de Platillos
CREATE TABLE IF NOT EXISTS platillos (
    id_platillo SERIAL PRIMARY KEY,
    nombre_platillo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    id_categoria INT REFERENCES categorias(id_categoria) ON DELETE CASCADE,
    calorias INT DEFAULT 0,
    ingredientes TEXT,
    alergenos VARCHAR(255),
    disponible BOOLEAN DEFAULT TRUE,
    imagen_url TEXT
);

-- 3. Insertar Categoría de Prueba si no existe
INSERT INTO categorias (id_categoria, nombre_categoria)
VALUES (1, 'Especialidades')
ON CONFLICT (id_categoria) DO NOTHING;

-- 4. Insertar Platillos de Prueba
INSERT INTO platillos (nombre_platillo, descripcion, precio, id_categoria, calorias, ingredientes, alergenos, disponible, imagen_url)
VALUES 
(
    'Corte Rib Eye Gourmet', 
    'Jugoso corte a la parrilla servido con papas rústicas y mantequilla de hierbas.', 
    380.00, 1, 750, 'Carne de res, mantequilla, finas hierbas, papa', 'Lácteos', TRUE, 
    'https://images.unsplash.com/photo-1544025162-d76694265947?w=500'
),
(
    'Enchiladas Suizas', 
    'Rellenas de pollo deshebrado, bañadas en salsa verde cremosa y queso gratinado.', 
    165.00, 1, 520, 'Tortilla de maíz, pollo, crema, queso manchego, tomate verde', 'Lácteos', TRUE, 
    'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?w=500'
),
(
    'Hamburguesa Artesanal', 
    'Carne sirloin, queso cheddar fundido, tocino crujiente y pan brioche.', 
    195.00, 1, 680, 'Carne sirloin, pan brioche, queso cheddar, tocino', 'Gluten, Lácteos', TRUE, 
    'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500'
)
ON CONFLICT DO NOTHING;