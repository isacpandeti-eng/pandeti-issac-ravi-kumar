

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
