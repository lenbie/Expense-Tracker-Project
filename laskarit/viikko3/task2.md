---

Monopoly
---
```mermaid
  classDiagram
    Monopoly_game "1" -- "1" Game_board
      class Monopoly_game{
        start.location
        prison.location
      }
      class Game_board{
      }
    Monopoly_game "1" -- "2" Dice
      class Dice{
      }
    Monopoly_game "1" -- "2..8" Player
      class Player{
        money
      }
    Game_board "1" -- "40" Tile
      class Tile{
        next
        function()
      }
    Player "2..8" -- "1" Game_piece
      class Game_piece{
      }
    Tile "40" -- "1" Game_piece"
    Tile "40" -- "1" Start
      class Start{
        location
        function()
      }
    Tile "40" -- "1" Prison
      class Prison{
        location
        function()
      }
    Tile "40" -- "3" Chance
      class Chance{
        function()
      }
    Tile "40" -- "3" Community_chest
      class Community_chest{
          function()
      }
    Community_chest "3" -- Community_chest_card
      class Community_chest_card{
        function()
      }
    Chance "3" -- Chance_card
      class Chance_card{
        function()
      }
    Tile "40" -- "2" Utility
      class Utility{
        function()
      }
    Tile "40" -- "4" Railroad_stations
      class Railroad_stations{
        function()
      }
    Tile "40" -- "28" Normal_street
      class Normal_street{
        name
        function()
      }
    Normal_street "28" -- "0..1" Hotel
      class Hotel{
      }
    Normal_street "28" -- "0..4" House
      class House {
      }
    Player "8" --> "28" Normal_street
```
