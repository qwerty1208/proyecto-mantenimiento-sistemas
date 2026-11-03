import { ComponenteBase } from '../core/componente-base.js';

/**
 * Componente Popover que muestra detalles adicionales (ingredientes, alérgenos, calorías)
 * al interactuar con las tarjetas de productos.
 * @extends ComponenteBase
 */
export class ModalProducto extends ComponenteBase {
    constructor() {
        super();
    }

    /**
     * Muestra la ventana flotante con la información del platillo.
     * @param {Object} datos - Objeto con calorías, ingredientes y alérgenos.
     * @param {number} posX - Posición horizontal del ratón.
     * @param {number} posY - Posición vertical del ratón.
     */
    mostrarPopover(datos, posX, posY) {
        const html = `
            <div class="popover-contenedor">
                <h4 class="popover-titulo">Detalles Nutricionales</h4>
                <p><strong>Calorías:</strong> ${datos.calorias} kcal</p>
                <p><strong>Ingredientes:</strong> ${datos.ingredientes || 'No especificados'}</p>
                <p><strong>Alérgenos:</strong> ${datos.alergenos || 'Ninguno'}</p>
            </div>
        `;

        const css = `
            .popover-contenedor {
                position: fixed;
                top: ${posY + 10}px;
                left: ${posX + 10}px;
                background-color: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 1rem;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
                z-index: 1000;
                pointer-events: none;
                max-width: 260px;
                font-size: 0.875rem;
            }
            .popover-titulo {
                color: #d97706;
                margin-bottom: 0.5rem;
            }
        `;

        this.renderizar(html, css);
    }

    ocultarPopover() {
        this.renderizar('');
    }
}

customElements.define('modal-producto', ModalProducto);