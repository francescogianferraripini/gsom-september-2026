# Speaker notes — Incontro 26

Note per il relatore, una per slide, pronte per l'`<aside class="notes">`.

Sono costruite unendo la specifica (`spec/incontro-26/`), le note già presenti nel deck e i concetti emersi nella spiegazione in aula. Dove la spiegazione a voce ha aggiunto qualcosa — un esempio, una metafora, una conseguenza pratica — il concetto è fuso nella nota; dove non ha aggiunto nulla, la nota resta quella della specifica.

---

## Copertina

Oggi apriamo il primo termine della formula: l'LLM. Il prossimo incontro apre il secondo: l'harness.

In apertura: presentare Mauro Luchetti, che tiene la parte pratica. Avvisare che la lezione è densa e senza sconti, e che la classe è mista: chi ha background di programmazione faccia da moltiplicatore sugli esercizi, lavorando in gruppetti.

Tutto il materiale sta su GitHub — slide, testi da cui le slide sono nate, codice delle esercitazioni, trascrizione. L'invito è a caricarsi il repo su un agente e usarlo: chiedere chiarimenti, cercare gli errori, farsi rifare le figure che non si sono capite. Chiedere all'aula di dire ad alta voce il numero di slide quando me lo dimentico: è quello che tiene allineata la trascrizione al deck.

---

## Sezione 1 — Cosa è un agente?

Tre slide, ~12 min. Che cosa ci si aspetta funzionalmente da un agente, e di che cosa è fatto. Chiude sulla formula, e il passaggio alla sezione 2 si fa a voce.

### Slide 1 — Cosa è un agente? Le aspettative

Slide interattiva: domanda aperta alla classe. Le ipotesi sono semi di discussione, mix di naïf e mature. La nota d'atterraggio compare solo alla fine della discussione.

Fra le ipotesi, quella su cui vale la pena fermarsi è *«che sostituisca una persona»*: è la frase che interessa di più ai vertici aziendali, perché in questi strumenti non riescono a vedere altro che un modo per tagliare teste. Serve come trampolino per il ribaltamento: la definizione vera è più semplice e insieme più potente — un agente **porta a termine un task**, non fa conversazione.

E "portare a termine un task complesso a piacere" vuol dire già quattro cose che torneranno per tutto il corso: saper usare strumenti, agire sulle applicazioni esterne, chiedere quando è in dubbio, accorgersi di aver sbagliato e riprovare.

Qui si dichiara l'obiettivo delle cinque lezioni: gli LLM sono il motore degli agenti, e oggi si apre il motore. Il taglio è l'intuizione profonda del perché funziona, non la cronaca dei modelli: il contorno invecchia in mesi, questo no.

### Slide 2 — Lo spazio delle soluzioni

Il punto non è la mappa, è l'asse verticale. Le storie di produttività riguardano task che hanno una verificabilità deterministica del risultato, indipendentemente dalla complessità: un tempo si scendeva a compromessi su entrambe, oggi resta solo il determinismo.

I due poli da nominare. Da una parte coding e ragionamento matematico: il software compila, non ha bug, fa quello che doveva fare; il teorema è dimostrato o non lo è. Dall'altra il ragionamento strategico aziendale: contesto amplissimo, ragionamento lungo, e nessun modo booleano di dire se la decisione è stata buona o cattiva. (Su quella vaghezza la consulenza strategica ha costruito la propria fortuna — battuta d'aula, non da slide.)

Il nesso da esplicitare, perché è il filo che regge tutto l'incontro: è la verificabilità a rendere **addestrabile** un agente. Se puoi dire "ha funzionato / non ha funzionato", puoi dare una reward. Torna identico alla Slide 37, dove il punteggio lo dà un controllo deterministico e non un umano.

### Slide 3 — Un agente è un sistema composto

La metafora va detta a tre livelli: l'LLM è la CPU — calcola, non decide cosa gira; l'harness è il sistema operativo — il loop, il contesto, i tool; system prompt, tools, KB e skills sono il software installato, ciò che a parità di macchina distingue un agente da un altro.

Aggiungere che l'harness è la cosa che fino a poco fa si chiamava *framework agentico*: è cambiato il nome, non l'oggetto. Sono i pezzi di software attorno al modello — il front-end di un assistente, un ambiente di coding agentico, un copilota — che servono a creare un agente e che vanno configurati.

Qui si dà anche il calendario dei tre incontri sulla formula, ed è il posto giusto: oggi l'LLM, cioè i dettagli interni del motore; il prossimo incontro l'harness più system prompt, tool e skill; il terzo prende un solo blocco, la KB, e lo espande — perché come organizzare l'informazione affinché sia usata da un agente merita una lezione dedicata.

Passaggio a voce verso la sezione 2: oggi apriamo il primo termine della formula, l'LLM. (La mappa dell'harness è la Slide 57: serve ad aprire il prossimo incontro, non questo.)

---

## Sezione 2 — L'LLM: cos'è e come genera

~20 min. È la sezione in cui si fissa il vocabolario — token, contesto, turno, tool call, stateless — e in cui si aprono tutti e tre i loop. Tutto il resto della lezione lo dà per acquisito.

### Slide 4 — Che cos'è un modello linguistico

Prima di entrare conviene un sondaggio: gli LLM li ha già spiegati qualcuno, e per quante ore? La risposta cambia il taglio — se c'è già stato un passaggio, questo diventa un secondo giro, e l'occasione va dichiarata: confrontare le due spiegazioni e tirare fuori i dubbi residui.

Poi la definizione: un LLM assegna una probabilità al prossimo token, dato il contesto che lo precede. "Token" è un tecnicismo che sposta un po' il senso di "parola": si scioglie alla Slide 17.

Il collegamento che dà profondità è la teoria dell'informazione. Il modello è addestrato per essere la formula matematica che comprime al meglio il testo che lo precede. La metafora: una radio che collega la Terra a Marte, banda strettissima e tempi lunghi, dove il messaggio va condensato al massimo. Se hai lo stesso modello linguistico di qua e di là, hai la garanzia matematica di spremere il massimo da quella linea — cioè di aver estratto il massimo significato dalle parole. Prevedere bene *è* comprimere bene.

È il primo dei due fronti della compressione, e va tenuto distinto dall'altro: questo è il modello come compressore di messaggi, e torna alla Slide 34 con la cross-entropy; l'altro è la conoscenza compressa nei pesi, ed è la Slide 30.

Sul contrasto in figura: la distribuzione appuntita (`La capitale della Francia è…`) contro quella piatta (`Il gatto è…`) è la misura di quanto è prevedibile il seguito.

### Slide 5 — La generazione: un token alla volta

L'esempio prosegue deliberatamente il contesto "Il gatto è…" della slide precedente.

Il giro da raccontare: si parte dalla prima parola, il modello genera la seconda, la seconda viene concatenata alla prima, il tutto rientra, esce la terza — fino a quando è il modello stesso a emettere un token speciale che dice *fermiamoci, ho finito*.

Il chiarimento che serve sempre, perché la figura parte da una parola sola: da consumatori non partiamo mai da un contesto vuoto. La nostra richiesta *è* la prima parte della frase. Il meccanismo però è identico: dato quello che gli abbiamo chiesto, srotolare parola per parola, estraendo tutto il significato possibile dal contesto e dal modello.

Il modello non pianifica la risposta: da questo punto di vista è stateless, e ragiona solo in termini di parola successiva.

### Slide 6 — Il golfista

Prima della metafora, va detto su che cosa è stato addestrato il modello puro: i corpus di pretraining — libri, codice, enciclopedie, Wikipedia, forum. (Nota a margine che fa effetto: ci sono aziende che comprano libri usati in grande quantità, li scansionano per costruire corpus sempre più grandi, e poi li buttano.)

Poi il golf, da raccontare per esteso perché è l'immagine su cui si regge metà lezione. È come imparare a giocare guardando tantissime partite: come i grandi giocatori fanno il colpo lungo, e poi, in funzione di dove è atterrato il primo, tirano il secondo. Drive, ferro, pitch, putt — impari le grandi sequenze di colpi, applicate su tutti i campi del mondo. Con quello costruisci la capacità di fare traiettorie.

La chiusa è la cerniera: mirare la pallina verso la buca sarà oggetto del rinforzo, cioè di una seconda fase di addestramento. Qui la buca c'è, ma non la guarda nessuno. In sezione 4 la stessa immagine torna con la mira: è l'RL ad aggiungerla.

### Slide 7 — Il 2° loop: la conversazione

Stesso meccanismo, due scale: a sinistra si aggiunge un token al contesto, a destra si aggiunge un turno alla storia — e in entrambi i casi si rilegge tutto da capo.

L'aggancio storico: ChatGPT, novembre 2022. Ricordare che non faceva nulla — non era un agente, era un chatbot, ci potevi solo chiacchierare. Eppure passare dalla generazione sequenziale di parole a una conversazione ha richiesto di dare al modello una forma di finalismo, una capacità di mirare: verso una conversazione intelligente e utile.

Sulla figura, leggere i tre ruoli come una sola frase da completare: `[system] sei un assistente utile`, `[user] ciao, chi sei?`, `[assistant]` — e da lì in poi il modello si limita a scrivere il testo, parola per parola. Al turno dopo, tutta quella roba, dal `system` fino alla nuova domanda, è di nuovo l'inizializzazione della frase.

