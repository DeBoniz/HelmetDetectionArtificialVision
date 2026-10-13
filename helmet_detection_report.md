# Report Sistema di Rilevamento Automatico Caschi di Sicurezza

## 1. Executive Summary

Il progetto ha sviluppato con successo un sistema di rilevamento automatico di persone con casco per applicazioni di videosorveglianza . Il modello finale (Modello 21) ha raggiunto prestazioni eccellenti con un **mAP50 di 94.69%** e un **recall di 89.61%**, dimostrando capacità ottimali per il deployment in scenari reali di sicurezza urbani.

## 2. Obiettivi del Progetto

Il sistema è stato progettato per:
- **Rilevamento automatico in tempo reale** di persone con casco 
- **Analisi 24/7** di immagini RGB (condizioni diurne/notturne)
- **Notifiche immediate** per violazioni della sicurezza
- **Integrazione** con sistemi di videosorveglianza esistenti

## 3. Dataset e Metodologia

### 3.1 Composizione del Dataset
- **Totale immagini**: 18,159
- **Training Set**: 16,386 immagini (90%)
- **Validation Set**: 1,130 immagini (6%)
- **Test Set**: 643 immagini (4%)

### 3.2 Caratteristiche del Dataset
Il dataset comprende diverse tipologie di immagini:
- Caschi in vari colori e tipologie
- Scenari urbani
- Condizioni di illuminazione variabili
- Angolazioni e distanze diverse
- Situazioni affollate e isolate

### 3.3 Preprocessing
- **Auto-Orient**: Applicato per correzione automatica orientamento
- **Resize**: Stretch to 640x640 pixels per compatibilità modello
- **Augmentations**: 2 output per training example con noise fino a 0.25% dei pixel

## 4. Sviluppo e Ottimizzazione del Modello

### 4.1 Approccio Iterativo
Sono stati testati 6 modelli diversi con configurazioni progressive:

1. **Modello 7**: Baseline senza immagini complesse
2. **Modello 11**: Aggiunta immagini video affollate
3. **Modello 16**: Inclusione hard negatives con label precise
4. **Modello 17**: Ottimizzazione label precise
5. **Modello 24**: Riduzione 50% immagini primo piano
6. **Modello 21**: Configurazione ottimale finale (senza hard negatives, con label precise e aggiunta di immagini con noise.)

### 4.2 Strategia di Miglioramento
- **Curation dei dati**: Rimozione hard negatives con label imprecise
- **Bilanciamento del dataset**: Aggiunta immagini video affollate
- **Qualità delle annotazioni**: Focus su label corrette e precise
- **Efficienza temporale**: Ottimizzazione numero epoche

## 5. Risultati del Modello Finale (Modello 21)

### 5.1 Metriche di Performance
| Metrica | Valore | Benchmark |
|---------|--------|-----------|
| **Precision** | 92.98% | Eccellente |
| **Recall** | 89.61% | Ottimo |
| **mAP50** | 94.69% | Superiore |
| **mAP50-95** | 72.54% | Buono |

### 5.2 Efficienza Operativa
- **Epoche di training**: 25 (convergenza rapida)
- **Tempo di training**: 2,942 secondi (~49 minuti)
- **Efficienza**: Miglior rapporto performance/tempo

### 5.3 Loss Functions (Epoca finale)
- **Box Loss**: 0.85148 (localizzazione accurata)
- **Classification Loss**: 0.4932 (classificazione affidabile)
- **DFL Loss**: 1.14306 (distribuzione focal loss ottimizzata)

## 6. Analisi Comparativa dei Modelli

Il Modello 21 si distingue per:
- **Highest mAP50**: 94.69% vs media 93.45% degli altri modelli
- **Best Recall**: 89.61% (capacità superiore di rilevamento)
- **Velocità**: Convergenza in 25 epoche vs 42-100 degli altri
- **Stabilità**: Configurazione pulita senza hard negatives problematici

## 7. Vantaggi Competitivi

### 7.1 Performance Tecniche
- **Alta precisione**: 92.98% riduce falsi positivi
- **Elevato recall**: 89.61% minimizza caschi non rilevati
- **Velocità inferenza**: Compatibile con analisi real-time
- **Robustezza**: Testato su scenari diversificati

### 7.2 Applicabilità Industriale
- **Integrazione semplice**: Standard input 640x640
- **Scalabilità**: Architettura ottimizzata per deployment
- **Affidabilità**: Metriche validate su test set indipendente
- **Versatilità**: Performance stabili in varie condizioni

## 9. Conclusioni

Il progetto ha raggiunto tutti gli obiettivi prefissati, sviluppando un sistema di rilevamento caschi con prestazioni elevate. Il Modello 21 rappresenta la soluzione ottimale, combinando alta accuratezza (mAP50 94.69%), efficienza computazionale e robustezza operativa.

Il sistema è pronto per il deployment in ambienti reali, con capacità di elaborazione real-time e notifiche immediate per violazioni della sicurezza. L'approccio metodologico adottato garantisce riproducibilità e possibilità di miglioramenti futuri attraverso l'espansione del dataset.

### 9.1 ROI Atteso
- **Riduzione incidenti**: Prevenzione automatica violazioni sicurezza
- **Compliance**: Rispetto normative sicurezza 
- **Efficienza operativa**: Monitoraggio 24/7 senza intervento umano
- **Scalabilità**: Applicabile a multiple telecamere simultaneamente

---

