#!/usr/bin/env python3
"""
Test semplificato per verificare la connessione Google Sheets
"""

import os
import json

def test_connessione_semplice():
    """Test semplificato della connessione"""
    print("🔍 Test connessione Google Sheets semplificato...")
    print("=" * 50)
    
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        
        # Usa il file credentials.json locale
        if os.path.exists('credentials.json'):
            print("✅ Usando file credentials.json locale")
            credentials = service_account.Credentials.from_service_account_file(
                'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
        else:
            print("❌ File credentials.json non trovato")
            return
        
        service = build('sheets', 'v4', credentials=credentials)
        
        # Test con SPREADSHEET_ID dall'ambiente o dal codice
        spreadsheet_id = os.environ.get('SPREADSHEET_ID', '1-Ki64dOkwpWeiBsR_4o6CTOGuXqQ-jWnIqNDTaBWVl8')
        print(f"🔍 Test con SPREADSHEET_ID: {spreadsheet_id}")
        
        try:
            result = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
            print(f"✅ Connessione Google Sheets: SUCCESSO!")
            print(f"   - Titolo: {result.get('properties', {}).get('title', 'N/A')}")
            print(f"   - Fogli disponibili: {len(result.get('sheets', []))}")
            
            # Lista i fogli
            for i, sheet in enumerate(result.get('sheets', [])):
                sheet_name = sheet['properties']['title']
                print(f"   - Foglio {i+1}: {sheet_name}")
                
        except Exception as e:
            print(f"❌ Errore accesso al foglio: {e}")
            
    except Exception as e:
        print(f"❌ Errore test connessione: {e}")
        print(f"   Tipo errore: {type(e).__name__}")

if __name__ == "__main__":
    test_connessione_semplice()
