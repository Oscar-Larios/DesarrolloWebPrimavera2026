SessionStorage es una herramienta del navegador que permite guardar información temporal en el dispositivo del usuario mientras una pestaña del navegador está abierta. Los datos se eliminan automáticamente cuando la pestaña se cierra. Se utiliza para almacenar información temporal durante la navegación en un sitio web.

Para guardar datos se usa el método `setItem`: sessionStorage.setItem("usuario", "Oscar");
Para obtener un dato se usa `getItem` let usuario = sessionStorage.getItem("usuario");
Para eliminar un dato específico se usa `removeItem`: sessionStorage.removeItem("usuario");
Y para borrar todos los datos almacenados se usa `clear`: sessionStorage.clear();

Si se quiere guardar un objeto, es necesario convertirlo a JSON usando `JSON.stringify`, y al recuperarlo usar `JSON.parse`.

SessionStorage y localStorage pertenecen a la Web Storage API y ambos permiten guardar datos en pares clave–valor mediante JavaScript. Además, solo almacenan datos como texto (strings) y tienen una capacidad aproximada de entre 5 y 10 MB.

La principal diferencia es que **localStorage guarda los datos de forma permanente**, incluso si el navegador se cierra, mientras que **sessionStorage solo guarda los datos durante la sesión de la pestaña**. Además, localStorage comparte la información entre todas las pestañas del mismo sitio, mientras que sessionStorage solo funciona en la pestaña actual.
