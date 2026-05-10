# PD-model-J-Test-
Tool in Python per il Backtesting della Probability of Default tramite Jeffreys Test 
# 🏦 PD Backtesting Tool: Jeffreys Test (EBA Compliant)

Questo repository ospita uno strumento avanzato in Python per la validazione statistica dei modelli di **Probability of Default (PD)**. Il tool implementa il **Jeffreys Test**, una metodologia Bayesiana robusta, ideale per il backtesting di portafogli bancari, in conformità con i requisiti di vigilanza europei.

---

## Background Teorico: Il Jeffreys Test

Nel contesto del rischio di credito, la validazione della PD consiste nel verificare se la probabilità stimata dal modello sia coerente con i default effettivamente osservati (*Default Rate*).

### Perché usare il Jeffreys Test?
A differenza dei test frequentisti classici (come il test Binomiale basato sulla distribuzione Normale), il Jeffreys Test utilizza un approccio **Bayesiano** con una **Prior non informativa** (distribuzione Beta con parametri $\alpha = 0.5, \beta = 0.5$).

**Vantaggi principali:**
1. **Low Default Portfolios (LDP):** È estremamente efficace per portafogli con pochi eventi di default, dove i test standard perdono potenza statistica.
2. **Distribuzione Beta:** Fornisce una stima più precisa della distribuzione "a posteriori" della PD, permettendo di calcolare con esattezza la probabilità che il modello stia sottostimando il rischio.



---

## Conformità Normativa (EBA Guidelines)

Il tool è progettato seguendo i principi del **Validation Report** richiesto dalle autorità di vigilanza (**EBA/GL/2017/16** - *Guidelines on PD estimation, LGD estimation and the treatment of defaulted exposures*).

### Il Sistema "Traffic Light" (Semaforo)
Secondo le best practice di vigilanza, l'esito del test viene classificato in tre fasce basate sul **p-value**:

| Colore | Soglia p-value | Significato Regolamentare |
| :--- | :--- | :--- |
| **Verde** | $p > 0.05$ | Modello calibrato correttamente. Nessuna azione richiesta. |
| **Giallo** | $0.01 < p \leq 0.05$ | Segnale di attenzione. Richiesto monitoraggio o analisi correttive. |
| **Rosso** | $p \leq 0.01$ | Sottostima significativa. Obbligo di ricalibrazione del modello. |



---

## Caratteristiche del Tool
- **Input Dinamici:** Integrazione con Google Colab Forms per un utilizzo immediato.
- **Visualizzazione HD:** Grafici vettoriali pronti per l'inserimento in presentazioni aziendali.
- **Analisi Statistica:** Calcolo automatico di TD osservato, p-value e soglie critiche.

## Requisiti Tecnici
Il codice richiede le seguenti librerie Python:
- `numpy`
- `scipy`
- `matplotlib`
- `pandas`

---

## Esempio di Output
Il tool genera un report grafico che mostra la distribuzione di densità della PD e posiziona la stima del modello rispetto alla zona di rifiuto statistico.

![Grafico Validazione](validazione_Portafoglio_Corporate.png)
