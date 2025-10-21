

<!-- vim-markdown-toc GFM -->

* [Il linguaggio python](#il-linguaggio-python)
* [Usare python](#usare-python)
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
* [Il linguaggio Python - Le strutture di controllo](#il-linguaggio-python---le-strutture-di-controllo)
    * [L'istruzione `if`](#listruzione-if)
    * [Componenti dell'istruzione `if`](#componenti-dellistruzione-if)
    * [`else` - Istruzioni alternative](#else---istruzioni-alternative)
    * [`elif` - Più alternative](#elif---più-alternative)
* [Gli operatori di confronto](#gli-operatori-di-confronto)
* [Gli operatori logici](#gli-operatori-logici)
* [Il ciclo `for`](#il-ciclo-for)
    * [Componenti del ciclo `for`](#componenti-del-ciclo-for)
    * [Sequenza di inizializzazione personalizzata](#sequenza-di-inizializzazione-personalizzata)
* [Il ciclo `while`](#il-ciclo-while)
    * [Componenti del ciclo `while`](#componenti-del-ciclo-while)
* [L'istruzione `break`](#listruzione-break)
* [L'istruzione `continue`](#listruzione-continue)
* [Le stringhe](#le-stringhe)
    * [Costruzione delle stringhe](#costruzione-delle-stringhe)
    * [Componenti](#componenti)
    * [Le sequenze di escape](#le-sequenze-di-escape)
        * [Sequenze di controllo](#sequenze-di-controllo)
        * [Sequenze per caratteri speciali](#sequenze-per-caratteri-speciali)
    * [Il prefisso di stringa `r`](#il-prefisso-di-stringa-r)
    * [Operazioni sulle stringhe](#operazioni-sulle-stringhe)
        * [Concatenazione e ripetizione](#concatenazione-e-ripetizione)
        * [Indicizzazione delle stringhe](#indicizzazione-delle-stringhe)
        * [I metodi degli oggetti stringa](#i-metodi-degli-oggetti-stringa)
            * [Elenco dei principali metodi](#elenco-dei-principali-metodi)
            * [Esempio di utilizzo](#esempio-di-utilizzo)
    * [Formattazione di stringhe](#formattazione-di-stringhe)
        * [Vecchio stile (%)](#vecchio-stile-)
            * [Componenti](#componenti-1)
            * [Più argomenti](#più-argomenti)
            * [Regola per i placeholder (vecchio stile)](#regola-per-i-placeholder-vecchio-stile)
        * [Nuovo stile (.format())](#nuovo-stile-format)
            * [Componenti](#componenti-2)
            * [Regola per i placeholder (nuovo stile)](#regola-per-i-placeholder-nuovo-stile)
        * [f-string (Python >= 3.6)](#f-string-python--36)
            * [Componenti](#componenti-3)
            * [Regola per i placeholder (f-string)](#regola-per-i-placeholder-f-string)
* [Le Liste](#le-liste)
    * [Caratteristiche delle Liste](#caratteristiche-delle-liste)
        * [Le liste sono sequenze ordinate](#le-liste-sono-sequenze-ordinate)
        * [Le liste possono contenere qualsiasi oggetto](#le-liste-possono-contenere-qualsiasi-oggetto)
* [Gli Indici](#gli-indici)
    * [Come richiamare gli elementi di una lista](#come-richiamare-gli-elementi-di-una-lista)
    * [Indici negativi](#indici-negativi)
* [Iterazione sulle Liste](#iterazione-sulle-liste)
* [La Notazione di Slicing](#la-notazione-di-slicing)
    * [La regola dello slicing](#la-regola-dello-slicing)
* [Comprensione di Lista](#comprensione-di-lista)
    * [Struttura della comprensione di lista](#struttura-della-comprensione-di-lista)
    * [Comprensioni di lista annidate](#comprensioni-di-lista-annidate)
    * [Comprensioni di lista vs. cicli for](#comprensioni-di-lista-vs-cicli-for)
* [Operazioni con le Liste](#operazioni-con-le-liste)
    * [Concatenazione](#concatenazione)
    * [Ripetizione](#ripetizione)
* [Metodi delle Liste](#metodi-delle-liste)
    * [Esempio: extend vs operatore +=](#esempio-extend-vs-operatore-)
* [L'operatore `in`](#loperatore-in)

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

### Stringhe di testo

In Python possiamo anche scrivere stringhe di testo e manipolarle, utilizzando apici singoli (`'`) o doppi (`"`):

| Tipo di Stringa | Esempio |
| :--- | :--- |
| Apici doppi (singola riga) | `"Questo e’ un testo"` |
| Apici doppi (multipla riga) | `""" Questo è un testo con tante righe """` |
| Apici singoli (singola riga) | `'quì uso gli apici singoli'` |
| Apici singoli (multipla riga) | `''' anche quì uso gli apici singoli '''` |

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


## Il linguaggio Python - Le strutture di controllo


### L'istruzione `if`

Eseguire un insieme di istruzioni se si verifica una condizione.

```python
a = 4
if a > 2:
    a = a * 10
print(a)
```

### Componenti dell'istruzione `if`

- **Parola chiave**: `if`
- **Test**: Qualsiasi espressione che ha risultato vero o falso
- **Due punti (`:`)**: Fine dell'istruzione if
- **Indentazione**: Il codice indentato a destra rispetto all'istruzione if viene eseguito se il test è verificato


### `else` - Istruzioni alternative

Fornire un set di istruzioni alternative.

```python
a = 4
if a > 2:
    a = a * 10
else:
    a = 9999
print(a)
```

- **Se il test è vero**: esegue il primo blocco
- **Se il test è falso**: esegue il blocco `else`


### `elif` - Più alternative

Fornire più set alternativi di istruzioni con verifica per esclusione.

```python
a = 4
if a < 2:
    a = a * 10
elif 2 < a <= 4:
    a = 999
elif 4 < a <= 6:
    a = 9999
else:
    a = 9999
print(a)
```

La valutazione avviene in sequenza:
- **Se il primo test è vero**: esegue il primo blocco
- **Se il primo test è falso e il secondo test è vero**: esegue il secondo blocco
- **Se i primi due test sono falsi ed il terzo è vero**: esegue il terzo blocco
- **Se tutti gli altri test sono falsi**: esegue il blocco `else`


## Gli operatori di confronto

| Operatore | Test |
|-----------|------|
| `==` | uguale a |
| `!=` | diverso da |
| `>` | maggiore di |
| `<` | minore di |
| `>=` | maggiore o uguale a |
| `<=` | minore o uguale a |


## Gli operatori logici

| Operatore | Test |
|-----------|------|
| `<test1> and <test2>` | vero se `<test1>` e `<test2>` sono entrambi veri |
| `<test1> or <test2>` | vero se almeno uno tra `<test1>` e `<test2>` è vero |
| `not <test1>` | vero se `<test1>` è falso |


## Il ciclo `for`

Ripetere tante volte un insieme di istruzioni.

```python
a = 0
for x in range(5):
    a = a + x
print(a)
```

### Componenti del ciclo `for`

- **Parole chiave**: `for` ... `in`
- **Variabile contatore**: viene inizializzata con un valore diverso per ogni iterazione
- **Sequenza di inizializzazione**: da questa sequenza vengono presi i valori di inizializzazione del contatore
- **Due punti (`:`)**: Fine dell'istruzione for
- **Indentazione**: Il codice indentato a destra rispetto all'istruzione for viene eseguito ad ogni iterazione


### Sequenza di inizializzazione personalizzata

La sequenza di inizializzazione può essere fatta "a mano" con una lista.

```python
a = 0
for x in [4, 5, 3]:
    a = a + x
print(a)
```


## Il ciclo `while`

Le iterazioni sono condizionate da un test:
- Se il test è vero, il ciclo continua
- Se il test è falso, il ciclo si chiude

```python
a = 1.05
while a < 2000:
    a = a ** 2 + 0.1
print(a)
```

### Componenti del ciclo `while`

- **Parola chiave**: `while`
- **Test**: decide se il ciclo continua
- **Due punti (`:`)**: Fine dell'istruzione while
- **Indentazione**: Il codice indentato a destra rispetto all'istruzione while viene eseguito ad ogni iterazione


## L'istruzione `break`

Interrompere un ciclo `for` o `while` se si verifica una condizione.

```python
x = 1
for t in range(10):
    x = x * 2 + 1
    print(x)
    if x > 500:
        break
```

- **Parola chiave**: `break`


## L'istruzione `continue`

- Salta le istruzioni rimanenti in un'iterazione
- Va all'iterazione successiva

```python
for i in range(6):
    if i == 4:
        continue
    print(i)
```

- **Parola chiave**: `continue`
- La riga di codice dopo `continue` non viene eseguita nell'iterazione in cui il test è vero



## Le stringhe

Le stringhe rappresentano parti di testo.

```python
x = "Una stringa"
```

- **Limiti della stringa**: delimitati da apici


### Costruzione delle stringhe

Le stringhe possono essere costruite sia con i singoli apici che con i doppi apici.

```python
x = "Un'altra stringa"
y = "la variabile 'x'"
txt1 = 'si chiama "stringa"'
```

### Componenti
- **Limiti della stringa**: apici singoli `'` o doppi `"`
- **Caratteri di testo**: il contenuto della stringa


### Le sequenze di escape

Caratteri speciali usati per determinate funzioni.

#### Sequenze di controllo

| Sequenza | Funzione |
|----------|----------|
| `\t` | Tabulazione |
| `\r` | Ritorno a capo |
| `\f` | Avanzamento di riga |
| `\n` | Avanzamento di riga con ritorno a capo |

#### Sequenze per caratteri speciali

| Sequenza | Funzione |
|----------|----------|
| `\\` | backslash |
| `\'` | carattere apice singolo |
| `\"` | carattere apice doppio |


### Il prefisso di stringa `r`

Raw string - i backslash non vengono letti come inizio di sequenze di escape.

```python
rstr = r"C:\Documenti\miodocumento.doc"
```


### Operazioni sulle stringhe

#### Concatenazione e ripetizione

```python
my_str = "una" + " " + "stringa"
another_str = "<<>>" * 10
```


#### Indicizzazione delle stringhe

Come richiamare un singolo carattere.

```python
una_stringa = "Una sequenza di caratteri"
una_stringa[3]
```

```python
una_stringa = "Una sequenza di caratteri"
una_stringa[10]
```


#### I metodi degli oggetti stringa

##### Elenco dei principali metodi

| Metodo | Metodo | Metodo |
|--------|--------|--------|
| `capitalize()` | `isalpha()` | `isspace()` |
| `find()` | `isascii()` | `isupper()` |
| `format()` | `isidentifier()` | `lower()` |
| `index()` | `islower()` | `swapcase()` |
| `isalnum()` | `isnumeric()` | `upper()` |

##### Esempio di utilizzo

```python
x = 'stringa'
y = x.upper()
print(y)
>>> STRINGA
```


### Formattazione di stringhe

#### Vecchio stile (%)

```python
pi = 3.14159265358979323846
s = "il valore di pi-greco è: %7.5f" % pi
print(s)
>>> il valore di pi-greco è: 3.14159

```

##### Componenti

- **Placeholder**: descrive come formattare il valore da inserire
- **Simbolo `%` dopo la stringa**: precede l'argomento da inserire al posto del placeholder
- **Argomento**: espressione (valore, variabile o espressione) che dà il valore da inserire nel placeholder

##### Più argomenti

```python
numero_articoli = 3
totale = 135.6

s ="""
Il carrello include %d articoli per un
totale di %6.2f€
""" % (numero_articoli, totale)

print(s)
>>> Il carrello include 3 articoli per un
>>> totale di 135.60€

```

- La prima variabile della sequenza sostituisce il primo placeholder
- La seconda variabile della sequenza sostituisce il secondo placeholder

##### Regola per i placeholder (vecchio stile)

| N | Elemento | Descrizione | Obbligatorio | Requisiti |
|---|----------|-------------|--------------|-----------|
| 0 | `%` | Inizio del placeholder | obbligatorio | - |
| 1 | numero intero | Larghezza campo | opzionale | richiede 0, 4 |
| 2 | `.` | separatore di campo | opzionale per placeholder float | richiede 1, 3, 4 |
| 3 | numero intero | Precisione decimale | opzionale per placeholder float | richiede 1, 2, 4 |
| 4 | lettera (`d`, `f`, ...) | tipo del placeholder | obbligatorio | richiede 0 |


#### Nuovo stile (.format())

```python
pi = 3.14159265358979323846
s = "pi greco: {:7.5f}".format(pi)

print(s)
>>> pi greco: 3.14159
```

##### Componenti

- **Placeholder**: delimitati da parentesi graffe `{}`
- **Metodo `.format()`**: fornisce gli argomenti per i placeholder

##### Regola per i placeholder (nuovo stile)

| N | Elemento | Descrizione | Obbligatorio | Requisiti |
|---|----------|-------------|--------------|-----------|
| 0 | `{` | Inizio del placeholder | obbligatorio | - |
| 1 | `:` | inizio specifica | opzionale | - |
| 2 | numero intero | Larghezza campo | opzionale | richiede 1 e 5 |
| 3 | `.` | separatore di campo | opzionale per placeholder float | richiede 1, 3, 5 |
| 4 | numero intero | Precisione decimale | opzionale per placeholder float | richiede 1, 2, 5 |
| 5 | lettera (`d`, `f`, ...) | tipo del placeholder | opzionale | richiede 1 |
| 6 | `}` | fine del placeholder | obbligatorio | - |


#### f-string (Python >= 3.6)

```python
pi = 3.14159265358979323846

s1 = "pi greco: {pi}"
s2 = f"pi greco troncato: {pi:7.5f}"

print(s1)
>>> pi greco: 3.14159265358979323846

print(s2)
>>> pi greco troncato: 3.14159

```

##### Componenti

- **Prefisso `f`**: indica una f-string
- **Placeholder con riferimento diretto**: contiene un riferimento diretto alla variabile, il valore o l'espressione da sostituire

##### Regola per i placeholder (f-string)

| N | Elemento | Descrizione | Obbligatorio | Requisiti |
|---|----------|-------------|--------------|-----------|
| 0 | `{` | Inizio del placeholder | obbligatorio | - |
| 1 | espressione | valore da formattare | obbligatorio | - |
| 2 | `:` | inizio specifica | opzionale | - |
| 3 | numero intero | Larghezza campo | opzionale | richiede 2, 6 |
| 4 | `.` | separatore di campo | opzionale per placeholder float | richiede 2, 4 e 6 |
| 5 | numero intero | Precisione decimale | opzionale per placeholder float | richiede 2, 3, 6 |
| 6 | lettera (`d`, `f`, ...) | tipo del placeholder | opzionale | richiede 2 e 6 |
| 7 | `}` | fine del placeholder | obbligatorio | - |

## Le Liste

Le liste sono oggetti composti da più elementi.

```python
lista1 = [1, 4, 5, 8]
lista2 = [0.3, 8 + 7j, "Nessuno"]
lista3 = []
```

### Caratteristiche delle Liste

#### Le liste sono sequenze ordinate

```python
lista1 = [4.0, 5, 8, True]
```

Gli indici partono sempre da 0:

```
Indici:  0    1   2    3
        [4.0, 5,  8,  True]
```

#### Le liste possono contenere qualsiasi oggetto

```python
lista2 = [4.0, ["primo", 2], 8, True]
```

Nota: un elemento può essere a sua volta una lista.

## Gli Indici

### Come richiamare gli elementi di una lista

```python
lista = [1, 3.0, 1.0, 2, 40]
print(lista[0])  # Primo elemento
x = lista[1] + 4
```

Le parentesi quadre sono usate per richiamare un singolo elemento. L'indice tra parentesi richiama l'elemento in quella posizione.

```
Indici:  0    1     2    3   4
        [1,  3.0,  1.0,  2,  40]
```

### Indici negativi

```python
lista = [1, 3.0, 1.0, 2, 40]
lista[-1]  # 40 -- ultimo elemento
lista[-2]  # 2 -- penultimo elemento
```

## Iterazione sulle Liste

Gli oggetti lista sono iterabili: possono essere scorsi con un ciclo `for`

```python
lista = [1, 3.0, 1.0, 2, 40]
for elemento in lista:
    print(elemento)
```

## La Notazione di Slicing

Come ottenere una parte di una lista:

```python
lista = [1, 3.0, 1.0, 2, 40]
lista[1:3]     # [3.0, 1.0]
lista[:2]      # [1, 3.0]
lista[2:]      # [1.0, 2, 40]
lista[-2:]     # [2, 40]
lista[:3:2]    # [1, 1.0]
lista[:]       # [1, 3.0, 1.0, 2, 40]
lista[::-1]    # [40, 2, 1.0, 3.0, 1]
```

### La regola dello slicing

```python
variabile[inizio:fine:passo]
```

- **inizio**: l'indice da cui inizia la sottolista
  - può essere omesso
  - se viene omesso si sottintende l'indice 0

- **fine**: l'indice che indica la fine della sottolista
  - può essere omesso
  - se viene omesso si sottintende l'indice dopo l'ultimo elemento
  - l'ultimo elemento ha indice `<fine - 1>`

- **passo**: indica il salto nella sequenza durante la scelta
  - può essere omesso
  - se viene omesso si sottintende 1
  - se è negativo l'ordine è invertito (dall'indice maggiore all'indice minore)

## Comprensione di Lista

Creare liste in maniera iterativa:

```python
lst = [x ** 2 for x in range(1, 8)]
# [1, 4, 9, 16, 25, 36, 49]
```

### Struttura della comprensione di lista

```python
[espressione for variabile_contatore in sequenza]
```

- **parole chiave**: `for` e `in`
- **variabile contatore**: la variabile che itera
- **sequenza**: la sequenza di iterazione della variabile contatore
- **espressione**: definisce il singolo elemento, dato il valore corrente della variabile contatore

### Comprensioni di lista annidate

**Lista di liste:**
```python
lst = [[x * y for y in range(1, 4)] 
       for x in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

Per ogni `x`, viene completata una sottolista iterando tutte le `y`.

**Lista piatta:**
```python
lst = [x * y for y in range(1, 4) 
       for x in range(1, 4)]
# [1, 2, 3, 2, 4, 6, 3, 6, 9]
```

Per ogni `y`, viene calcolato un nuovo elemento iterando tutte le `x`.

### Comprensioni di lista vs. cicli for

**Pro:**
- Codice più veloce
- Codice più compatto

**Contro:**
- Codice illegibile (se si esagera)
- Espressioni one-liner per le singole iterazioni

## Operazioni con le Liste

### Concatenazione

```python
[5, 2.0, 3] + [1, 1, 3]
# [5, 2.0, 3, 1, 1, 3]
```

L'operatore `+` concatena due liste.

### Ripetizione

```python
[2, 3] * 3
# [2, 3, 2, 3, 2, 3]
```

L'operatore `*` concatena una lista con se stessa per un numero di volte dato dal moltiplicatore.

## Metodi delle Liste

**Usare i metodi invece che espressioni con gli operatori quando è possibile.**

Lista dei metodi disponibili:
- `.append()` - aggiunge un elemento
- `.count()` - conta occorrenze
- `.insert()` - inserisce un elemento
- `.reverse()` - inverte l'ordine
- `.clear()` - svuota la lista
- `.extend()` - estende con un'altra lista
- `.pop()` - rimuove e restituisce un elemento
- `.sort()` - ordina la lista
- `.copy()` - crea una copia
- `.index()` - trova l'indice di un elemento
- `.remove()` - rimuove un elemento

### Esempio: extend vs operatore +=

```python
lst = [1, 2, 3, 4]
lst += [99, 99]  # Possibile ma...

lst.extend([99, 99])  # Preferibile!
```

## L'operatore `in`

```python
lst = [1, 2, 3, 4]
2 in lst
# True
```

Ritorna `True` se l'oggetto sta dentro il contenitore.

---

*Francesco Mannella - Programmazione Scientifica in Python - Il linguaggio Python: Le liste*
