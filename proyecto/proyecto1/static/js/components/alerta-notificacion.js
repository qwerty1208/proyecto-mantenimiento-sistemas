import { ComponenteBase } from '../core/componente-base.js';

export class AlertaNotificacion extends ComponenteBase {
    inicializarComponente() {
        const mensaje = this.getAttribute('mensaje') || 'Operación exitosa';
        const tipo = this.getAttribute('tipo') || 'exito';

        const html = `<div class="alerta alerta--${tipo}">${mensaje}</div>`;
        const css = `
            .alerta {
                padding: 1rem;
                border-radius: 6px;
                font-weight: 500;
                margin-bottom: 1rem;
            }
            .alerta--exito {
                background-color: #d1fae5;
                color: #065f46;
                border: 1px solid #a7f3d0;
            }
            .alerta--error {
                background-color: #fee2e2;
                color: #991b1b;
                border: 1px solid #fca5a5;
            }
        `;

        this.renderizar(html, css);
    }
}

customElements.define('alerta-notificacion', AlertaNotificacion);