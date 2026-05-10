import requests

url = "https://g2-data-api.p.rapidapi.com/g2-products"

querystring = {"product":"postman","max_reviews":"1000"}

headers = {
	"x-rapidapi-key": "934596b695msh080ef90b49c9542p1754c1jsne5208e246c77",
	"x-rapidapi-host": "g2-data-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())