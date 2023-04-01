```mermaid

  sequenceDiagram
    main->>+Machine: Machine()
    Machine->>+FuelTank: FuelTank()
    Machine->>FuelTank: fill(40)
    deactivate FuelTank
    Machine->>+Engine: Engine(40)
    deactivate Engine
    deactivate Machine
    main->>Machine: drive()
    Machine->>Engine: start()
    
````
