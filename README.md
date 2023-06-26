# Prerequisiti
 - Caricare i file HTML, qual'ora non ci fossero, su una cartella allo stesso livello del file python
 - Aprire il file con un compilatore
 - Modifica la riga 9        app.config['MAIL_USERNAME'] = 'email@gmail.com'        con l'email con la quale si vuole inviare il codice OPT
 - Modifica la riga 10       app.config['MAIL_PASSWORD'] = 'password'        con la password per i servizi del account gmail che userai per inviare la mail
 - Modifica riga 22        if username == 'email@gmail.com' and password == '1234'      con l'email e la password dell'account di colui che vuole effettuare il login, alla stessa mail verrà poi inviato il codice OTP per l'autenticazione finale
# Funzionamento
 - Lanciare il programma, cliccare sul sull'indirizzo IP che viene generato, si aprirà una pagina HTML con la possibilità di inserire nome utente e password, se entrambi sono riconosciuti dal sistema verrà inviata automaticamente una mail contenente il codice OTP da inserire nella pagina che verrà visualizzata al momento del successo del login, se anche il codice OTP è corretto viene effettuato il Login completo

![immagine](https://github.com/carlobarraco/reposiroty/assets/137286869/6afcc337-c10c-4240-a1f2-3860836f964b)
![immagine](https://github.com/carlobarraco/reposiroty/assets/137286869/e63fdfef-3440-456b-b028-ebdd5fb31bdd)
![immagine](https://github.com/carlobarraco/reposiroty/assets/137286869/c03627fc-74f3-40b3-81a2-9fa842213917)

