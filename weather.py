import requests
API_KEY="7b987133563f30c2e1d25fdaba64be07"
def weather(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    if response.status_code!=200:
        return "Not Found"
    data=response.json()
    temperature=data["main"]["temp"]
    description=data["weather"][0]["description"]
    city_name=data["name"]
    return f"{city_name}: {temperature}°C, {description}"

if __name__== "__main__":
    city=input("Enter the city : ")
    print(weather(city))