Monopoly
---
```mermaid
  classDiagram
        Monopoly game "1" --> "1" Game board
        class Monopoly game{
                }
        class Game board{
        }
        Monopoly game "1" --> "2" Dice
        class Dice{
        }
        Monopoly game "1! --> "2..8" Players
        class Players{
        }
```
