/**
 * Clase encargada de validar la sesión del usuario.
 */
export class GuardiaAutenticacion {
    /**
     * Verifica si existe un token activo en LocalStorage.
     * @returns {boolean}
     */
    static estaAutenticado() {
        const token = localStorage.getItem('token_sesion');
        return Boolean(token);
    }

    /**
     * Intercepta la navegación y redirige al login si no se encuentra un token activo.
     */
    static protegerRuta() {
        if (!this.estaAutenticado()) {
            window.location.href = '/login';
        }
    }
}