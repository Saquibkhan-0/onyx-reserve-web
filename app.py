from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Expanded Luxury & Performance Fleet Database
fleet_data = [
    {
        "id": 1, "brand": "Porsche", "model": "911 GT3 RS", "color": "Alpine White", 
        "price": "45,000", "engine": "4.0L Naturally Aspirated Flat-6", "hp": "518 HP", 
        "img": "https://i.pinimg.com/1200x/f9/b6/70/f9b6700a023b5e83ee98c6ebb4e6444a.jpg"
    },
    {
        "id": 2, "brand": "BMW", "model": "M4 Competition", "color": "Sapphire Black", 
        "price":  "25,000" , "engine": "3.0L Twin-Turbo Inline-6", "hp": "503 HP", 
        "img": "https://i.pinimg.com/736x/4f/7a/ea/4f7aea0d417a5401a3562207838616f9.jpg"
    },
    {
        "id": 3, "brand": "Mercedes-AMG", "model": "GT R", "color": "Selenite Grey", 
        "price": "38,000" , "engine": "4.0L Biturbo V8", "hp": "577 HP", 
        "img": "https://i.pinimg.com/736x/2c/a2/aa/2ca2aa3f3f5dc00cd250cd50ffe0757a.jpg"
    },
    {
        "id": 4, "brand": "Audi", "model": "RS6 Avant", "color": "Nardo Gray", 
        "price": "28,000" , "engine": "4.0L Twin-Turbo V8", "hp": "591 HP", 
        "img": "https://i.pinimg.com/736x/44/a8/8f/44a88f0a9f3b1d45e88689bfd195680f.jpg"
    },
    {
        "id": 5, "brand": "Lexus", "model": "LC 500", "color": "Infrared", 
        "price": "24,000" , "engine": "5.0L V8", "hp": "471 HP", 
        "img": "https://i.pinimg.com/1200x/3d/db/f2/3ddbf207344f56a12660030f8fe8e742.jpg"
    },
    {
        "id": 6, "brand": "Volkswagen", "model": "Golf R", "color": "Lapiz Blue", 
        "price": "15,000" , "engine": "2.0L Turbocharged Inline-4", "hp": "315 HP", 
        "img": "https://i.pinimg.com/736x/df/dd/09/dfdd09372d0490c4c15ee76abf142356.jpg"
    },
    {
        "id": 7, "brand": "Nissan", "model": "GT-R Nismo", "color": "Pearl White", 
        "price": "35,000" , "engine": "3.8L Twin-Turbo V6", "hp": "600 HP", 
        "img": "https://bringatrailer.com/wp-content/uploads/2023/04/2021_nissan_gt-r_bc3829d9ad66c6135ed466b484783a3c-21985.jpg"
    },
    {
        "id": 8, "brand": "Audi", "model": "R8 V10 Performance", "color": "Mythos Black", 
        "price": "42,000" , "engine": "5.2L Naturally Aspirated V10", "hp": "602 HP", 
        "img": "https://i.pinimg.com/736x/9f/94/08/9f9408c6ab812cf8c3095a84b2a24e5a.jpg"
    },
    {
        "id": 9, "brand": "Mercedes-AMG", "model": "G 63", "color": "Obsidian Black", 
        "price": "40,000", "engine": "4.0L Biturbo V8", "hp": "577 HP", 
        "img": "https://i.pinimg.com/736x/6a/b8/1c/6ab81c449e1b4c129e958cd48366f87a.jpg"
    },
    {
        "id": 10, "brand": "Porsche", "model": "Taycan Turbo S", "color": "Carmine Red", 
        "price": "35,000" , "engine": "Dual Electric Motors", "hp": "750 HP", 
        "img": "https://prs.porsche.com/iod/image/US/Y1AFM1/1/N4Igxg9gdgZglgcxALlAQynAtmgLnaAZxQG0BdAGnDSwFMAnNFUOAExRFoA9cBaAGwgB3XjHrQ+-WjFwgqEAA74izEADc09OBlnIQrWoQDWuRSAC+5qrShq44qHSi6W7PQHk0hOMXlKCUMSollT8iAAW+FBIqCBsHAAiAIIAmnIgisqBzCEgCuKsAK5gLnFuICkAjEkAYgCylemZAUGgkLCIpCAADAAy6d0AcgCsAwCKgwMAKgnplQDiABxzvQAac4MAzBvrVJUACgCic6uNVABMAMIA7OnnNQBSdw8AQncA6gCc6ZsvACw-Gr7H4AaQAEj99pMqH9FrMYUkATCEtsYTUAGzpP4AVTeMNWSJAwzqEKow1WuyJAC1gVR0TVuul6U86fMkkyHvCQOiQd86YMpkyAEqXJmrABq6Wu3Up102xyo13R7MVSX6ipBqJA1zqy0V2PmUpSepAiwAktj0oteoaqItxeqQJ9hninQ8VU66lrPvtblRPkKzk7xSyne9Bf6qQqQElFqSY2a+SBDosPYc6ud0jUplqalTGVR5pVKfMwVr5l70vMppjC+Kg2CPWbFkmzeLM1Qze8tQ9PmN0g8wR2QCDFgBldIgl5a8GjKg2mZCx11FHpQYPYeDd6E-Z-V27idUfax9JjSqhsYPQljTWns+noVJsbYk1jd5zkDYhJB7FjP0gcVLmHcUGXSB0CwAoVMUocAIEKZx6AATw4bFDxALAIAMfgUloTQUHObpznRSwrBAQhaFwKIEFaEAYAgegcF0EAACsFFoJAqFwRhAgUTQbF0GA0H4cjLCAA?clientId=icc"
    }
]

