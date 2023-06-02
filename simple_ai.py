import sys, time, random

# List of greetings
greetings = ["Hello", "Hi", "Hey there", "Good morning", "Good afternoon",
             "Good evening", "Howdy", "Greetings", "Salutations", "What's up?",
             "How are you?", "How's it going?", "Nice to see you", "Long time no see",
             "How have you been?", "What's new?", "How's your day going?",
             "How's everything?", "It's a pleasure to meet you", "Welcome"]

# Dictionary of car information
car_info = {
    "Nissan": "Nissan is a Japanese car manufacturer known for its reliable and fuel-efficient vehicles.",
    "Ford": "Ford is an American automaker known for its wide range of vehicles, including trucks and SUVs.",
    "Audi": "Audi is a German luxury car manufacturer renowned for its elegant designs and advanced technology.",
    "BMW": "BMW is a German automobile company famous for producing high-performance and luxury vehicles.",
    "Toyota": "Toyota is a Japanese car manufacturer recognized for its durability, quality, and innovation.",
    "Chevrolet": "Chevrolet is an American automobile division of General Motors, offering a diverse lineup of cars, trucks, and SUVs.",
    "Mercedes-Benz": "Mercedes-Benz is a German luxury car brand that is synonymous with comfort, refinement, and cutting-edge technology.",
    "Honda": "Honda is a Japanese automaker known for producing reliable and fuel-efficient vehicles, including cars, motorcycles, and power equipment.",
    "Hyundai": "Hyundai is a South Korean automaker that has gained popularity for its affordable and feature-packed vehicles.",
    "Tesla": "Tesla is an American electric vehicle manufacturer renowned for its innovative electric cars and sustainable energy solutions."
}

typing_speed = 70  # Words per minute for typing simulation

# Function to simulate typing effect
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)

# Starting message
print("Hello, you can type a car brand and I will tell you some information about it.")

while True:
    person_input = input("User: ")  # Get user input

    if person_input in greetings:  # If user input matches a greeting
        slow_type("Hello, which car would you like to know about?")
        print()
    elif person_input in car_info:  # If user input matches a car brand
        slow_type(car_info[person_input])
        print()
    else:
        print("I can only talk about cars. Also, you should always check if you spelled it correctly and used the first capital letter!")
