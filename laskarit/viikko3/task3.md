```mermaid
  sequenceDiagram
  participant main
  participant Machine
  main->>Machine: Machine()
  activate Machine
  Machine->>FuelTank: FuelTank()
  activate FuelTahnk
  Machine->>FuelTank: fill(40)
  Machine->>Engine: Engine(40)
  activate Engine
  main->>Machine: drive()
  Machine->>Engine
````