Il punto da martellare: al secondo turno il modello è totalmente stateless. Per avere la risposta successiva devi risottomettere da capo tutta la storia precedente, system prompt compreso. Conseguenza immediata, da anticipare qui e da sviluppare in sezione 5: paghi token di ingresso e token di uscita, e ogni turno lo paghi di più, perché ti trascini dietro una storia che si allunga e che viene ri-fatturata.

### Slide 8 — Il 3° loop: la tool call

Un tool solo, per semplicità. Il punto non è il tool: è che il turno non finisce alla prima risposta.

La metafora che chiude il concetto: è come in un quiz dove, se hai dichiarato le tue possibilità, quando non sai qualcosa puoi chiamare da casa. La dichiarazione dei tool nel system prompt è esattamente quello: da lì in poi il modello può decidere se rispondere con quello che sa o chiedere l'invocazione di un tool. Quando lo chiede si ferma; chi riceve la richiesta la esegue e gli restituisce il risultato; lui riparte con quella risposta dentro il contesto.

La riga `[tool]` non l'ha scritta il modello: lui ha solo chiesto, e si è fermato. A eseguire e ad appendere il risultato è stato qualcun altro — ed è il tema del prossimo incontro.

Se in aula c'è chi non programma, dare subito l'esempio concreto prima della meccanica: un tool è una funzione, per esempio "cerca il prezzo di un prodotto in un sistema esterno".

La chiusa forte, che vale come riassunto dell'intera sezione: le capacità intrinseche di un LLM sono queste tre, e non ce ne sono altre. Tutto il resto — tutto quello che facciamo e faremo con l'AI — lo organizza l'harness; dentro, il motore è una cosa che sa completare delle frasi. E quelle frasi o sono completamenti di conversazione, o sono richieste di esecuzione di uno strumento.

### Slide 9 — Perché serve un secondo addestramento

Stesso prompt, due risposte: è la prova concreta che il pretraining da solo non basta.

Il modo di leggerla che funziona: *«Come posso aumentare le vendite?»* non è una frase che di solito ha una risposta. È una frase che nel corpus di pretraining compare, tipicamente, nell'indice di un libro di management — quindi il completamento plausibile sono altre domande, non una risposta. Dopo il secondo giro di addestramento lo stesso modello risponde per davvero, sia pure in modo aneddotico e basandosi solo sui suoi pesi: per aumentare le vendite puoi agire su tre leve — marketing, partnership, e così via.

Il contrasto è tipografico prima che di contenuto: monospaziato sbiadito contro testo pieno. È la stessa macchina, con un obiettivo diverso.

Le due risposte sono le stesse della Slide 36, dove tornano come la coppia che gli umani confrontano: qui è il prima e il dopo, là è il come.

### Slide 10 — Il colpo non basta: serve la mira

È il golfista della Slide 6 con una cosa in più: stessa inquadratura e stessa scala, così si riconosce. Il pretraining insegna il colpo — prevedere il token successivo dato il contesto precedente, nient'altro. Ma un turno di conversazione, o un giro di tool call, ha una meta: serve un addestramento *dopo* il pretraining, che ottimizzi il percorso lungo l'intera traiettoria e non il singolo token.

Il passaggio da fare qui: anche la capacità di *decidere* di chiamare un tool viene dal reinforcement learning. Prima l'RL trasformava un completamento di testo in una risposta conversazionale; adesso addestra il modello a non allucinare quando non sa, e a chiedere invece l'esecuzione di uno strumento esterno — una funzione software esposta dall'harness, che qualcun altro chiama per lui.

E il senso di finalismo non lo impari completando frasi: lo impari stando dentro un contesto operativo simulato, un ambiente aziendale finto in cui il modello completa frasi *per risolvere un problema*. È il seme della Slide 37.

Chiude la sezione 2: i tre loop ci sono tutti, ma due dei tre non nascono dal pretraining. Come gliela si insegni, e quanto costa, è la sezione 4.

Domanda che arriva spesso qui: *l'LLM resterà così, o acquisirà altre abilità?* La risposta ha due tempi. Il primo sono i soldi: i data center in costruzione sono ottimizzati per questa architettura, hardware e software, e ogni miglioramento sarà marginale rispetto all'impostazione attuale. Il secondo è il flywheel: anni di uso intensivo su scala mondiale hanno prodotto le traiettorie su cui si fa l'RL, e più questi oggetti vengono usati, meglio funzionano. Da un feedback positivo di questa forza non si esce a cuor leggero. Il secondo tempo si riprende alla Slide 50.

---

## Sezione 3 — Perché funziona

~40 min, la sezione più lunga dell'incontro. Aprire dichiarando il patto: gli embedding sono il concetto più importante di tutti. E dare una volta la regola di ingaggio del materiale: portate a casa il massimo dell'intuizione, poi prendete queste slide, caricatele su un agente e massacratelo di domande.

### Slide 11 — La base di tutto: a ogni parola il suo vettore

Partire dal fatto grezzo: i computer ragionano per numeri, non per parole. Il passaggio fortissimo, quello che sta alla base di tutto, è stato decidere di associare a ogni parola un vettore.

Vale la pena dire che non è chiaro quanto sia stata virtù e quanto necessità: queste cose funzionano sulle GPU, che sono fatte in un certo modo, e si è deciso di sfruttare quella capacità computazionale. È un'osservazione che torna alla Slide 15 e alla Slide 48 — l'economia dei modelli è economia di GPU.

La riformulazione che dà il senso dell'operazione: voglio trasformare la comprensione e la manipolazione del significato — che è roba di logica e di linguistica, piena di regole e convenzioni — in una serie di operazioni matematiche.

E l'associazione parola/vettore non la scrive nessuno a mano: viene appresa durante l'addestramento.

### Slide 12 — Che cos'è un vettore

Tre letture dello stesso oggetto: una lista di numeri, una freccia, e — se la lunghezza è fissa — soltanto una direzione. È la terza che conta per il seguito.

La metafora che apre la porta: il mondo delle idee di Platone. A ogni parola, a ogni concetto, corrisponde un punto in quel mondo. I mondi delle idee saranno poi tanti — gli spazi sono tanti — ma il concetto resta: il significato *è* una posizione. Spostare la parola è spostare il significato; misurare la distanza è misurare l'affinità; e soprattutto confrontare gli allineamenti di direzione è operare matematicamente sui concetti.

Sul pannello della sfera, la frase da dire: questi spazi sono sfere di raggio 1, e i punti non stanno "dentro" lo spazio ma appoggiati sulla superficie. Il nostro lavoro sarà spostarli avanti e indietro su quella superficie, come uomini che camminano sulla Terra.

Negli embedding le dimensioni sono migliaia: la freccia non si può più disegnare, ma tutto quello che diremo continua a valere.

### Slide 13 — Vettori e prodotto scalare

La meccanica in una riga: moltiplico il primo elemento della riga per il primo della colonna, sommo il secondo per il secondo, e avanti così.

I tre casi, detti come significati e non come numeri. Prodotto scalare alto, vicino a 1: i due puntano nella stessa direzione, vogliono dire la stessa cosa. Zero: sono ortogonali, vogliono dire cose totalmente diverse. Negativo: direzione opposta, e molto spesso uno è il contrario dell'altro.

È la prima delle due primitive — il prodotto scalare è la verifica di vicinanza di significato. E tutto ciò che segue, embeddings, attention, fully connected, è questa operazione ripetuta miliardi di volte.

### Slide 14 — La somma: spostarsi nello spazio

La seconda primitiva, da dire con la stessa formula secca della slide prima: la somma è trasposizione di significato. Il prodotto scalare *misura*, la somma *muove*.

Parti da un punto, aggiungi un vettore, arrivi altrove: è la direzione di quel vettore a decidere dove. Nel disegno le frecce si concatenano invece di partire dalla stessa origine, proprio per rendere la somma un movimento e non un confronto.

Trenta secondi, perché l'esempio vero — re meno uomo più donna — sta nella Slide 16. Qui si fissa solo che sommare è spostarsi: da qui in poi quello spostamento torna ovunque, nel contributo del fully connected che si somma all'embedding, nel vettore di posizione, nei value pesati dell'attention.

### Slide 15 — La scala del calcolo: vettori e matrici

Tre gradini, e il secondo è quello che conta: moltiplicare un vettore per una matrice vuol dire fare tante volte il prodotto scalare e generare un nuovo vettore, che rappresenta l'affinità del mio embedding con tanti concetti **in parallelo**. Una batteria di rilevatori interrogata in un colpo solo. E matrice per matrice vuol dire applicare quella stessa operazione a tanti embedding contemporaneamente.

Questi sono trucchi di velocizzazione, ma è tutto qui il calcolo di un LLM — ed è per questo che le GPU, fatte per moltiplicare matrici, sono il suo motore naturale.

La griglia 4×3 di questo livello è la stessa forma che avranno le matrici Q, K e V dell'attention: chi la riconosce qui non ha bisogno di rispiegazioni là.

### Slide 16 — Embeddings: lo spazio delle idee

