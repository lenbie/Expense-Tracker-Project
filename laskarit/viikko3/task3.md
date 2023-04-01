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
    Machine->>Engine: is_running()
    Engine->>FuelTank: fuel_contents()
    FuelTank->>Engine: fuel_contents()
    Engine->>Machine: True
    Machine->>Engine: use_energy()
    Engine->>FuelTank: consume()
    deactivate Machine
    deactivate Engine
    deactivate FuelTank
 
````
