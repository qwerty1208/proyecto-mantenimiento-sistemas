/**
 * Clase Base abstracta para la creación de Web Components nativos.
 * Facilita la reutilización de código, manejo de Shadow DOM e inyección de estilos.
 * @extends HTMLElement
 */
export class ComponenteBase extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  /**
   * Renderiza una plantilla HTML y una hoja de estilos dentro del Shadow DOM.
   * @param {string} html - Cadena con el contenido HTML del componente.
   * @param {string} css - Cadena con los estilos CSS del componente.
   */
  renderizar(html, css = '') {
    const estilo = css ? `<style>${css}</style>` : '';
    this.shadowRoot.innerHTML = `${estilo}${html}`;
  }

  /**
   * Método de ciclo de vida que se ejecuta al insertar el componente en el DOM.
   */
  connectedCallback() {
    this.inicializarComponente();
  }

  /**
   * Método que deben sobreescribir las clases hijas para configurar lógica inicial.
   */
  inicializarComponente() {
    // Definido en las clases hijas
  }
}