Due proprietà: la vicinanza è affinità — concetti simili stanno vicini; le direzioni sono relazioni — king meno man più woman dà queen.

Gli esempi nella versione che funziona in aula: se sommo il concetto di *capitale* al concetto di un *paese*, più o meno atterro sull'embedding della sua capitale. Se prendo il passaggio da uomo a donna e lo applico a *re*, atterro su qualcosa di molto vicino a *regina*.

Due avvertenze da dire ad alta voce, perché tengono onesto il discorso. La prima: gli esempi non sono perfettamente veri, sono molto simili a quello che accade. La seconda: queste regolarità non le ha scritte nessuno — gli embedding si organizzano da soli, e questo accade a valle del training. Tutto quello che stiamo guardando è una macchina già addestrata; all'inizio non funziona niente.

La punchline chiude la slide: un LLM, in fondo, è un manipolatore di embeddings.

### Slide 17 — La tokenizzazione e l'embedding lookup

Il token si definisce per frequenza nel corpus di pretraining: la parola comune ha il suo token; la parola poco comune viene spezzata nelle componenti che la compongono; la parola rarissima finisce nei token delle singole lettere. In figura, `elettroencefalogramma`: una parola, tre token.

La conseguenza che fa alzare la testa a tutti: i modelli sono multilingua, ma il vocabolario è squilibrato. Le parole inglesi più frequenti hanno il loro token; le parole italiane spesso no, e devono comporsi da sottotoken. Siccome si paga a token, usare un LLM in italiano è intrinsecamente più costoso che usarlo in inglese — una tassa sulle lingue che hanno contribuito meno al corpus. Fenomeno simmetrico e interessante: pezzi di token identici fra lingue diverse sono una delle cose che rendono possibile il multilinguismo.

La lookup è letteralmente una moltiplicazione: cercare la riga 28741 nella matrice degli embedding è moltiplicare quella matrice per un vettore one-hot lungo centomila, tutto zeri tranne un 1.

Chiudere col glifo in basso: dentro il token le lettere spariscono — ed è per questo che a un modello riesce difficile contare le lettere di una parola. D'ora in poi diremo: token.

### Slide 18 — Cosa serve, per prevedere la parola successiva

Dirlo subito: questa slide è da rileggere a casa. In aula si legge una volta e si va avanti.

L'esempio che tiene insieme i primi due punti, e che conviene riusare identico fino alla Slide 21: *chi ha segnato il canestro decisivo in quella finale NBA del 1998?* Rispondere *Michael Jordan* non vuol dire solo capire che si sta parlando di pallacanestro — quello è l'attention, cioè estrarre significato dalla relazione fra le parole. Vuol dire anche avere dentro cognizioni fattuali sempre più precise — e quello è il fully connected.

Il terzo punto con la metafora che funziona meglio di tutte: il libro di ingegneria. All'inizio sembra di trecento pagine; di rilettura in rilettura, di esercizio in esercizio, ti accorgi che le cose da sapere sono quattro o cinque, e da quelle ricostruisci tutto il resto. Lo stacking dei blocchi è quello: i blocchi in basso fanno le cose terra terra, più si sale più hanno distillato concetti generali e astratti, e a quel punto "ragionano" — per analogia, per correlazione, per metafora.

Qui si risponde anche alla domanda sull'architettura: il Transformer è del 2017, tutte le reti linguistiche che funzionano davvero ci sono basate, e l'inerzia tecnologica dice che durerà ancora a lungo.

Chiudere sui due vincoli: tutto deve essere computazionalmente denso, perché training e inferenza siano sostenibili; e la scelta autoregressiva parola per parola discende dalla struttura stessa dell'unico dataset abbastanza grande che esista — l'interezza del testo su internet.

I tre punti sono, nell'ordine, attention (slide 23–27), fully connected (20–22) e stacking dei blocchi (19).

### Slide 19 — L'architettura, in un colpo d'occhio

Tre tempi, e vanno fatti lentamente. Il copione:

1. **Blocco nero.** Il modello linguistico è questa scatola: una funzione matematica, calcolata da un computer che costa un sacco di soldi. Entra una frase, esce una distribuzione di probabilità.
2. **Apriamo.** N blocchi tutti uguali, dal basso verso l'alto: astrazione crescente. Tutti uguali nella struttura — cambiano solo i pesi.
3. **Apriamo un blocco.** Due parti. La self-attention: guardare i token precedenti e metterli in correlazione — capire che "il gatto è sul" parla di gatti, e che il *sul* è collegato al gatto. Il fully connected: sapere le cose — che a quel minuto di quella partita il canestro l'ha segnato Michael Jordan.

Una precisazione da fare qui: il modello non prevede la parola, prevede una distribuzione sulle parole successive. Di solito si riaggancia la più probabile, ma si può scegliere anche più in basso — è il flag di temperatura che molti hanno già visto nei chatbot: rende più probabile non scegliere la parola più probabile.

Il canale centrale scorre: ogni sottoblocco non sostituisce l'embedding, gli somma il suo contributo. Dopo la distribuzione, il sampling sceglie il token effettivo. La figura è semplificata: omesse le normalizzazioni e le teste dell'attention.

Se la figura non passa, non ripetere le parole: ripetere il gesto. Blocco uno, blocco due, blocco tre, blocco N — tutti uguali, astrazione.

### Slide 20 — Il fully connected: fanout, gate, compressione

L'indice dei tre stadi, prima degli zoom. Guardo tantissimi concetti in parallelo (fanout); tengo solo quelli che superano una certa soglia (la non linearità, la ReLU); li ricomprimo con matrici che riducono la dimensione, tornando a un embedding della dimensione originale.

La frase che chiude il giro, e che collega il blocco al canale centrale della slide precedente: l'output di questo blocco non sostituisce il vecchio embedding — gli si somma. Lo sposta verso la risposta giusta.

I due punti in fondo dicono dove abita la conoscenza. Ciò che è scritto: gli embedding dei token e le colonne delle matrici, cioè i pattern dei rilevatori e i loro contributi. Ciò che emerge: le regolarità geometriche fra quei vettori, le direzioni-relazione dello spazio delle idee — nessuno le ha scritte, si sono formate perché servivano a predire.

### Slide 21 — Fanout: il matching concettuale

Le immagini che funzionano, in ordine: il fully connected è una batteria di pesi, una mega batteria di fatti, una libreria di similitudini.

Il racconto: entra l'embedding della parola, già arricchito dal significato di quelle precedenti; è il punto di domanda a cui bisogna rispondere. Sale, e trova che questo token parla di basket, di quella squadra, di quella partita; più in basso c'è magari il fatto che era il capitano di quella squadra, e di strato in strato questi concetti si allineano su *Michael Jordan* — e la predizione diventa *Michael*. Quando dovrà generare la parola dopo, sarà già orientato coi vettori verso *Jordan*.

E il contrasto, che spiega la ReLU senza chiamarla per nome: su "il gatto è sul" scattano *animale domestico*, *arriva in un luogo*, *frase al presente*, mentre il contesto giuridico e il linguaggio matematico non scattano affatto, come altre migliaia. Il vettore esce raffinato perché è stato confrontato con qualcosa che, salendo di blocco in blocco, gli arricchisce il significato.

È il rilevatore di affinità della Slide 13, moltiplicato per migliaia.

Domanda che arriva spesso qui: *se faccio un prompt già ben strutturato, è come se arrivassi già con una parola molto arricchita, e rendo più efficiente il resto?* La risposta è al novanta per cento sì. Nei due casi — prompt strutturato subito, oppure conversazione che chiarisce man mano — arrivi comunque a una frase che porta bene la semantica; darglielo di prima botta è soprattutto un tema di ottimizzazione dei costi, non necessariamente di qualità del risultato. Però più la frase è ricca, meglio esprimi la semantica, e meglio quella semantica matcha le categorie dei fully connected per individuare la traiettoria verso la parola migliore. Il temperamento da non togliere: un tempo questa era un'arte; oggi i modelli sono così grossi che capiscono comunque, anche scrivendo male. Ma la competenza sta nei pesi e va sfrucugliata: più il prompt è preciso, più si va nella direzione giusta. Da qui si può anticipare il reasoning (Slide 47): i modelli che "pensano" fanno esattamente questo da soli, buttando fuori parole per espandere il prompt prima di rispondere.

### Slide 22 — Compressione: la sovrapposizione

Il collo di bottiglia: i concetti sopravvissuti al gate vengono ricompressi, con matrici che riducono la dimensione, in un unico vettore della dimensione di partenza. Lo spazio si era espanso col fanout, qui si ricontrae.

La sovrapposizione: più significati coesistono, sovrapposti, nello stesso embedding. Non c'è una cella per concetto — ce ne sono migliaia, sommati.

Ripetere qui la frase del canale centrale, perché è il punto in cui si vede: quel vettore è una direzione nello spazio delle idee, e sommato all'embedding ne sposta il significato. È la stessa geometria della Slide 16, applicata dentro il blocco.

Chiarire anche che questi blocchi sono diversi l'uno dall'altro nei pesi, ma strutturalmente identici e ripetuti: è quello che rende possibile la torre della Slide 19.

### Slide 23 — L'attention: a che cosa serve

