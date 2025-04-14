# Ejercicio: Sistema de Reservas de Vuelos

# Imagina que estamos creando un sistema para una pequeña agencia de viajes
# que permite a los usuarios reservar vuelos, ver disponibilidad, y cancelar reservas.
# Este sistema debe manejar una lista de vuelos, con cada vuelo teniendo una fecha, hora, origen, destino, y
# una cantidad limitada de asientos disponibles.

list_of_flights = [
    {
        "flight_number": "123",
        "date": "2025-06-01",
        "time": "10:00",
        "origin": "New York",
        "destination": "London",
        "available_seats": 10,
        "price": 100
    },
    {
        "flight_number": "456",
        "date": "2025-06-02",
        "time": "14:00",
        "origin": "Paris",
        "destination": "Tokyo",
        "available_seats": 5,
        "price": 200
    },
    {
        "flight_number": "789",
        "date": "2025-06-03",
        "time": "18:00",
        "origin": "Sydney",
        "destination": "Tokyo",
        "available_seats": 3,
        "price": 300
    }
]


def show_flights():
    print("Lista de vuelos disponibles:")
    for flight in list_of_flights:
        print(f"Vuelo {flight["flight_number"]}: {flight["origin"]} -> {flight["destination"]}, "
              f"Fecha: {flight["date"]} {flight["time"]}, Asientos disponibles: {flight["available_seats"]}, "
              f"Precio: {flight["price"]}")


reservations = []

while True:
    print("1. Ver disponibilidad de vuelos")
    print("2. Reservar vuelo")
    print("3. Cancelar reserva")
    print("4. Ver reservas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        show_flights()

    elif opcion == "2":
        show_flights()
        flight_number = input("Ingrese el número de vuelo para reservar: ")

        selected_flight = None
        for flight in list_of_flights:
            if flight["flight_number"] == flight_number:
                selected_flight = flight
                break

        if selected_flight is None:
            print("Número de vuelo no encontrado.")
            continue

        if selected_flight["available_seats"] <= 0:
            print("Lo siento, ya no hay asientos disponibles en este vuelo.")
            continue

        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")
        age = input("Ingrese su edad: ")
        email = input("Ingrese su email: ")
        phone = input("Ingrese su teléfono: ")

        selected_flight["available_seats"] -= 1
        reservations.append({
            "flight_number": flight_number,
            "name": name,
            "last_name": last_name,
            "age": age,
            "email": email,
            "phone": phone
        })

        print("Reserva realizada con éxito.")

    elif opcion == "3":
        show_flights()
        flight_number = input(
            "Ingrese el número de vuelo para cancelar la reserva: ")
        name = input("Ingrese su nombre: ")
        last_name = input("Ingrese su apellido: ")

        reserva_encontrada = None
        for reserva in reservations:
            if reserva["flight_number"] == flight_number and reserva["name"] == name and reserva["last_name"] == last_name:
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            reservations.remove(reserva_encontrada)
            for flight in list_of_flights:
                if flight["flight_number"] == flight_number:
                    flight["available_seats"] += 1
                    break
            print("Reserva cancelada con éxito.")
        else:
            print("Reserva no encontrada.")

    elif opcion == "4":
        if not reservations:
            print("No hay reservas registradas.")
        else:
            for reserva in reservations:
                print(
                    f"Reserva para el vuelo {reserva["flight_number"]}: {reserva["name"]} {reserva["last_name"]}")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Por favor, seleccione 1, 2, 3 ,4 o 5.")
