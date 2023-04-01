---

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
        Monopoly game "1" --> "2..8" Player
        class Player{
        }
        Game board "1" --> "40" Tile
        class Tile{
          next
        }
```