Il contrasto con il blocco precedente, detto secco: il fully connected arricchisce; l'attention non arricchisce, monitora la relazione fra le parole. Ed è l'unico punto in cui le corsie si parlano — il fully connected lavora su ogni token per conto suo.

L'esempio che apre il concetto d'ordine, e che torna alla Slide 28: *il cane morde l'uomo* contro *l'uomo morde il cane*. L'ordine cambia radicalmente il significato: le parole valgono anche in funzione della loro posizione reciproca, non solo di sé stesse.

Avvertire che le tre slide che seguono sono la stessa tabella, con una riga in più ogni volta: se le si guarda come tre figure diverse, non si capisce niente.

### Slide 24 — Attention: domande e chiavi

L'esempio è `Il portiere diede un calcio`, e il compito è: sono sulla parola *calcio*, e devo trasformarla nell'embedding che predice la parola successiva. Per farlo devo caricarla del significato delle parole che contano — qui *portiere*, anche perché c'è *diede*.

La meccanica: prendo il mio embedding e lo moltiplico per delle matrici che hanno il ruolo di filtrare quanto *calcio* è relativo a una cosa o a un'altra. Ne escono due vettori che poi allineo, e maggiore è l'allineamento, maggiore è il peso che darò a quella parola.

Le tre proiezioni partono tutte dall'embedding, non l'una dall'altra: Q e K sono ottimizzate — testa per testa — per trovare il token giusto nel contesto precedente. E la Q esiste solo per il token che sta cercando, mentre K e V esistono per tutti: è un dettaglio che tornerà utile alla Slide 40.

La metafora della biblioteca tiene separati i tre ruoli: la richiesta al banco è Q, il match si fa sulle etichette dei dorsi che è K, il contenuto del libro è V e arriva dopo. Ciò su cui fai match non è ciò che ricevi.

### Slide 25 — Softmax: il budget di ascolto

Una riga sola della tabella, e cambia tutto: le affinità grezze diventano percentuali che sommano a 1. È il budget di ascolto che *calcio* distribuisce fra le parole precedenti — e la quota che va a *portiere* è il peso con cui ne assorbirà il significato.

Il fatto da far notare sui numeri: 3.1 contro 1.9 diventa 63% contro 19%. La softmax allarga i divari: è un "max morbido".

La stessa macchina torna all'uscita del modello, quando i punteggi diventeranno la distribuzione sul prossimo token (Slide 29).

### Slide 26 — V: il contenuto del libro

Il terzo volto del token. *Portiere*, come tutte le altre parole, ha un altro mini vettore, calcolato moltiplicando per un'altra matrice, che si porta addosso il **significato** della parola — ciò che consegna, se ascoltato. Quando *calcio* analizza le parole precedenti e scopre che il match casca su *portiere*, in uscita si sarà portato dentro quello che *portiere* aveva da dare: all'uscita dell'attention, *calcio* ha a che fare con lo sport.

La somma pesata è lo spostamento: i value, pesati dal budget di ascolto, si sommano all'embedding, e il significato si muove verso l'interpretazione giusta. È la manipolazione della Slide 22, ma qui guidata dal contesto: sono gli altri token a decidere la direzione.

Secondo tempo, le teste. In ogni blocco non c'è un'attention sola: ce ne sono tante in parallelo, e ognuna estrae caratteristiche un po' diverse. Una può essere concentrata sul dominio — lo sport; un'altra sulla sintassi; un'altra sui riferimenti; un'altra sul tono più o meno aggressivo dato dall'ordine delle parole. Ognuna contribuisce a estrarre il massimo significato dalla frase, per poi confrontarlo con la ricchezza dei fully connected.

### Slide 27 — Lo stesso token, due contesti

La prova. Stessa macchina, stesse matrici di proiezione, altra frase: `ossa forti con il calcio`. Qui lo stesso oggetto matematico carica *calcio* del significato di *ossa* e *forti* — ed è così che si scioglie l'omonimia fra il gioco e l'elemento chimico. Nessuno ha scritto da nessuna parte che "calcio" è ambiguo: l'ambiguità la scioglie il contesto, e lo strumento sono i pesi.

Far notare che a cambiare è solo la riga dei token: tutto il resto della macchina è identico. Nella prima frase un solo token si prende quasi tutto il budget; nella seconda il budget si divide fra due.

La definizione da lasciare all'aula, perché è la sintesi di tutta la sotto-sezione: analizzare una sequenza vuol dire prendere le caratteristiche di ciò che viene prima, e capire quanto portarsele su per andare avanti.

Ed è il punto in cui chiudere l'arco: se avete capito questo, avete capito l'AI di oggi — gli investimenti nei data center, le bolle finanziarie, la posta in gioco geopolitica. L'AI è moltiplicazione di matrici che trasforma vettori per predire la parola successiva. Subito dopo, il riconoscimento onesto: tutto questo funziona solo a valle dell'addestramento, cioè solo se dentro gli embedding e dentro le matrici ci sono i numeri giusti. Come ci si arrivi è la sezione 4 — ma senza aver visto prima la macchina che gira, l'addestramento non si capirebbe.

### Slide 28 — Positional encoding: l'ordine conta

L'attention, per come è fatta, compara solo le parole: nel match Q·K non c'è niente che dica chi viene prima. *Il gatto morde il cane* e *il cane morde il gatto* sarebbero lo stesso sacchetto di embedding.

Il positional encoding è semplicemente un vettore che, all'ingresso della rete, si somma alla parola e la battezza: tu sei la terza parola della frase, quindi vieni prima della quinta e prima della settima.

Il guadagno: non solo *la parola A sta nella stessa frase della parola B*, ma *la parola A stava tre parole prima di B*. Ed è ancora uno spostamento — anche la posizione è una direzione nello spazio delle idee: "gatto, secondo token della frase" è il punto *gatto*, spostato un po'.

È l'innesto già visto nella mappa dell'architettura.

### Slide 29 — Reverse embedding: tornare ai token

È il riassunto dell'intera sezione 3, e conviene farlo esattamente così: il token dell'ultima parola — che poteva essere il punto di domanda a cui rispondere — ha guardato le parole precedenti, ne ha preso un po' di significato, le ha confrontate con fatti e informazioni, ha ricompattato tutto strato dopo strato, e di somma in somma si è spostato verso l'embedding che meglio descrive la parola successiva.

L'operazione finale è l'inversa della prima: all'ingresso da token a vettore, all'uscita dal vettore finale a una preferenza su ogni token del vocabolario. Ancora prodotti scalari: centomila affinità — i logits — che la softmax trasforma nella distribuzione.

L'esempio è quello con cui la lezione è partita: `Il gatto è` — *sul* è la più probabile, ma il modello ha visto tante frasi in cui era *un*, *morbido*, *nero*, *stanco*. E *Parigi* ha logit negativo: dopo "il gatto è", nel suo training set, non c'era mai scritto Parigi. Aver visto tante parole permette di stimare la distribuzione ottimale — e l'affinità non seleziona soltanto, esclude.

Il cerchio del "manipolatore di embeddings" si chiude qui.

### Slide 30 — L'LLM come compressore lossy

Il conto, fatto ad alta voce, è quello che rende evidente il paradosso. Quando leggete che un modello è da ventisette miliardi di parametri, quei parametri sono i numeri che stanno dentro il modello: un vocabolario da centomila voci con mille numeri ciascuna fa già cento milioni di parametri di soli embedding; poi ci sono le matrici Q, K, V e quelle dei fully connected.

Il paradosso: miliardi di parametri addestrati su decine di trilioni di token, e alla fine il modello tira fuori conoscenza fattuale precisa. Non ci sta. Non potrebbe impararla a memoria: è costretto a essere un compressore lossy, e per comprimere così deve aver imparato i principi generali e i collegamenti fra i concetti. Non memorizza: modella.

Le conseguenze da nominare: niente archivio consultabile — nessuna riga di database da leggere, la conoscenza è nei vettori appresi e va ricostruita ogni volta, ed è per questo che il recupero può sbagliare. E le capacità emergenti — ragionamento, analogia, transfer fra domini — non sono programmate: sono un effetto collaterale della compressione.

La conseguenza filosofica è il momento in cui l'aula si sveglia: *i modelli sono intelligenti?* Una delle capacità di chi pensa è ricondurre gli oggetti a principi primi e saperli ricostruire, invece di memorizzare ogni possibile istanza. Quella caratteristica ce l'hanno — solo se impara capendo le cose può comprimere così tanto e funzionare così bene.

La pull-quote in fondo è di Ted Chiang: ChatGPT è un JPEG sfocato del web. E per comprimere così, ha dovuto capire.

### Slide 31 — Conseguenze della compressione

La regola: più il modello è piccolo, più ha dovuto comprimere, e più il singolo fatto si sfoca — a meno che non sia emerso tante volte nel training set.

L'esperimento da proporre all'aula, concreto e verificabile in dieci secondi: prendere un modello anche di punta, dirgli di non cercare su internet, e chiedergli di parlare della propria azienda. Su un'azienda di qualche centinaio di persone ne sa un sacco, ma sbaglia le cose importanti — l'offering, il posizionamento, i numeri — e confonde le tecnologie sostituendole con altre simili. Più il modello è piccolo, più la sfocatura aumenta; più è grande, più l'immagine che restituisce è dettagliata.

