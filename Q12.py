# 12. Static Methods                                                 Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


#  Formula____  Fahrenheit=(Celsius×9/5)+32
class TemperatureConvertor:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return  (c * 9/5) +32
    
c = 25
temp_f = TemperatureConvertor.celsius_to_fahrenheit(c)
print("temp-c:", c, "Convert temp-f:", temp_f) 