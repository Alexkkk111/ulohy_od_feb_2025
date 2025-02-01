

class City:
    def __init__(self, city_name, region, country, no_citizens, zip_code, area_code):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.no_citizens = no_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def print_adress(self):
        print(f"Adresa pre mesto {self.city_name} je: {self.city_name}, {self.region},{self.zip_code},{self.area_code}")

Nitra = City("Nitra", "Nitriansky kraj", "Slovensko", 100000,"949 01","SK023")
Nitra.print_adress()