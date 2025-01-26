# class laptop:
#     def brand(self,name):
#         print(f"Brand name is {name}")

# class Dell(laptop):
#     pass 
# class Mac(laptop):
#     pass
# obj=Dell()
# obj.brand("Dell")
# obj1=Mac()
# obj1.brand("Mac")


# class mobile:
#     def brand(self,name):
#         print(f"brand name is {name}") 
# class Samgsung(mobile):
#     pass
# class Iphone(mobile):
#     pass
# obj=Samgsung()
# obj.brand("Samgsung")
# obj1=Iphone()
# obj1.brand("Iphone")



class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")

class Samsung(Mobile):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels

    def display_info(self):
        super().display_info()
        print(f"Camera Megapixels: {self.camera_megapixels}")

class Apple(Mobile):
    def __init__(self, brand, model, price, os_version):
        super().__init__(brand, model, price)
        self.os_version = os_version

    def display_info(self):
        super().display_info()
        print(f"OS Version: {self.os_version}")

# Create objects
samsung_phone = Samsung("Samsung", "Galaxy S23", 50000, 50)
apple_phone = Apple("Apple", "iPhone 14", 70000, "iOS 16")

# Display information
samsung_phone.display_info()
print()
apple_phone.display_info()