La regola pratica è quella in fondo: fidati del framing, verifica i fatti. Le allucinazioni non sono un bug morale del modello: sono il comportamento strutturale di un compressore lossy a cui chiedi di ricostruire ciò che non ha memorizzato bene.

### Slide 32 — MoE: non tutti i pesi lavorano sempre

Il perché, nell'ordine giusto: la maggior parte dei parametri sta nei fully connected, perché è lì che stanno i fatti e le conoscenze episodiche — ed è anche la parte più costosa da calcolare, mentre per un dato token la maggior parte dei rilevatori resta muta. Allora i pesi si spezzano in esperti: durante l'addestramento si danno incentivi perché dentro un blocco finiscano informazioni dello stesso dominio — non lo si impone esplicitamente — e in esecuzione un piccolo router decide a chi mandare ogni token. Le matrici si moltiplicano solo sui sottoassiemi che servono.

La domanda che arriva quasi sempre è sul risparmio di RAM, e la risposta va tenuta pronta: una GPU ha due memorie — una abbondante e lenta, e una locale e veloce dove avviene il calcolo, che è sempre la strozzatura. Senza questi trucchi, per fare le moltiplicazioni devi trasferire tutti i pesi dalla lenta alla veloce. Con il mixture of experts sai a priori che, se si sta parlando di sport, devi portare su solo il blocco dello sport: il codice civile ugandese non serve, e comunque avrebbe attivazioni sotto soglia.

Vale la pena tenere il disclaimer: la parte sul traffico fra RAM lenta e RAM veloce è una ricostruzione, e potrebbe non essere ultra precisa; di sicuro però in questo modo si risparmiano pezzi di calcolo. Il risultato è modelli enormi nei parametri totali, con un costo per token da modello piccolo.

Da qui si annuncia la KV cache (Slide 40): stesso genere di trucco, e stesso effetto sul mondo reale.

---

## Sezione 4 — Come viene addestrato

~24 min. Tre fasi: da completatore di testo, a conversatore, a modello che sa volere i tool.

L'attacco che funziona è il ribaltamento: finora vi ho descritto un modello che funzionava già; ma all'inizio, nelle sue matrici, ci sono numeri a caso, e butta fuori probabilità a caso. Bisogna immaginare un processo con cui, libro dopo libro, diventa sempre più bravo.

### Slide 33 — Le tre fasi

Slide-mappa: verrà richiamata alle slide 34, 36 e 37 evidenziando lo stadio corrente.

La frase d'inquadramento: quello di cui abbiamo parlato finora — il completamento di frasi — è il pretraining, e produce un modello linguistico puro. Per trasformarlo in qualcosa che sa parlare servono altre due fasi, entrambe di reinforcement learning: l'RLHF e poi l'RL agentico.

Il dettaglio che rende la pipeline: ognuna delle tre parte dal modello prodotto dalla precedente. È sempre la stessa rete, trasformata tre volte — mai ricostruita da zero.

### Slide 34 — Pretraining: indovinare il prossimo token

Il gioco, raccontato sull'esempio di sempre: gli do `Il gatto è`, gli nascondo il resto della frase, gli faccio prevedere la parola successiva. All'inizio dirà probabilità a caso. Io premio: care matrici, andatevi a toccare in modo da alzarmi la probabilità di *sul* e deprimere quella di tutte le altre. Il punteggio è la cross-entropy — quanta probabilità hai dato al token che era davvero lì. La correzione è backpropagation e gradient descent: un meccanismo assolutamente stupido, matematico e informatico, che va a toccare gli embedding, le matrici Q, K, V e i rilevatori dei fully connected.

La metafora del cane, con la correzione che chiarisce mentre fa ridere: quando fa la cosa giusta gli dai il biscotto. Solo che il pretraining è un po' più violento — quando sbaglia, oltre a non dargli il biscotto, gli dai anche le botte: devi alzare la probabilità giusta *e* abbassare tutte le sbagliate. (Nessun animale è stato maltrattato per questa presentazione.)

Il punto sottile: il giudizio è sul singolo token successivo, ma ciò che alla fine viene stimata è l'intera distribuzione.

Chiudere sulla scala della striscia in basso: tutto questo, ripetuto su venticinque-cinquanta trilioni di token. E ricordare che minimizzare la cross-entropy è letteralmente comprimere: è il fronte 1 della Slide 4, la radio per Marte.

### Slide 35 — Gradient descent: sbaglia, misura, correggi

L'errore è un paesaggio: ogni punto è una configurazione dei pesi, l'altitudine è quanto il modello sbaglia. Il gradiente dice, per ogni singolo peso, in che direzione muoverlo per sbagliare un po' meno. Un passetto, e si ricomincia — nessuna comprensione, solo la pendenza locale, seguita miliardi di volte su miliardi di pesi insieme.

Detto in modo operativo: si calcola la media degli errori di predizione e si modificano i pesi interni, cioè i valori di quelle matrici, per convergere verso un modello addestrato.

L'unica cosa da aggiungere, perché serve tre volte nelle prossime slide: è lo stesso identico metodo per tutte e tre le fasi. Cambia solo il punteggio da migliorare — cross-entropy, reward model, controllo deterministico.

### Slide 35b — Nasce il 1° loop

Il pretraining lascia una capacità sola: dato un contesto, qual è il prossimo token. Ripetuta, quella capacità *è* la generazione — genera un token, lo accoda al contesto, rigenera, fino a STOP. È il loop della Slide 5. Con questo soltanto il modello continua un testo: non risponde a un turno, e non esegue niente. Ottimizza il colpo, non il percorso: è il golfista senza mira della Slide 6.

Il ragionamento che chiude il cerchio meglio della figura, e che vale la pena fare proprio qui: perché si è partiti da un puro modello linguistico? Perché è impossibile addestrare a fare una bella conversazione uno che non parla la lingua. Serviva un metodo di pura forza bruta — l'architettura Transformer e il task semplicissimo dell'indovinare la parola successiva — per costruire una base che capisse la lingua e sapesse qualche concetto del mondo. Solo dopo si può passare alla fase successiva: solo quando sai fare decentemente il loop di generazione, puoi essere addestrato a fare una buona conversazione.

Prima delle tre slide-anello: la stessa figura torna alla 36b e alla 38, ogni volta con un anello in più acceso. Dei tre, il pretraining ne accende uno solo — il più interno.

### Slide 36 — RLHF: arriva la mira

Il problema è quello della Slide 9, riletto dal lato del *come*: solo dopo avere un modello che capisce la lingua puoi creare segnali nuovi, con cui premiarlo quando la sequenza di parole dopo un turno di conversazione è una risposta intelligente.

Perché serve un trucco: per il next-token hai esempi infiniti e gratis — ogni frase di ogni enciclopedia di tutta internet è un esempio, con la sua parola successiva già lì. Ma per dire se una conversazione va bene o no serve un giudizio umano, ed è un task cognitivo che non si produce a quella scala.

La storia che regge la slide, e che va raccontata perché è vera ed è scomoda: all'inizio degli anni Venti il lavoro di etichettatura è stato portato in Kenya, dove le persone che parlano inglese costano meno al mondo. Hanno preso abbozzi di conversazione generati dalle prime versioni dei modelli puri e hanno chiesto: per una domanda come *come posso aumentare le vendite*, è meglio la risposta A o la risposta B? Migliaia di casi, un ranking, due lire a quelle persone, e poi a casa.

Con quel training set — un paio di milioni di preferenze — si addestra un modello intermedio che non sa rispondere, ma sa giudicare: un pignolino, un puntacazzista, che dice se una risposta è buona o no. Quello poi lo fai girare gratis su milioni di domande e risposte nuove, e quel feedback ottimizza il modello linguistico principale.

Il punto critico da non perdere: il modello non ottimizza verso il giudizio umano — ottimizza verso la *stima* che il reward model fa di quel giudizio. Il golfista della Slide 10 ora mira alla buca, ma la bandierina gliel'ha piantata il reward model.

Nota storica: novembre 2022, ChatGPT. Non un nuovo modello — GPT-3 esisteva dal 2020 — ma un nuovo modo di addestrarlo a conversare.

### Slide 36b — Nasce il 2° loop

Quello che l'RLHF aggiunge non è vocabolario: è la **forma** della risposta. Il modello smette di continuare il testo e comincia a rispondere a un turno.

La formula compatta: l'utente scrive, il modello lavora, la risposta si accoda alla storia, e si ricomincia. È il loop della Slide 7. E a ogni giro si rispedisce tutto: l'API non ricorda niente, la storia la rimette il chiamante, per intero, ogni volta.

Far notare a voce il vuoto in mezzo: fra "il modello lavora" e "la risposta si accoda" non c'è ancora niente. Il modello sa parlare, non sa ancora agire — per quello serve la terza fase, ed è lo spazio che la Slide 38 riempirà.

### Slide 37 — RL agentico: traiettorie

È qui che si risponde alla domanda che l'aula pone quasi sempre in sezione 2 — *come fa il modello a capire che non sa, e quindi a chiedere aiuto?* Non lo capisce per introspezione: ha imparato che chiamare un tool al momento giusto è ciò che fa vincere.

