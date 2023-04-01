```mermaid
  sequenceDiagram
  participant main
  participant Machine
  main->>+Machine: Machine()
  Machine->>+FuelTank: FuelTank()
  Machine->>FuelTank: fill(40)
  Machine->>+Engine: Engine(40)
  main->>Machine: drive()
  Machine->>Engine
  deactivate Machine
  deactivate FuelTank
  deactivate Engine
````
