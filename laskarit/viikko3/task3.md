```mermaid

  sequenceDiagram
    main->>+Machine: Machine()
    Machine->>+FuelTank: FuelTank()
    Machine->>FuelTank: fill(40)
    Machine->>+Engine: Engine(40)
    deactivate Machine
    main->>Machine: drive()
    Machine->>Engine: start()
    
````
