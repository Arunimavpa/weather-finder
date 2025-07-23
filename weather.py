import requests
class Weather:
    def __init__(self,api_key):
        self.api_key=api_key

    def get_weather(self,city):
        if not city:
            return "Not found"
        
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response=requests.get(url)

        if response.status_code!=200:
            return "Not found"
        
        data=response.json()
        temp=data["main"]["temp"]
        description=data["weather"][0]["description"]
        name=data["name"]
        return f"{name}: {temp}°C, {description}"

if __name__== "__main__":
    api_key="7b987133563f30c2e1d25fdaba64be07"
    city=input("Enter the city : ")
    w=Weather(api_key)
    print(w.get_weather(city))