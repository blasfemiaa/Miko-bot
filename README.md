
### English Version

# Bot in Development

This bot is under development and includes various functions that I update regularly.

## Changelog

### Version 0.1
- Basic bot with Russian Roulette game functionality.

### Version 0.2
- Added functionality to extract text from images and send it in the chat.

### Version 0.3
- Now has the functionality to respond based on the text you send. For example, if you send "miko", it will respond with something. You can add more responses by modifying the logic with `elif` statements or adding new logic.

## Commands

### `!ruletarusa`
- This command activates the Russian Roulette game.
- You must assign a specific role to play with specific members.
- When a round starts, there are 6 randomized turns. If a player "dies," they are muted in the channel. (Currently, unmuting must be done manually.)

### `!textoimg`
- This command allows you to extract text from images and send it in the chat.
- Supports both Spanish and English.
- The image must have good definition. You need to paste the image and use the command to transcribe the text.

### Custom Text Responses
- The bot will respond based on specific text inputs. For example, sending "miko" will trigger a specific response.
- You can add more responses by modifying the logic with `elif` statements or adding new logic in the `on_message` event.

---

### Versión en Español

# Bot en Desarrollo

Este bot está en desarrollo y contiene varias funciones que voy actualizando regularmente.

## Registro de Cambios

### Versión 0.1
- Bot básico con la función del juego de la ruleta rusa.

### Versión 0.2
- Agregada la funcionalidad para extraer texto de las imágenes y enviarlo en el chat.

### Versión 0.3
- Ahora tiene la funcionalidad de responder según el texto que mandes. Por ejemplo, si envías "miko", responderá algo. Puedes agregar más respuestas cambiando la lógica con declaraciones `elif` o agregando nueva lógica.

## Comandos

### `!ruletarusa`
- Con este comando activas el juego de la ruleta rusa.
- Debes asignar un rol específico para poder jugar con miembros específicos.
- Al iniciar una ronda, hay 6 turnos aleatorios. Si un jugador "muere," es silenciado en el canal. (Actualmente, el desilenciamiento debe hacerse manualmente.)

### `!textoimg`
- Con este comando puedes extraer el texto de las imágenes y enviarlo en el chat.
- Soporta tanto español como inglés.
- La imagen debe tener buena definición. Debes pegar la imagen y usar el comando para transcribir el texto.

### Respuestas Personalizadas
- El bot responderá según entradas de texto específicas. Por ejemplo, enviar "miko" activará una respuesta específica.
- Puedes agregar más respuestas modificando la lógica con declaraciones `elif` o agregando nueva lógica en el evento `on_message`.
