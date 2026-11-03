import { ComponenteBase } from '../core/componente-base.js';

/**
 * Web Component que representa la tarjeta de un platillo del menú.
 * Hereda metodos y Shadow DOM de ComponenteBase.
 * @extends ComponenteBase
 */
export class TarjetaPlatillo extends ComponenteBase {
    constructor() {
        super();
        this.datosPlatillo = null;
    }

    /**
     * Setea los datos del platillo y desencadena la renderizacion heredada.
     * @param {Object} platillo
     */
    configurarDatos(platillo) {
        this.datosPlatillo = platillo;
        this.inicializarComponente();
    }

    inicializarComponente() {
        if (!this.datosPlatillo) return;

        const { nombre_platillo, precio, imagen_url } = this.datosPlatillo;

        const html = `
            <article class="tarjeta">
                <img class="tarjeta__imagen" src="${imagen_url || 'https://via.placeholder.com/300'}" alt="${nombre_platillo}">
                <div class="tarjeta__contenido">
                    <h3 class="tarjeta__nombre">${nombre_platillo}</h3>
                    <p class="tarjeta__precio">$${precio} MXN</p>
                </div>
            </article>
        `;

        const css = `
            .tarjeta {
                background-color: #ffffff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                cursor: pointer;
            }
            .tarjeta:hover {
                transform: translateY(-4px);
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
            }
            .tarjeta__imagen {
                width: 100%;
                height: 180px;
                object-fit: cover;
            }
            .tarjeta__contenido {
                padding: 1.25rem;
            }
            .tarjeta__nombre {
                font-size: 1.25rem;
                font-weight: 600;
                margin: 0;
            }
            .tarjeta__precio {
                font-size: 1.1rem;
                color: #d97706;
                font-weight: 700;
                margin-top: 0.5rem;
            }
        `;

        // Llama al método herededado de ComponenteBase
        this.renderizar(html, css);
        this._registrarEventos();
    }

    _registrarEventos() {
        const tarjeta = this.shadowRoot.querySelector('.tarjeta');
        if (!tarjeta) return;

        tarjeta.addEventListener('mousemove', (evento) => {
            this.dispatchEvent(new CustomEvent('ver-nutricion', {
                detail: { datos: this.datosPlatillo, x: evento.clientX, y: evento.clientY },
                bubbles: true,
                composed: true
            }));
        });

        tarjeta.addEventListener('mouseleave', () => {
            this.dispatchEvent(new CustomEvent('ocultar-nutricion', {
                bubbles: true,
                composed: true
            }));
        });
    }
}

customElements.define('tarjeta-platillo', TarjetaPlatillo);