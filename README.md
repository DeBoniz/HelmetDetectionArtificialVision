# HelmetDetection 

Progetto per il rilevamento automatico di caschi di sicurezza tramite modelli di deep learning (YOLO/Ultralytics).

---

## Struttura della cartella


HelmetDetection/
├── AnnotationHelmet/
│   └── casco_env/         # Ambiente virtuale Python
├── datasetmodelloscelto/  # Dataset scelto per l’addestramento
├── datasets/              # Altri dataset di supporto/test
├── ultralytics/           # Framework YOLO + configurazioni
├── videotest/             # Video per testare il modello
└──helmet_detection_report.md          # File che contiene un sommario del progetto


- **AnnotationHelmet/**  
  Contiene strumenti e script per la gestione delle annotazioni.  
  All’interno si trova la cartella **"casco_env/"**, un ambiente virtuale Python necessario per eseguire training, predizioni o script vari.

- **datasetmodelloscelto/**  
  Contiene il **dataset scelto per l’addestramento** del modello.  

- **datasets/**  
  Contiene altri dataset di supporto o di test.

- **ultralytics/**  
  Directory dedicata al framework **Ultralytics YOLO**, con script e configurazioni per il training/prediction.

- **videotest/**  
  Contiene i video usati per testare il modello addestrato.
- **helmet_detection_report/**
  Contiene una descrizione completa sui modelli e sul progetto.
  

- Inoltre vi sono presenti 2 video inferenziati di esempio con il modello "best.pt" anch'esso presente , ovvero il corrispondente migliore del addestramento 21.
---

##  Ambiente virtuale

Prima di eseguire qualsiasi comando (training, predizione o script Python), è obbligatorio attivare l’ambiente virtuale:

```bash
source AnnotationHelmet/casco_env/bin/activate
 ```
per disattivarlo: ```bash deactivate   ```
## Utilizzo

Per effettuare una predizione su immagini o video:

```bash yolo task=detect mode=predict model=runs/detect/train21-modelloscelto-/weights/best.pt source=../videotest/testv.mp4 project=runs/detect name=predict   ```

train21-modelloscelto- può anche essere cambiato con gli altri modelli presente all'interno di runs/detect/ , così come può essere scelto il video o l'immagine su cui fare inferenza specificandone il percorso in source .

Per effettuare un training yolo: 

```bash yolo task=detect mode=train model=yolov11s.pt data=datasetmodelloscelto/data.yaml epochs=100 imgsz=640 ```

model può variare in base al modello che si sceglie di usare in base alle esigenze dell'utente, così come può variare la grandezza delle immagini e il numero di epoche di addestramento con i parametri imgsz ed epochs seguendo la volontà dell'utente .(i modelli già scaricati e disponibili sono presenti nella cartella ultralytics.)

È consigliato usare il file data.yaml corretto per il dataset scelto, altrimenti YOLO non potrà avviare il training.

Il comando desiderato va effettuato all'interno della cartella ultralytics con il virtual environment (casco_env) attivo per far si che funzioni.

è possibile inoltre osservare dati in merito al modello nella cartella runs/detect/train21(modelloscelto)/ , dove si trovano, immagini esplicative rappresentanti confusion matrix, boxplot , e file csv contententi le metriche di ogni epoca di training, oltre ad un file di configurazione args.yaml, per un'analisi più approfondita del modello e dei suoi parametri. 

Per osservare i risultati delle inferenze su video/immagini occorre andare nella cartella ultralytics/runs/detect/predictx dove vi sarà un file .avi corrispondente al video post-inferenza o un file .jpg corrispondente all'immagine post-inferenza
