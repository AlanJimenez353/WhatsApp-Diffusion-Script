#Este script toma la lista de mensajes y genera un .txt con los mensajes en formato para luego ser usandos en envioDeMensaje.py
mensajes = [
    "✨ ¡Bienvenido!: 🃏 🃏 Somos Ganamos Casino Online 🃏 🃏. Trabajamos con las plataforma Ganamos.net una de las plataformas más completas que existen, cuenta con más de 2.000 máquinas, caballos, deportivas, casino, etc... además posee póker, bingo, ruleta, blackjack y baccarat (todo online). Te creamos un usuario y contraseña que posteriormente vas a poder ingresar desde el enlace que te enviaremos. Para cargar saldo es mediante transferencias a nuestro banco. Por su seguridad siempre consulte CBU antes de cada carga ya que rotamos. Atendemos las 24hs los 365 días del año. 🕒 Los comprobantes se deben enviar en el momento de realizada la transferencia. ⛔ No está permitido retirar saldo de otros usuarios. ️👤 \n\n 📱 https://wa.me/2233434384 📲",
    "✨ ¡Saludos de bienvenida!: 🃏 🃏 Descubre el mundo de Ganamos Casino Online 🃏 🃏, trabajamos con Ganamos.net, un sitio líder en entretenimiento online con más de 2.000 opciones entre máquinas, apuestas en carreras de caballos, deportes, y juegos de casino. Disfruta también de póker, bingo, ruleta, blackjack y baccarat completamente online. Creamos para ti un usuario y contraseña que podrás utilizar en el enlace que te proporcionaremos. Las recargas se hacen por transferencia bancaria. Verifica siempre el CBU antes de cada transferencia. Atención al cliente disponible 24/7. 🕒 Envía tu comprobante de transferencia justo después de realizarla. ⛔ Prohibido retirar saldo de otros usuarios.\n\n 📱 https://wa.me/2233434384 📲",
    "✨ ¡Te damos la bienvenida a Ganamos Casino Online! 🃏 🃏 En Ganamos.net encontrarás una de las plataformas de juego online más robustas, con más de 2.000 máquinas tragamonedas, apuestas en caballos, deportes y más. Incluye juegos de póker, bingo, ruleta, blackjack y baccarat, todo accesible online. Configuraremos tu cuenta y te enviaremos los detalles para que accedas a través del enlace a continuación. Recarga tu saldo mediante transferencia bancaria y recuerda consultar el CBU por seguridad. Estamos a tu disposición 24/7. 🕒 Recuerda enviar el comprobante de la transferencia inmediatamente. ⛔ Está prohibido hacer retiros de cuentas de otros usuarios.\n\n 📱 https://wa.me/2233434384 📲",
    "✨ Bienvenido a la experiencia Ganamos Casino Online! 🃏 🃏 Conoce Ganamos.net, donde te ofrecemos una experiencia completa con más de 2.000 máquinas, apuestas en deportes, casino en vivo y mucho más. Además, disfruta del póker, bingo, ruleta, blackjack y baccarat todo en línea. Te proporcionaremos un usuario y contraseña para que empieces a jugar inmediatamente a través del siguiente enlace. Para añadir fondos, realiza una transferencia bancaria, y siempre verifica el CBU por seguridad. Atención continua 24 horas al día, 365 días al año. 🕒 Envía los comprobantes de tus transferencias al momento de efectuarlas. ⛔ No se permite la retirada de saldo de cuentas ajenas.\n\n 📱 https://wa.me/2233434384 📲",
    "✨ Recibe un cordial saludo de Ganamos Casino Online! 🃏 🃏 Únete a Ganamos.net, una de las plataformas más completas de entretenimiento online con más de 2.000 máquinas, apuestas deportivas y juegos de casino. Además, cuenta con póker, bingo, ruleta, blackjack y baccarat, todo disponible online. Te asignaremos un usuario y contraseña que podrás utilizar siguiendo el enlace a continuación. Los depósitos se realizan a través de transferencia bancaria, y te recomendamos verificar siempre el CBU por motivos de seguridad. Nuestro servicio al cliente está disponible las 24 horas del día. 🕒 Por favor, envía tu comprobante de transferencia inmediatamente después de hacerla. ⛔ No está permitido retirar fondos de cuentas de terceros.\n\n 📱 https://wa.me/2233434384 📲"
]

# Guardar los mensajes en un archivo de texto
with open('mensajes.txt', 'w', encoding='utf-8') as file:
    for mensaje in mensajes:
        file.write(mensaje + "\n\n")