Cambia l'unità di giudizio: non più la frase migliore, ma la traiettoria che completa il task — n chiamate a sistemi esterni, una dopo l'altra. L'esempio concreto è quello della figura: *trova il prezzo e aggiornami il foglio*. Il modello deve pensarci su, cercare il prezzo, leggerlo da dove l'ha trovato, scriverlo sul foglio. Andare a scrivere direttamente il risultato è un percorso sbagliato: non è la risposta a essere sbagliata, è la sequenza di passi. E la definizione che ne esce: un agente è quella roba che decide di fare cose — e va addestrato a decidere uno step dopo l'altro nel modo giusto, perché ha un finalismo, cioè capisce dalla domanda il fine che deve darsi.

Il punteggio non lo dà un umano: il task è verificabile, e un controllo deterministico dice se è stato completato. È la differenza con la slide prima — niente reward model. Il GRPO confronta i punteggi di più tentativi con la loro media, e quel *vantaggio* è ciò che aggiorna i pesi; la reward risale la traiettoria vincente e premia ogni passo, tool call comprese.

Come si ottengono i segnali, due strade. La prima: sandbox — ambienti in cui il modello gira, fa le cose, e il risultato è verificabile. È il ponte con la Slide 2: la verificabilità deterministica è ciò che rende un task addestrabile. La seconda: il mondo — dai il modello a tutti, gratis; le persone lo usano e tu capisci da come reagiscono se ha lavorato bene. A volte il giudizio te lo chiedono esplicitamente col pollice; ma anche interrompere una risposta a metà è un segnale che quella risposta non andava. Le traiettorie di tutti vengono raccolte, e sono quelle che migliorano l'edizione successiva del modello.

Il dato che chiude, e che prepara la Slide 50: ci sono provider che offrono l'agente a prezzo pieno, e a un decimo del prezzo se dai il permesso di usare le tue traiettorie per addestrare i loro modelli. Superata una certa soglia, la base utenti è la cosa più preziosa che un provider possa avere.

### Slide 38 — Nasce il 3° loop

Terza e ultima slide-anello: la corona di mezzo si riempie, e il diagramma è completo. La meccanica è già stata vista alla Slide 8 — qui si dice che quel giro adesso ha un nome e una provenienza: nasce dalla terza fase di addestramento.

I tre punti da richiamare in breve. Una tool call è testo: il modello emette una richiesta strutturata — nome del tool, parametri — e si ferma. Il modello può volere solo i tool che conosce: l'elenco, con nome e descrizione, gli viene dato in apertura di contesto. E il giro: qualcuno esegue, il risultato rientra nel contesto, il modello riparte, fino a task completato.

La nota in basso è il cliffhanger, e va detta perché è il ponte con il prossimo incontro: il modello sa solo chiedere. Chi esegue davvero — chi fa parsing, dispatch, sandbox — è l'harness.

---

## Sezione 5 — Lo scenario, più o meno completo

~30 min. L'attacco è quello giusto: adesso una carrellata di elementi di scenario, ma i concetti principali sono già stati dati tutti. Dichiararlo libera l'aula per le domande residue: farle qui, prima di partire.

### Slide 39 — L'API: come si parla al modello

La premessa da dare prima del JSON: non potete mai parlare con un modello direttamente. Quella roba sta su schede, organizzata per servire tanti utenti in contemporanea; l'inferenza è un'arte oscura e costosissima, i data center si costruiscono per l'inferenza, e sopra ci sono mille ottimizzazioni. Voi parlate con un'API: un endpoint su internet.

Poi il punto didattico: la struttura dell'API riflette esattamente la struttura del modello. Il loop interno di completamento è gestito dietro l'endpoint; quello che si vede è il system prompt, i ruoli, la conversazione. Sul system prompt, la precisazione che anticipa il prossimo incontro: sono le istruzioni generali, e il reinforcement learning ha lavorato molto perché vengano scavalcate il meno possibile.

La prova della statelessness, che colpisce più della definizione: potete cambiare a posteriori il contenuto dei turni precedenti, e il modello si baserà su quello che gli rimandate. Non c'è sessione, non c'è persistenza — nessun identificatore di sessione, da nessuna parte.

Due precisazioni storiche, in piccolo: la primissima API di OpenAI (2020) era ancora più semplice — un solo campo `prompt`, una stringa di testo; il formato con `messages` e i ruoli arriva nel 2023. Le API più recenti offrono anche uno stato lato server, ma opzionale: il modello mentale che conta resta questo. Il nome del modello nell'esempio non conta — conta la forma della chiamata.

Chiudere nominando il protagonista del prossimo incontro: è l'harness a gestire tutto questo, chiamando l'LLM attraverso queste API.

### Slide 40 — Il contesto ha un costo

Presentarla per quello che è: roba tecnica che impatta le economie reali in modo fortissimo.

Il costo è quadratico: ogni nuovo token fa Q·K con tutti i precedenti — raddoppi il contesto, quadruplichi il lavoro. Il prefill è il costo iniziale di "leggere" il prompt: calcolare K e V di ogni token, a ogni strato.

Il meccanismo della cache in una frase: siccome le cose vengono generate parola per parola, la generazione del token successivo è totalmente basata su calcoli già fatti per i token precedenti. Allora quegli stati interni si salvano, e al giro dopo si ricaricano invece di ricalcolarli. Dei token precedenti non si rifà più nulla — né le proiezioni di K e V, né, soprattutto, il passaggio dai fully connected layer, che è la parte più costosa. Ogni giro del primo loop paga solo il token nuovo.

Funziona perché la masked attention rende il passato immutabile: K, V e fully connected dei token precedenti non cambiano mai. Le Q del passato invece non si salvano affatto, perché non servono più: servivano solo a produrre l'output di quel token, che non può più cambiare.

I due fatti concreti che rendono reale la cosa, e che fanno presa più della griglia. Il primo: la conversazione ripresa il giorno dopo. Il primo turno è lentissimo, perché la cache è stata buttata per far spazio ad altri e va rifatto tutto il prefill — a volte è il prodotto stesso ad avvisarti che riprendere quella conversazione ti mangerà molti token. Il secondo: tenere in cache tutto questo costa RAM, chi costruisce data center si è preso la RAM disponibile e ha dettato ai produttori come farla — ed è uno dei motivi per cui il telefono nuovo costa molto di più.

### Slide 41 — L'API è stateless: cosa significa davvero

L'API non conserva stato: a ogni turno il contesto completo — system prompt, storico, nuovo input — viene inviato da capo. E il contesto cresce con la conversazione: non paghi la domanda, paghi tutto quello che è stato detto finora.

La lettura delle curve, nell'ordine che funziona: il provider, senza cache, avrebbe un costo più che lineare; con la cache il suo costo diventa incrementale, perché processa solo i token nuovi. L'utente invece, se non usa esplicitamente la cache, rimanda tutta la storia a ogni turno — quindi paga molto di più, e cresce con la conversazione. La forbice fra le due curve è tutto il valore della KV cache.

Il costo di un turno, e la qualità della risposta, dipendono dalla dimensione cumulativa del contesto, non dalla singola domanda.

Domanda che arriva spesso qui: *conviene ricominciare una chat da capo invece di continuare quella lunga?* La risposta è: dipende. Se lo stato della conversazione a cui sei arrivato è uno stato di qualità — hai tirato fuori roba, avete capito insieme — andare avanti da lì conviene. Ma se riprendi il giorno dopo una conversazione lunga, la cache nel frattempo è stata cancellata, e quella fase di ricaricamento costa tanto, soprattutto in computazione. La pratica operativa da raccontare: quando si arriva a un punto di consistenza, farsi scrivere un markdown con quello a cui si è arrivati, salvarlo, e al giro dopo ripartire da lì — è il documento che rappresenta al meglio lo stato. È anche un primo assaggio di progressive disclosure, che è materia del terzo incontro.

### Slide 42 — Il modello è stateless: il contesto è tutto

Da raccontare a voce, all'apertura della slide: il protagonista di «Memento», amnesia anterograda. Ricorda la vita prima dell'incidente, ma ogni nuovo ricordo svanisce in minuti. Sopravvive scrivendo tutto su Polaroid e tatuaggi: ciò che gli serve sapere deve essere fisicamente davanti ai suoi occhi, ora. Un LLM funziona così — il training è la "vita prima", enorme ma congelata; tutto il resto esiste solo se è nel contesto, in questo istante.

Nessuna memoria interna: a ogni chiamata il modello rilegge tutto da capo. La KV cache è un risparmio di calcolo, non un ricordo.

Sulla figura, la cosa da far notare perché serve alla Slide 44: la pila non cresce solo di conversazione. Turni, dichiarazioni dei tool, tool call, risultati — ogni giro dei tre loop appende qualcosa, e quella roba lì dentro resta. Più ci sono state chiamate a tool con le loro risposte dai sistemi, più il contesto è cresciuto.

E abbiamo visto che il contesto costa — vedremo tra poco che, oltre a costare, a un certo punto inizia a far male.

### Slide 43 — Il modello è figlio dei suoi training set

