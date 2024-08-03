import requests

class Flights():
    def __init__(self):
        self.api_url = "https://api.turkishairlines.com"

    def calculateFlightMiles(self):
        response = requests.get(f"{self.api_url}/test/calculateFlightMiles")
        data = response.json()
        return data
    
ucus = Flights()

while True:
    secim = input("q for exit otherwise type 1  ")
    if secim == "q":
        break
    else:
        if secim == "1":
            result = ucus.calculateFlightMiles()
            print(result)