@app.route('/')
def index():
    return render_template('index.html', cars=fleet_data)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cars')
def cars():
    return render_template('cars.html', cars=fleet_data)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/book/<int:car_id>', methods=['GET', 'POST'])
def book_car(car_id):
    selected_car = next((car for car in fleet_data if car["id"] == car_id), None)
    
    if request.method == 'POST':
        customer_name = request.form.get('name')
        email = request.form.get('email')
        start_date = request.form.get('start_date')
        
        # Grab the exact number of days entered in the form
        try:
              days = int(request.form.get('days'))
              if days < 1:
                  days = 1
        except (ValueError, TypeError):
             days = 1 # Fallback if left blank
            
        # Force the database price into an integer (and strip any accidental commas)
        clean_price = int(str(selected_car['price']).replace(',', ''))
        total_price = days * clean_price
        
        print(f"NEW BOOKING: {customer_name} booked {selected_car['brand']} {selected_car['model']} for {days} days. Total: ₹{total_price}")
        
        return render_template('success.html', name=customer_name, car=selected_car, days=days, total_price=total_price)
        
    return render_template('book.html', car=selected_car)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Log the message to the backend terminal
        print(f"\n--- INCOMING TRANSMISSION ---")
        print(f"Client: {name} ({email})")
        print(f"Message: {message}")
        print(f"-----------------------------\n")
        
        # Reload the page and pass a success flag
        return render_template('contact.html', success=True)
        
    return render_template('contact.html')
@app.route('/book/<int:car_id>', methods=['GET', 'POST'])
def book(car_id):
    selected_car = next((car for car in fleet_data if car["id"] == car_id), None)
    
    if request.method == 'POST':
        data = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "dates": f"{request.form.get('start_date')} to {request.form.get('end_date')}"
        }
        print(f"\n--- TELEMETRY LOG: NEW BOOKING ---")
        print(f"Client: {data['name']} | Vehicle: {selected_car['brand']} {selected_car['model']}")
        print(f"----------------------------------\n")
        return render_template('success.html', data=data, car=selected_car)
        
    return render_template('book.html', car=selected_car)

if __name__ == '__main__':
    app.run(debug=True, port=5000)