La formulazione più forte è anche la più corta: il modello *è* un bias. La sua capacità di prevedere è l'aver capito il bias del testo su cui è stato addestrato. Addestrato su fonti equilibrate, ricche e varie, ti dà una risposta realistica; addestrato su testi estremisti, parlerà da estremista. Non c'è nulla che non sia nei training set.

Il cut-off: il mondo del modello si ferma alla data di raccolta dei dati; di ciò che accade dopo, nei pesi non c'è nulla.

Il passaggio sul carattere va fatto pesare: anche *come* si comporta, e cosa risponde volentieri, viene da un training set — le preferenze umane stimate dal reward model. Chi fornisce il feedback plasma l'AI, con implicazioni etiche, geopolitiche e di business. È un tema di tenuta democratica, non solo tecnico: quando un singolo attore controlla il proprio modello, controlla anche i valori che gli sono stati insegnati nel reinforcement learning. Il modello che usi non è "l'AI": è una particolare AI, addestrata con particolari valori da particolari persone.

Se serve un'immagine: i bambini dell'esperimento attribuito a Federico II, cresciuti senza che nessuno parlasse loro. Un modello impara a ragionare esattamente così — da ciò che gli è stato fatto sentire, e da nient'altro.

Il box finale è il rovesciamento: la conoscenza sui modelli fa parte dei training set, quindi un'AI ha letto i paper che descrivono il proprio funzionamento interno. L'uomo non sa progettare un cervello; un'AI ha conoscenza di dettaglio del proprio.

### Slide 44 — Context rot

Il visual attuale è uno stand-in: la specifica prevede qui il grafico esterno sul degrado con contesto lungo. Sostituirlo prima della lezione.

Il modo di raccontarla che tiene insieme costo e qualità in un colpo solo: più è lunga la conversazione, non solo costa di più in prefill — peggiora anche la performance. E "conversazione" qui vuol dire tutto quello che sta nel contesto, non solo quello che vi siete detti: ci possono essere mille altri testi, in particolare le chiamate ai tool e le loro risposte.

Il perché: il budget di attenzione — la softmax della Slide 25 — si diluisce su migliaia di token. Tutto ascolta un po', niente abbastanza. L'analogia umana che chiude il concetto: come tutti noi, ci ricordiamo meglio le ultime parole che ci siamo detti, o le primissime. Il mezzo lo perdiamo.

Le regole pratiche: nuovo compito, nuova chat — "continuare" una conversazione lunga per comodità peggiora, non migliora. E non riempire: seleziona ciò che entra.

La definizione operativa da mandare a memoria, perché è la sintesi di tutta la sezione: l'arte di creare agenti è riempire il contesto con tutto e solo — e senza ripetersi — le informazioni e le capability necessarie al modello per dare la risposta o l'azione migliore.

Bel modo di chiudere: è un gioco di equilibri fra due spinte opposte, chi vuole dare tanto contesto perché più semantica si esprime meglio si viene capiti, e chi vuole darne poco per costo e per qualità. Hanno ragione tutti e due, e l'equilibrio lo governa qualcuno fuori dal modello: l'harness.

### Slide 45 — I tool accelerano il context rot

Stesso fenomeno della slide precedente, con l'acceleratore: la 44 dice che il contesto degrada, questa dice che i tool lo riempiono molto più in fretta. Il confronto fra le due pendenze — lineare e lenta a sinistra, a scalini e ripida a destra — è tutta la figura.

Le tre regole, che sono le indicazioni azionabili della sezione. Esporre solo i tool necessari: ogni definizione paga un costo fisso in contesto, anche se quel tool non viene mai chiamato. Dimensionare i tool result: un tool che restituisce cinquantamila token grezzi non è un tool ben progettato, è un carico. Meglio tool specifici che generici: uno che fa una cosa sola viene anche scelto con più precisione.

La cornice: i tool sono la risposta al limite più evidente del modello da solo — non sa quello che non sa, e non può agire nel mondo. Ma ogni tool call deposita nel contesto il suo risultato, e lì resta per tutta la sessione.

### Slide 46 — Multimodality

Tutta la spiegazione si aggancia a quello che è già stato detto: la parola aveva un significato, cioè un vettore. Bene — si prende un'immagine, la si taglia in tessere, a ogni tessera si dà un embedding, e quegli embedding si ricompongono prima di entrare nel modello linguistico principale. Una patch entra come entrerebbe un token.

La parte notevole, ed è giusto chiamarla così: gli embedding che nascono da un'immagine finiscono vicini alle parole che quell'immagine descrivono. Stesso spazio, stesse coordinate — il significato è la posizione, non il mezzo.

La chiusa: vale per le immagini, per l'audio, per il video. Il concetto di base è sempre lo stesso collegamento — da parola a embedding, da pezzetto di immagine a embedding, da pezzetto di suono a embedding, da sequenza di immagini compresse a embedding. Alla fine, vedere un documento, vedere una foto e leggerne il testo diventano la stessa cosa: per questo lo stesso modello può leggere un contratto e guardarne la scansione.

### Slide 47 — Reasoning

Pensare è generare: prima di rispondere, il modello genera token di ragionamento, che restano nel contesto ma non sono la risposta. Invece di essere noi a spiegare bene il problema, si può triggerare il modello perché sia lui a buttare fuori parole — ragionando, espandendo il prompt, sviscerando l'argomento — e a rispondere solo dopo.

Da dove viene: è ancora RL, e sono premiate le traiettorie di pensiero che arrivano alla risposta giusta.

I due fatti economici, che sono il motivo per cui questa slide sta in sezione 5 e non in 3. Si pagano: quei token si accodano al resto della conversazione come tutti gli altri, quindi più qualità significa più calcolo *alla domanda*, non al training. E si possono dosare: si è visto che si possono dare al modello budget molto precisi di token di riflessione interiore. È su questo che si reggono molte delle economie alla base degli investimenti in capacità di calcolo — qualità che si compra a consumo.

Sull'esempio in figura, meno 25% e poi più 25% su ottanta euro: far notare che la risposta intuitiva è anche quella sbagliata. Si vede *a che cosa serve* il ragionamento, non solo che c'è.

È sempre il primo loop: semplicemente, lo STOP arriva molto più tardi.

### Slide 48 — I costi: training, inferenza, distillazione

Due economie diverse e un ponte. Il training è un investimento una tantum ed enorme: mesi di cluster di GPU, ordine delle decine di milioni. Dallo stesso foundational model si addestrano poi più varianti via RL — conversazionale, coding, agentica — e il grosso dell'investimento si paga una volta sola. L'inferenza invece sono centesimi per chiamata moltiplicati per miliardi di chiamate: è lì che si gioca il margine.

Il ponte è la distillazione, e in aula è la parte che merita più tempo: da un modello grande e costoso si generano gli esempi su cui si addestra un modello piccolo ed economico. Qualità simile, costo per token molto più basso, perché ha meno parametri da calcolare. A volte si distilla su capacità specifiche — stessa logica del MoE della Slide 32: modelli più piccoli e più mirati.

L'aneddoto che rende viva la slide, da dare per quello che è, cioè un sospetto diffuso e non una certezza: è così che si ritiene vengano addestrati alcuni modelli piccoli — interrogando in massa i modelli grandi altrui per farsi generare il training set, e distillandosi poi il proprio modello locale. Torna alla Slide 50: le traiettorie sono il valore, e chi le ha se le tiene.

La nota in fondo è l'aggancio alla Slide 15: tutto è moltiplicazione di matrici, quindi l'economia dei modelli è, in fondo, economia di GPU.

### Slide 49 — Il prezzo per token

Le tre regole. I token di output costano di più, tre-cinque volte, perché vengono generati uno alla volta mentre quelli di input si processano in parallelo nel prefill. Il contesto si ripaga a ogni chiamata, perché il modello è stateless: tutta la pila rientra, e si rifattura, a ogni giro. E la cache sconta ciò che non cambia: il prefisso stabile — system prompt e dichiarazioni dei tool — costa una frazione se riusato. È la KV cache diventata listino.

Il passaggio da fare, perché è il ponte con il prossimo incontro: quello in slide è il listino, ma nel momento in cui costruite agenti dentro un harness il gioco è un altro. C'è una cosa che va ottimizzata durante tutto il ciclo di vita dell'esecuzione dell'agente, e adesso le diamo il suo nome: il contesto. Va ottimizzato in due direzioni opposte insieme — perché non scoppi, e perché sia ricco a sufficienza. Ci sono voci che sfuggono e che possono far crescere i costi davvero: si vedranno meglio descrivendo l'harness.

Ordine di grandezza oggi: da centesimi a qualche dollaro per milione di token, a seconda del modello. Le cifre invecchiano in fretta, le regole no.

### Slide 50 — Il valore delle traiettorie

Il punto di partenza riprende la Slide 37: addestrare, in particolare per l'RL, non è complesso solo tecnicamente. È complesso avere le traiettorie — percorsi reali, andati bene o male, in contesti in cui il modello ha dovuto decidere fra A e B. Ogni conversazione è una traiettoria: prompt, risposte, correzioni, approvazioni e rifiuti.

L'asimmetria è il messaggio: per l'utente è un mezzo per risolvere un problema oggi, stateless e dimenticato domani; per il provider sono miliardi di tracce reali, il carburante del prossimo training, con pattern d'uso che nessun test artificiale produce.

