import './components/boton-reutilizable.js';
import './components/tarjeta-platillo.js';
import { ModalProducto } from './components/modal-producto.js';

class AplicacionRestaurante {
    constructor() {
        this.contenedorPlatillos = document.getElementById('contenedor-platillos');
        this.instanciaPopover = new ModalProducto();
        document.body.appendChild(this.instanciaPopover);
    }

    async inicializar() {
        if (!this.contenedorPlatillos) return;

        // Escuchar eventos personalizados emitidos desde el Web Component TarjetaPlatillo
        this.contenedorPlatillos.addEventListener('ver-nutricion', (e) => {
            const { datos, x, y } = e.detail;
            this.instanciaPopover.mostrarPopover(datos, x, y);
        });

        this.contenedorPlatillos.addEventListener('ocultar-nutricion', () => {
            this.instanciaPopover.ocultarPopover();
        });

        try {
            const respuesta = await fetch('/api/platillos/');
            const platillos = await respuesta.json();
            this.renderizarPlatillos(platillos);
        } catch (error) {
            console.error('Error al cargar catálogo de platillos:', error);
        }
    }

    renderizarPlatillos(platillos) {
        if (!this.contenedorPlatillos) return;
        this.contenedorPlatillos.innerHTML = '';

        platillos.forEach(platillo => {
            // Instanciar el Web Component hijo que hereda de ComponenteBase
            const tarjetaComponent = document.createElement('tarjeta-platillo');
            tarjetaComponent.configurarDatos(platillo);
            this.contenedorPlatillos.appendChild(tarjetaComponent);
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const app = new AplicacionRestaurante();
    app.inicializar();
});