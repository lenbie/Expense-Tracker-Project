```mermaid

  sequenceDiagram
    main->>+Machine: Machine()
    Machine->>+FuelTank: FuelTank()
    Machine->>FuelTank: fill(40)
    deactivate FuelTank
    Machine->>+Engine: Engine(40)
    deactivate Engine
    deactivate Machine
    main->>+Machine: drive()
    Machine->>+Engine: start()
    Engine->>+FuelTank: consume(5)
    deactivate Engine
    deactivate FuelTank
    Machine->>+Engine: is_running()
    Engine->>+FuelTank: fuel_contents()
    FuelTank-->>Engine: 35
    deactivate FuelTank
    Engine-->>Machine: True
    deactivate Engine
    Machine->>+Engine: use_energy()
    Engine->>+FuelTank: consume(10)
    deactivate Machine
    deactivate Engine
    deactivate FuelTank
 
````
