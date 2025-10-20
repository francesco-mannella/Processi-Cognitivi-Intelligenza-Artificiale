

<!-- vim-markdown-toc GFM -->

* [Il linguaggio python](#il-linguaggio-python)
* [Usare python](#usare-python)
* [](#)
* [Concetti di base](#concetti-di-base)
    * [Le operazioni e le variabili in python](#le-operazioni-e-le-variabili-in-python)
    * [Operatori matematici le operazioni standard](#operatori-matematici-le-operazioni-standard)
    * [Operatori matematici altre operazioni](#operatori-matematici-altre-operazioni)
    * [Stringhe di testo](#stringhe-di-testo)
* [Variabili](#variabili)
    * [Assegnamento di valore](#assegnamento-di-valore)
    * [Usare il valore nelle operazioni](#usare-il-valore-nelle-operazioni)
    * [Operatori di assegnamento](#operatori-di-assegnamento)
    * [Tipi di variabili](#tipi-di-variabili)
        * [Le variabili scalari](#le-variabili-scalari)
            * [Valori booleani bool](#valori-booleani-bool)
            * [Valori interi int](#valori-interi-int)
            * [Valori float reali float](#valori-float-reali-float)
            * [Valori complessi complex](#valori-complessi-complex)
        * [Indagare il tipo di una variabile](#indagare-il-tipo-di-una-variabile)
    * [I tipi di variabile predefiniti](#i-tipi-di-variabile-predefiniti)

<!-- vim-markdown-toc -->
## Il linguaggio python 
Un linguaggio di programmazione consente di scrivere istruzioni che vengono
tradotte in un codice binario comprensibile dalla macchina. Questo processo di
traduzione, noto come **compilazione** o **interpretazione**, converte le
istruzioni di alto livello in operazioni matematiche e logiche che il
processore del computer può eseguire direttamente. In questo modo, le
istruzioni umane vengono trasformate in un formato che la macchina può
comprendere ed eseguire per svolgere compiti specifici.

Un linguaggio **compilato** è un linguaggio di programmazione in cui il codice
sorgente viene tradotto in codice macchina eseguibile tramite un processo di
compilazione, prima di essere eseguito. Compilare significa tradurre l'intero
codice sorgente in un file eseguibile prima dell'esecuzione

Un linguaggio **interpretato** esegue il codice direttamente tramite un
interprete, traducendo le istruzioni una alla volta. 

**Python** è un linguaggio di programmazione interpretato, ad alto livello,
noto per la sua sintassi semplice e leggibile, utilizzato in vari ambiti come
sviluppo web, data science e automazione.


## Usare python 

L'interprete Python può essere utilizzato in diversi modi:

* Usare Python in una console interattiva:
  - **IPython**: IPython è un'interfaccia interattiva avanzata per Python che offre funzionalità aggiuntive rispetto alla console standard di Python. Permette di eseguire codice Python in modo interattivo, esplorare oggetti, visualizzare grafici in linea e molto altro. È particolarmente utile per il debugging e l'esplorazione dei dati.
    * Ad esempio, possiamo usare la console ipython come una calcolatrice:
        ``` 
        In [1]: x = 5
        In [2]: y = 10
        In [3]: x + y
        Out[3]: 15
        ```
* Scrivere codice python su notebook online:
    - **Colab** (Google Colaboratory): è un servizio gratuito offerto da Google che
    consente di scrivere ed eseguire codice Python direttamente nel browser. È
    particolarmente utile per il machine learning, l'analisi dei dati e la
    didattica, poiché offre l'accesso a risorse computazionali potenti, come GPU e
    TPU, senza necessità di configurazione locale. Colab supporta l'importazione di
    librerie Python e l'integrazione con Google Drive per il salvataggio e la
    condivisione dei notebook.
    Colab è una piattaforma che utilizza i notebook Python, conosciuti come Jupyter
    Notebook, per creare documenti interattivi. Questi documenti consentono di
    integrare codice eseguibile, testo formattato, immagini e grafici in un unico
    file. I notebook sono organizzati in celle, che possono contenere codice
    Python, testo in Markdown o l'output del codice eseguito. È possibile inserire
    vari tipi di celle nel documento, eseguire ogni cella di codice singolarmente o
    eseguire l'intero documento in una sola volta.
    ![Esempio di foglio colab](pics/colab-run-few-lines.gif)

* Scrivere codice python su file:
    - Per scrivere codice su file in maniera efficiente, vengono usati dei programmi di scrittura con delle funzionalità aggiuntive, gli IDE.  Un IDE (Integrated Development Environment) è un software che fornisce strumenti completi per lo sviluppo di applicazioni, come un editor di codice, un debugger e un compilatore. Spyder (Scientific Python Development Environment) è un IDE specificamente progettato per il linguaggio Python. Offre funzionalità come l'editing avanzato del codice, il debugging interattivo, l'integrazione con librerie scientifiche e un'interfaccia utente che facilita l'esplorazione dei dati e la visualizzazione.
    ![Esempio debug in spyder](pics/debugging-commands.gif)
    
-----

## Concetti di base

### Le operazioni e le variabili in python

L'ambiente **Python** può essere usato come calcolatore.

### Operatori matematici le operazioni standard

| Operatore | Operazione |
| :---: | :--- |
| `+` | Addizione |
| `-` | Sottrazione |
| `*` | Moltiplicazione |
| `/` | Divisione |

### Operatori matematici altre operazioni

| Operatore | Operazione |
| :---: | :--- |
| `//` | Divisione per interi |
| `**` | Esponente |
| `%` | Modulo |

-----

### Stringhe di testo

In Python possiamo anche scrivere stringhe di testo e manipolarle, utilizzando apici singoli (`'`) o doppi (`"`):

| Tipo di Stringa | Esempio |
| :--- | :--- |
| Apici doppi (singola riga) | `"Questo e’ un testo"` |
| Apici doppi (multipla riga) | `""" Questo è un testo con tante righe """` |
| Apici singoli (singola riga) | `'quì uso gli apici singoli'` |
| Apici singoli (multipla riga) | `''' anche quì uso gli apici singoli '''` |

-----

## Variabili

### Assegnamento di valore

Si usa il simbolo `=` per assegnare un **valore** a un **nome** di variabile:

| Nome | Assegnamento | Valore |
| :--- | :---: | :--- |
| `x` | `=` | `3` |
| `Pippo` | `=` | `5 * 7.2` |
| `v23` | `=` | `"Questo è un testo"` |

### Usare il valore nelle operazioni

Il valore di una variabile può essere usato in altre operazioni:

```python
x = 3
y = 5 + x
y  # Risultato: 8
```

### Operatori di assegnamento

Questi operatori combinano un'operazione con l'assegnamento, modificando il valore della variabile:

| Operatore | Esempio | Equivale a |
| :---: | :--- | :--- |
| `+=` | `x += 1` | `x = x + 1` |
| `-=` | `x -= 3.4` | `x = x - 3.4` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 4` | `x = x % 4` |


### Tipi di variabili

#### Le variabili scalari

Le variabili scalari rappresentano singoli valori e includono:

  * **Valori booleani** (Vero o Falso)
  * **Numeri interi**
  * **Numeri in virgola mobile** (Reali)
  * **Numeri complessi**

##### Valori booleani bool

Assegnare un valore di tipo booleano rende la variabile di tipo booleano.

| Esempio di Assegnamento | Note |
| :--- | :--- |
| `x = False` | Assegna direttamente il valore. |
| `x = 1 + 4 == 5` | Assegna il risultato di una comparazione (che è booleano). |

##### Valori interi int

Assegnare un valore di tipo intero rende la variabile di tipo intero.

| Esempio di Assegnamento | Note |
| :--- | :--- |
| `x = 2` | Assegna direttamente il valore intero. |
| `x = int( 2.0 )` | Converte un altro tipo (float) in intero. |

##### Valori float reali float

Assegnare un valore di tipo `float` (virgola mobile) rende la variabile di tipo `float`.

| Esempio di Assegnamento | Note |
| :--- | :--- |
| `x = 3.4` | Assegna direttamente il valore float. |
| `x = float( 4 )` | Converte un altro tipo (int) in float. |

##### Valori complessi complex

Assegnare un valore di tipo complesso rende la variabile di tipo `complex`.

| Esempio di Assegnamento | Note |
| :--- | :--- |
| `x = 3.4 + 2j` | Assegna un numero complesso con parte immaginaria `2j`. |
| `x = complex ( 1 )` | Converte un altro tipo (int) in complesso. |

-----

#### Indagare il tipo di una variabile

Per conoscere il tipo di una variabile si usa la funzione **`type()`**:

```python
type(x)
```

La funzione `type` ritorna **il tipo della variabile**.


### I tipi di variabile predefiniti

La tabella seguente riassume i principali tipi di variabile predefiniti in Python, suddivisi per categorie:

| Tipo | Nome Python | Scalare | Sequenza | Mutabile | Contenitore Iterabile |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Booleani** | `bool` | X | | | |
| **Interi** | `int` | X | | | |
| **Virgola Mobile** | `float` | X | | | |
| **Complessi** | `complex` | X | | | |
| **Stringhe** | `str` | | X | | X |
| **Tuple** | `tuple` | | X | | X |
| **Liste** | `list` | | X | X | X |
| **Insiemi** | `set` | | | X | X |
| **Dizionari** | `dict` | | | X | X |----
