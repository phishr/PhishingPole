import requests

url = "https://lowderwithcrowder.000webhostapp.com/mail.php"

r = requests.post(url, data={'to': 'eliasbothell@outlook.com', 'from': 'Ramon Dailey support@daileycomputer.com <support@daileycomputer.com>', 'subject': 'Hey Bro','message': 'Hey dawg, I just wanted you to know that youre FUCKING GAY'})

print(r.text[:100])