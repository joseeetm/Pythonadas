# positional params
def calculate_expenses(plane_ticket_price,car_rental_rate,hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = (hotel_rate * trip_time)- 10
    trip_total = hotel_total + car_rental_total + plane_ticket_price
    return trip_total

print(calculate_expenses(200,100,100,5))

# trip_planner with final_destination with default_value
def trip_planner(first_destination ,second_destination, final_destination = "Codecademy HQ" ):
    print('Here is what your trip will look like!')
    #print('First, we will stop in' ,first_destination ,', then', second_destination, ', and lastly', final_destination)
    print(f'First, we will stop in {first_destination}, {second_destination}, and lastly {final_destination}')


# positional arguments call
trip_planner("France","Germany","Denmark")


# argument keyword call
trip_planner(first_destination = "Iceland", final_destination = "Germany",second_destination = "India")

# using positional and default argument value
trip_planner("Brooklyn", "Queens")