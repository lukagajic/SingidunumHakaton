# People Tracker - Singidunum hakaton 2021
## Uputstvo za podešavanje okruženja i pokretanje projekta
Da biste uspeli da pokrenete aplikaciju u lokalnom okruženju, neophodno je da uradite sledeće:

 1. Morate instalirati **erlang** kao podršku za RabbitMQ message broker. Možete ga preuzeti sa ovog **[linka](https://erlang.org/download/otp_win64_23.3.exe)**.
 2. Morate instalirati RabbitMQ message broker. Možete ga preuzeti sa sa ovog **[linka](https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.14/rabbitmq-server-3.8.14.exe)**.
 3. Morate instalirati Node.js okruženje. Možete preuzeti LTS verziju sa ovog **[linka](https://nodejs.org/dist/v14.16.1/node-v14.16.1-x64.msi)**.
 4. Kada ste instalirali erlang, RabbitMQ i Node.js, možete klonirati GitHub repozitorijum na vašu mašinu.
 5. U korenom direktorijumu projekta, kreirajte Python virtualno okruženje sa komandom `python -m venv venv`
 6. Nakon ovog koraka uđite u folder venv, a zatim u folder Scripts koji se nalazi unutar foldera venv `cd venv\Scripts`
 7. Iz Scripts direktorijuma pokrenite **activate.bat** skriptu kako bi se aktiviralo virtualno okruženje
 8. Vratite se u koreni direktorijum projekta `cd ..\..`
 9. Iz korenog direktorijuma pokrenite preuzimanje svih neophodnih biblioteka koje projekat koristi u virtualno okruženje komandom `pip install -r requirements.txt`
 10. Uđite u folder **node** komandom `cd node` i odatle pokrenite skriptu **app.js** komandom `node app.js`
 11. Otvorite još jedan prozor komandne linije koji vodi do korena projekta.
 12. Pokrenite **app** Python skriptu  komandom `python app.py`
 13. Kada se pokrene Flask Veb server, otvorite Veb pregledač i ukucajte adresu `http://localhost:5000`
