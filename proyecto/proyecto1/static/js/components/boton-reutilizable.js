import { ComponenteBase } from '../core/componente-base.js';

/**
 * Componente Web ejecutable para botones personalizados que hereda de ComponenteBase.
 * @extends ComponenteBase
 */
export class BotonReutilizable extends ComponenteBase {
    constructor() {
        super();
    }

    inicializarComponente() {
        const texto = this.getAttribute('texto') || 'Aceptar';
        const tipo = this.getAttribute('tipo') || 'primario';
        const enlace = this.getAttribute('enlace'); // <-- ¡Nuevo atributo!

        // Si hay enlace, generamos un <a>, de lo contrario un <button>
        const etiqueta = enlace ? 'a' : 'button';
        const atributoRuta = enlace ? `href="${enlace}"` : '';

        const html = `<${etiqueta} ${atributoRuta} class="boton boton--${tipo}">${texto}</${etiqueta}>`;
        
        const css = `
            .boton {
                padding: 0.6rem 1.2rem;
                border: none;
                border-radius: 6px;
                font-weight: 600;
                cursor: pointer;
                transition: background-color 0.2s ease;
                font-family: inherit;
                display: inline-block; /* Crucial para que el <a> tome dimensiones */
                text-decoration: none; /* Quita el subrayado de los links */
                text-align: center;
                box-sizing: border-box;
            }
            .boton--primario {
                background-color: #d97706;
                color: #ffffff;
            }
            .boton--primario:hover {
                background-color: #b45309;
            }
            .boton--secundario {
                background-color: #4b5563;
                color: #ffffff;
            }
            .boton--secundario:hover {
                background-color: #374151;
            }
        `;

        this.renderizar(html, css);
    }
}

customElements.define('boton-reutilizable', BotonReutilizable);