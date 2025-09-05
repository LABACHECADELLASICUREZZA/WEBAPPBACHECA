#!/usr/bin/env python3
"""
Script di test per verificare la configurazione delle variabili d'ambiente
Esegui questo script per controllare se tutto è configurato correttamente
"""

import os
import json

def test_configurazione():
    """Testa la configurazione delle variabili d'ambiente"""
    print("🔍 Test configurazione variabili d'ambiente...")
    print("=" * 50)
    
    # Test GOOGLE_CREDENTIALS
    google_credentials = os.environ.get('GOOGLE_CREDENTIALS')
    if google_credentials:
        try:
            # Prova a parsare il JSON
            credentials_info = json.loads(google_credentials)
            print("✅ GOOGLE_CREDENTIALS: PRESENTE e valido")
            print(f"   - Tipo account: {credentials_info.get('type', 'N/A')}")
            print(f"   - Project ID: {credentials_info.get('project_id', 'N/A')}")
        except json.JSONDecodeError:
            print("❌ GOOGLE_CREDENTIALS: PRESENTE ma JSON non valido")
    else:
        print("❌ GOOGLE_CREDENTIALS: MANCANTE")
    
    # Test SPREADSHEET_ID
    spreadsheet_id = os.environ.get('SPREADSHEET_ID')
    if spreadsheet_id:
        print(f"✅ SPREADSHEET_ID: PRESENTE - {spreadsheet_id}")
    else:
        print("❌ SPREADSHEET_ID: MANCANTE")
    
    # Test file credentials.json locale
    if os.path.exists('credentials.json'):
        print("✅ credentials.json: PRESENTE (locale)")
    else:
        print("⚠️ credentials.json: MANCANTE (locale)")
    
    print("=" * 50)
    
    # Test connessione Google Sheets
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        
        print("🔍 Test connessione Google Sheets...")
        
        if google_credentials:
            # Usa variabili d'ambiente
            credentials_info = json.loads(google_credentials)
            credentials = service_account.Credentials.from_service_account_info(
                credentials_info, scopes=['https://www.googleapis.com/auth/spreadsheets'])
        elif os.path.exists('credentials.json'):
            # Usa file locale
            credentials = service_account.Credentials.from_service_account_file(
                'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
        else:
            print("❌ Nessuna credenziale disponibile")
            return
        
        service = build('sheets', 'v4', credentials=credentials)
        
        # Test accesso al foglio
        if spreadsheet_id:
            try:
                result = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
                print(f"✅ Connessione Google Sheets: SUCCESSO")
                print(f"   - Titolo: {result.get('properties', {}).get('title', 'N/A')}")
                print(f"   - Fogli disponibili: {len(result.get('sheets', []))}")
            except Exception as e:
                print(f"❌ Errore accesso al foglio: {e}")
        else:
            print("⚠️ SPREADSHEET_ID mancante, impossibile testare l'accesso")
            
    except Exception as e:
        print(f"❌ Errore test connessione: {e}")

if __name__ == "__main__":
    test_configurazione()
