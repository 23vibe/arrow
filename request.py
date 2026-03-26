import requests

url = "http://localhost:7071/api/sendEmail"

# Example data; replace with your test values
payload = {
	"name": "Test User",
	"email": "ivan.sivacek@webcom.cz",
	"message": "This is a test message."
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Raw text:", response.text)
