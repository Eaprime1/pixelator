# Google Drive Integration Setup

## Overview
To run scripts from Google Drive, you have several options:

### Option 1: Google Apps Script (Recommended)
- Create scripts directly in Google Drive using Apps Script
- Can trigger from web apps or time-based triggers
- Access via: script.google.com

### Option 2: Google Drive API + Local Server
- Authenticate using OAuth2
- Download and execute scripts from Drive
- Requires setup of credentials

### Option 3: Webhook Integration
- Use the current GPS app to POST data to Google Apps Script
- Apps Script can then process and store in Google Sheets/Drive

## Quick Setup for Apps Script Integration

1. Go to script.google.com
2. Create a new project
3. Use this code to receive GPS data:

```javascript
function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  const sheet = SpreadsheetApp.openById('YOUR_SHEET_ID').getActiveSheet();
  
  sheet.appendRow([
    new Date(),
    data.latitude,
    data.longitude,
    data.accuracy,
    data.provider
  ]);
  
  return ContentService.createTextOutput('Success');
}
```

4. Deploy as web app
5. Add the webhook URL to your GPS app

## Environment Variables Needed
```bash
export GOOGLE_DRIVE_WEBHOOK_URL="your_apps_script_url"
export GOOGLE_CLIENT_ID="your_client_id"
export GOOGLE_CLIENT_SECRET="your_client_secret"
```