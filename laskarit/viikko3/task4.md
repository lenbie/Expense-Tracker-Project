```mermaid
  sequenceDiagram
  Main->>main: main()
  main->>laitehallinto: HKLLaitehallinto()
  main->>rautatietori: Lataajalaite()
  main->>ratikka6: Lukijalaite()
  main->>bussi244: Lukijalaite()
  main->>laitehallinto: lisaa_lataaja(rautatietori)
  main->>laitehallinto: lisaa_lukija(ratikka6)
  main->>laitehallinto: lisaa_lukija(bussi244)
  main->>lippu_luukku: Kioski()
  main->>lippu_luukku: osta_matkakortti("Kalle")
  lippu_lukku->>Matkakortti: Matkakortti(Kalle)
  lippu_luukku-->>kallen_kortti: uusi_kortti
  main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
  rautatietori->>kallen_kortti: kasvata_arvoa(3)
  main->>+ratikka6: osta_lippu(kallen_kortti, 0)
  ratikka6->>Main: RATIKKA
  Main-->>ratikka6: 1.5
  ratikka6->>kallen_kortti: kortti.arvoa
  kallen_kortti-->>ratikka6: 3
  ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
  ratikka6-->>-main: True
  main->>bussi244: osta_lippu(kallen_kortti, 2)
  bussi244->>Main: SEUTU
  Main-->>bussi244: 3.5
  bussi244->>kallen_kortti: kortti.arvoa
  kallen_kortti-->>bussi244: 1.5
  bussi244-->>main: False
  
  
```
