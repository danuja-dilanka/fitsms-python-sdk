# FitSMS Python SDK (v4)

The official Python SDK for the [FitSMS.lk](https://fitsms.lk) gateway, maintained by Global Cloud Media. This package provides a seamless way to integrate SMS capabilities into Python applications, automation scripts, and AI agents using the FitSMS v4 API.

---

## 🚀 Features

- **Auto-Formatting**: Converts Sri Lankan numbers into `947XXXXXXXX` format.
- **v4 Support**: Fully compatible with FitSMS v4 REST API.
- **Requests Powered**: Uses the industry-standard `requests` library.
- **DevOps Ready**: Lightweight and ideal for VPS alerts, cron jobs, and monitoring systems.

---

## 📦 Installation

```bash
pip install fitsms
```

---

## ⚡ Quick Start

### 1. Initialize the Client

```python
from fitsms import FitSMS

api_token = 'YOUR_V4_API_TOKEN'
sender_id = 'YOUR_SENDER_ID'

sms = FitSMS(api_token, sender_id)
```

---

### 2. Send an SMS

```python
try:
    response = sms.send('0761234567', 'Hello from Global Cloud Media!')

    if response.get('status') == 'success':
        print(f"Message Sent! RUID: {response['data']['ruid']}")
    else:
        print(f"Failed: {response.get('message')}")

except Exception as e:
    print(f"Error: {str(e)}")
```

---

### 3. Check Account Balance

```python
balance = sms.get_balance()
print(f"Remaining Units: {balance['data']['sms_unit']}")
```

---

## 📖 API Reference

| Method        | Parameters                  | Description |
|--------------|---------------------------|------------|
| send()       | recipient(s), message     | Send SMS (Single/Bulk) |
| get_balance()| none                      | Get SMS unit balance |
| get_status() | ruid, recipient           | Check delivery status |
| get_profile()| none                      | Get account details |

---

## ⚙️ Advanced Usage

### Manual Status Reconciliation

```python
import time

time.sleep(10)

status = sms.get_status(
    'fe424939fc3c4b6dbcc876994517d712',
    '0761234567'
)

print(status)
```

---

### 🇱🇰 Sri Lankan Number Formatting

The SDK automatically formats numbers:

```
0761234567   → 94761234567
761234567    → 94761234567
+94761234567 → 94761234567
```

---

## 🔔 Webhook Integration (Recommended)

FitSMS v4 uses webhooks for real-time delivery updates.

### Sample Webhook Payload

```json
{
    "status": "success",
    "data": {
        "to": "94770000000",
        "from": "MyBrand",
        "message": "Test",
        "ruid": "fe424939fc3c4b6dbcc876994517d712",
        "received_at": "2026-03-28T23:24:22+05:30"
    }
}
```

### Example Flask Webhook

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sms-webhook', methods=['POST'])
def sms_webhook():
    data = request.json

    print("SMS Status Update:", data)

    # Example DB update
    # update_message_status(data['data']['ruid'], data['data']['status'])

    return jsonify({'status': 'ok'})
```

---

## 🛡 Best Practices

- Use environment variables:
```python
import os
api_token = os.getenv('FITSMS_API_TOKEN')
```

- Store and index `ruid` in your database
- Log all API responses
- Prefer webhooks over polling

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 👨‍💻 Maintainer

Maintained by [Global Cloud Media (pvt) Ltd.](https://globalcloudmedia.lk)