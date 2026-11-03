-- Script idempotente para la creación de esquemas iniciales del sistema de restaurante
-- Diseñado para PostgreSQL (Neon DB)

-- Tabla de Roles
CREATE TABLE IF NOT EXISTS roles (
    id_rol SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(150) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    id_rol INT REFERENCES roles(id_rol) ON DELETE SET NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Categorías de Platillos
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(80) UNIQUE NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla de Platillos (Mapeada para tarjetas y popover interactivo)
CREATE TABLE IF NOT EXISTS platillos (
    id_platillo SERIAL PRIMARY KEY,
    nombre_platillo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    precio NUMERIC(10, 2) NOT NULL CHECK (precio >= 0),
    id_categoria INT REFERENCES categorias(id_categoria) ON DELETE RESTRICT,
    calorias INT DEFAULT 0,
    ingredientes TEXT,
    alergenos TEXT,
    disponible BOOLEAN DEFAULT TRUE,
    imagen_url VARCHAR(255),
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);