La prova per assurdo che chiude il discorso: alcuni dei principali laboratori ti danno il modello gratis, open weights — ma non ti danno i loro training set, in particolare quelli di reinforcement learning. Se il valore fosse nei pesi, non regalerebbero i pesi.

Da qui l'avvertenza all'utente: molti offrono un opt-out, e va bene — ma va capito che quello che fate è il vero valore economico di questi operatori. Su quei segnali, su quelle reward, si addestra la generazione successiva di modelli agentici. Il moat non è il modello, che diventa commodity: sono le traiettorie d'uso reale, che nessuno può replicare.

Le tre domande in chiusura sono da lasciare in aula, non da rispondere.

### Slide 51 — Closed, open weights, open source

Tassonomia rapida, con tre colori.

**Closed.** I grandi provider ad API, tipicamente americani. Non sai com'è fatto il modello dietro — puoi intuire che siano variazioni sul tema. Zero infrastruttura: chiami quell'indirizzo, passi quel codice, ti billa i token mandati e quelli generati; qualità di frontiera. I due rischi da nominare: l'endpoint oggi c'è, domani chissà — versioni nuove, deprecazioni, e un contesto geopolitico che può cambiare da un giorno all'altro. E l'opt-out: ti dicono che se lo attivi non ti addestrano sui tuoi dati; sarà vero, probabilmente — ma dietro quella barriera non si sa niente.

**Open weights.** Tipicamente cinesi, e la domanda da fare all'aula è: perché regalano i modelli? Non è generosità, è guerra finanziaria — serve a svalutare gli asset degli altri, a dire ai mercati che quel vantaggio non esiste. E in effetti il vantaggio si accorcia: tre, quattro mesi; con i soldi che girano, tre o quattro mesi fanno ridere. Li scarichi, li porti in casa, ci fai fine-tuning e distillazione, i dati restano tuoi. Ma dati e ricetta di training restano privati, le licenze a volte hanno vincoli, e l'infrastruttura è a tuo carico: tirare su le macchine e fare inferenza a scala è un mestiere, e pochissime aziende italiane fanno inferenza locale.

**Open source vero.** Pesi, dati e codice di training pubblici: riproducibili e ispezionabili fino in fondo. Sono i santi della situazione — e purtroppo sono anche i più lontani dalla frontiera.

Quasi tutto ciò che il mercato chiama "open source" è in realtà open weights. La scelta si fa sul caso d'uso, non per principio. E la frontiera si muove: guardiamola.

### Slide 52 — Quando closed, quando open

La tabella si legge per righe, ma il messaggio sta in due frasi.

La fotografia onesta del mercato: chi ha grandi esigenze di privacy e le competenze per fare inferenza locale — o si appoggia a grandi provider di infrastruttura — può andare su open. Ma per mille questioni di opportunità e comodità la stragrande maggioranza usa modelli commerciali closed, perché garantiscono di essere sulla frontiera e tolgono un enorme numero di sbattimenti. Vale anche per gli esercizi di questo corso: dirlo, così l'aula non si aspetta altro.

La nota sul moat, che aggancia la slide precedente: con closed paghi il token *e* regali le traiettorie; con open paghi l'infrastruttura, e le traiettorie restano tue.

E la previsione, che è la cosa da lasciare: più mordono i costi, e più si fa forte la pressione geopolitica di autonomia e indipendenza, più i modelli open acquisteranno prestigio — magari con meccanismi di fine-tuning, che è la slide dopo.

### Slide 53 — Fine-tuning: riprendere la discesa

La definizione più semplice: prendi un modello già addestrato, gli porti i tuoi dati, e gli dici di fare qualche altro giro di training — qualche altro colpetto alle matrici. Stesso metodo di sempre, gradient descent, ma con un punteggio nuovo e pochi passi.

Il perché non si fa quasi mai, con i numeri che lo rendono concreto: il fine-tuning puro su modelli di queste dimensioni richiede computazione enorme, cioè GPU e tempo da training, non da inferenza. E vale la pena ricordare che addestrare un modello linguistico di frontiera costa nell'ordine delle decine, se non centinaia, di milioni di dollari di soli costi energetici e di noleggio dell'infrastruttura. Far girare in casa un modello su cui fare fine-tuning completo è proibitivo.

Il rischio, oltre al costo: correggendo tutti i pesi il modello può disimparare il resto — catastrophic forgetting.

Serve quindi un'alternativa che corregga senza riscrivere. È la prossima slide.

### Slide 54 — LoRA: la correzione a basso rango

L'intuizione, nella formulazione che funziona: invece di andare a toccare le matrici principali — i pettini dei fatti dentro il fully connected, dove se tocchi qualcosa viene giù tutto — si creano *sopra* delle mini matrici più piccole, che poi vengono espanse dinamicamente e vanno a prendere i tuoi dati. Così, invece di andare in sostituzione delle capability del modello principale, vai in addizione leggera, dando dei colpetti sui tuoi dati proprietari.

Il vincolo tecnico è quello che rende la cosa economica: la correzione è costretta a essere il prodotto di due matrici sottili — poche direzioni nuove, non una riscrittura. Con r piccolo, otto o sessantaquattro, contro dimensioni in migliaia, si passa da d×d parametri a 2·d·r: meno dell'uno per cento. In pratica l'adattatore è un file di pochi MB: si monta, si smonta, se ne tengono molti, uno per dominio.

E poi il giudizio, che è la parte più utile per l'aula e va detto senza attenuarlo: il fine-tuning ha senso in pochissimi casi. Ormai il novantanove per cento dei problemi di performance di un agente si risolve migliorando i prompt o la knowledge base — cioè con le materie dei prossimi due incontri.

Dove invece ha senso davvero: la distillazione sul proprio caso d'uso. Metti in produzione il modello grande, raccogli le traiettorie dei tuoi utenti su quel caso d'uso; se è molto circoscritto, molto ripetitivo, con un vocabolario di dominio ristretto, allora puoi addestrare un modello piccolo su quello — e funziona. Ma lo usi solo per quello.

È anche questo a rendere davvero interessanti gli open weights: il modello resta condiviso, la specializzazione diventa tua.

### Slide 55 — La fotografia del mercato

La fotografia invecchia in settimane: rifare lo screenshot a ridosso della lezione fa parte della preparazione, e con esso vanno aggiornate data e fonte in didascalia.

Lettura in aula: evidenziare la frontiera di Pareto e il concetto di *dominato* — tutto ciò che sta sotto o a destra della frontiera. Indicare un paio di closed di punta e almeno un open weights competitivo, agganciando la Slide 51; i punti in basso a destra della frontiera sono dove lavora la distillazione, agganciando la Slide 48.

Il messaggio: non esiste il modello migliore in assoluto — esiste una frontiera, documentata e misurabile. Ci sono modelli bravissimi che costano tantissimo, e modelli anche solo *pochissimo* più scarsi che costano ordini di grandezza in meno; fra due punti vicini sulla frontiera si arrivano a trovare differenze di prezzo di tre ordini di grandezza a fronte di una manciata di punti di qualità.

La domanda da lasciare all'aula è quindi: quanta performance vi serve davvero, e quanto siete disposti a pagarla? Perché poi, molte volte, si finisce comunque per volere quella performance in più — ed è una scelta, non un dato di fatto.

### Slide 56 — La formula, riletta

Slide di chiusura, e non è un riepilogo dell'incontro: è la barra di avanzamento del corso. La formula della Slide 3 torna identica, con acceso il solo termine che abbiamo aperto oggi.

Trenta secondi, e sono l'unico bilancio della giornata: dei sei termini della formula, oggi ne abbiamo aperto uno. Leggere la sintesi sotto il blocco acceso — manipolatore di embeddings, stateless, addestrato in tre fasi a volere i tool — perché è il riassunto in tre battute di tutta la lezione.

Nessun cliffhanger in slide: basta far notare che i cinque blocchi spenti sono il programma dei prossimi due incontri. La stessa figura torna in apertura dell'incontro 27 con `Harness` acceso, e in chiusura del 27 con `System Prompt`, `Tools` e `Skills` accesi; il 28 completa con `KB`.

### Slide 57 — Il ruolo dell'harness

Chiusura del deck. La formula della slide prima dice che dei sei termini se ne è aperto uno; questa apre il secondo e si ferma lì.

La riga che lega tutto: l'harness è un software classico e deterministico, che orchestra quello che fa l'agente sotto la direzione dell'LLM. Se pensiamo all'agente come a un'entità neuro-simbolica, l'LLM è la parte *neuro* e l'harness quella *simbolica* — l'esoscheletro operativo, dentro il quale c'è un cervello.

Il prossimo incontro sta tutto dentro questa figura: la mappa torna in apertura del 27, estesa, ed è la figura madre di quella lezione. Non anticipare i contenuti — basta far vedere quanto è grande la scatola.

E poi il congedo: oggi abbiamo visto i large language model; il prossimo incontro vediamo come farli funzionare in un contesto reale, più operativo, con i tool e il controllo della dimensione del contesto visti dal vivo. Chiudere chiedendo un feedback sul taglio, per fare un aggiustamento dell'ultimo minuto sulla lezione successiva.
