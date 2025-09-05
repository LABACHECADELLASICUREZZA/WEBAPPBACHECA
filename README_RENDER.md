# Guida Configurazione Render.com

## Problema
L'app pubblicata su Render.com non trova le pubblicazioni perché mancano le variabili d'ambiente necessarie per Google Sheets API.

## Soluzione

### 1. Configura le Variabili d'Ambiente su Render.com

Vai sul dashboard di Render.com e aggiungi queste variabili d'ambiente al tuo servizio:

#### GOOGLE_CREDENTIALS
- **Chiave**: `GOOGLE_CREDENTIALS`
- **Valore**: Il contenuto completo del tuo file `credentials.json` (tutto il JSON in una riga)

**Come ottenere il valore:**
1. Apri il file `credentials.json` locale
2. Copia tutto il contenuto JSON
3. Incollalo come valore della variabile d'ambiente

#### SPREADSHEET_ID
- **Chiave**: `SPREADSHEET_ID`
- **Valore**: L'ID del tuo Google Sheets (es: `1-Ki64dOkwpWeiBsR_4o6CTOGuXqQ-jWnIqNDTaBWVl8`)

### 2. Test della Configurazione

Esegui lo script di test per verificare che tutto sia configurato correttamente:

```bash
python test_config.py
```

### 3. Riavvio del Servizio

Dopo aver configurato le variabili d'ambiente:
1. Vai sul dashboard di Render.com
2. Trova il tuo servizio
3. Clicca su "Manual Deploy" o "Redeploy"

## Verifica

Dopo la configurazione, l'app dovrebbe funzionare correttamente su Render.com come funziona in locale.

## Troubleshooting

Se l'app ancora non funziona:

1. **Controlla i log**: Vai su Render.com → Dashboard → Logs
2. **Verifica le variabili**: Usa lo script `test_config.py`
3. **Controlla i permessi**: Assicurati che il service account abbia accesso al Google Sheets

## Differenze tra Locale e Render.com

| Ambiente | Credenziali | File |
|----------|-------------|------|
| **Locale** | File `credentials.json` | Presente nella cartella |
| **Render.com** | Variabile `GOOGLE_CREDENTIALS` | Configurata nel dashboard |
