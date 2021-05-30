import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
predmet = ["Istorija racunarstva","Majkrosoft teghnologije za pristup podacima","Kriptografija"]

class kontakt: 
    adresa = "Ruzveltova 43",
    mesto = "Beograd",
    telefon = "060 122 122"

kontakt = kontakt()

payload = json.dumps({
  "id" : "123456",
  "ime": "Marko",
  "prezime":"Lazarevic",
  "smer": "Informacione tehnologije",
  "predmet": predmet,
  "prosek" : "6.2",
  "kontakt": [kontakt.adresa,kontakt.mesto,kontakt.telefon] 

})

headers = {
  'Content-Type': 'application/json'
}

conn.request("POST", "/apiv1/pantry/5055caaf-0972-4e9f-86f0-2a9ab97bf1e7/basket/Marko", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))