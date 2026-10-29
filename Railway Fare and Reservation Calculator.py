
distance = float(input("Enter travel distance in km: "))
travel_class = input("Enter class (Sleeper/AC): ").lower()
passengers = int(input("Enter number of passengers: "))

if distance <= 0 or passengers <= 0:
    print("Invalid distance or passenger count.")
elif travel_class not in ("sleeper", "ac"):
    print("Invalid travel class.")
else:
    if travel_class == "sleeper":
        rate = 1.50
    else:
        rate = 3.00

    total_fare = 0

    for i in range(passengers):
        age = int(input("Enter age of passenger: "))

        if age < 0:
            print("Invalid age.")
            continue

        if age < 5:
            fare = 0
        else:
            fare = distance * rate

            if age <= 11:
                fare = fare * 0.50
            elif age >= 60:
                fare = fare * 0.80

            fare = fare + 40

        total_fare = total_fare + fare
        print("Passenger", i + 1,
              "Fare: Rs.", round(fare, 2))

    print("\nTotal Railway Fare: Rs.",
          round(total_fare, 2))

    cancellation = total_fare * 0.25
    print("Sample Cancellation Penalty (25%): Rs.",
          round(cancellation, 2))
    print("Refund after cancellation: Rs.",
          round(total_fare - cancellation, 2))

'''Enter travel distance in km: 100
Enter class (Sleeper/AC): Sleeper
Enter number of passengers: 3
Enter age of passenger: 4
Enter age of passenger: 10
Enter age of passenger: 65
Passenger 1 Fare: Rs. 0
Passenger 2 Fare: Rs. 115.0
Passenger 3 Fare: Rs. 160.0

Total Railway Fare: Rs. 275.0
Sample Cancellation Penalty (25%): Rs. 68.75
Refund after cancellation: Rs. 206.25'''


flowchart TD
    A([Start]) --> B[/Enter distance, class and passenger count/]
    B --> C{Distance > 0 and passengers > 0?}
    C -- No --> D[Display invalid distance or passenger count]
    D --> Z([Stop])
    C -- Yes --> E{Class is Sleeper or AC?}
    E -- No --> F[Display Invalid travel class]
    F --> Z
    E -- Yes --> G[Set fare rate and total fare = 0]
    G --> H[/Enter passenger age/]
    H --> I{Age < 0?}
    I -- Yes --> J[Display Invalid age]
    I -- No --> K{Age < 5?}
    K -- Yes --> L[Passenger fare = 0]
    K -- No --> M[Calculate distance fare]
    M --> N{Age <= 11?}
    N -- Yes --> O[Apply 50% concession]
    N -- No --> P{Age >= 60?}
    P -- Yes --> Q[Apply 20% concession]
    P -- No --> R[Keep full distance fare]
    O --> S[Add reservation charge of Rs. 40]
    Q --> S
    R --> S
    L --> T[Add fare to total and display passenger fare]
    S --> T
    J --> U{More passengers?}
    T --> U
    U -- Yes --> H
    U -- No --> V[Display total railway fare]
    V --> W[Calculate 25% cancellation penalty and refund]
    W --> X[Display penalty and refund]
    X --> Z
