# PokeDream — ROADMAP de Progressão

> Framework de decisão para o Hermes Agent.
> Não é linear — adapta conforme as capturas e o progresso.
> Versão 3.0 — Baseada em decisões, não em etapas fixas.

---

## 🎯 Filosofia do Jogo

| Arquivo        | Quem escreve           | Quem lê                     |
| -------------- | ---------------------- | --------------------------- |
| `ROADMAP.md`   | Humano (nós)           | Hermes                      |
| `STATE.json`   | Bot (a cada 60s)       | Hermes                      |
| `ACTIONS.json` | Hermes (quando decide) | Bot (a cada 30s)            |
| `GUIA.md`      | Humano (nós)           | Referência completa do jogo |
| `PROGRESS.md`  | Bot (diário)           | Humano + Hermes             |

**Ter todos os Pokémon Shinys, ou no maior rank possível** (Ultra Raro, Legendary, Mythic), formando um time completo e forte.

### Estratégia Geral
1. Use o **melhor Pokémon atual** para caçar na **hunt mais difícil disponível** com **vantagem elemental**
2. Capture Pokémon durante as hunts — quando achar um **melhor que o atual**, troque o ativo
3. Guarde Pokémon bons no **Depot** para usar depois
4. Evolua SEMPRE que possível (nível + stones disponíveis)
5. O progresso é lento e baseado em **qualidade > velocidade**
6. 
**Objetivo final**: Ter todos os Pokémon no maior rank possível (Shiny, Mítico, Lendário), formando um time completo e forte.

**Como chegar lá**: 
- Use o melhor Pokémon que você tem para **caçar a hunt mais difícil disponível com vantagem elemental**
- No caminho, capture Pokémon melhores → troque o ativo → guarde os bons no Depot
- **Não force uma ordem fixa** (não precisa ser Squirtle → Geodude → Pikachu)
- O progresso é orgânico: capture algo bom, use-o, capture algo melhor, troque
- **Qualidade > Velocidade** — time forte > pressa

---

## 🧠 Estrutura de Decisão (aplicar a cada ciclo)

### 1. QUAL HUNT ESCOLHER?

```
1. Qual o nível do Pokémon ativo?
2. Quais hunts estão desbloqueadas? (nível ≤ Pokémon ativo, sem 🔒)
3. Dessas, quais têm type advantage? (consultar tabela no GUIA.md)
4. Escolha a de MAIOR nível entre as com vantagem
5. Se nenhuma com vantagem, escolha a de maior nível neutra
6. Se estiver perto de upar (ex: Lv 58 → Lv 60), considere esperar para desbloquear novas hunts
```

### 2. QUANDO TROCAR DE POKÉMON ATIVO?

```
1. Pokémon capturado tem CATEGORIA maior? → Trocar
2. Mesma categoria, mas POTENCIAL muito maior (+20)? → Trocar
3. É SHINY? → Priorizar (a menos que categoria muito inferior)
4. Mesma espécie mas stats melhores? → Trocar
5. Pokémon atual muito forte e sem substituto à altura? → Manter
```

### 3. O QUE FAZER COM CAPTURAS?

```
1. Melhor Pokémon do time → ATIVO (em campo)
2. Próximos melhores → PARTY (reserva, até 6 slots)
3. Pokémon bons de tipos diferentes → DEPOT (para usar depois)
4. Pokémon fracos (mesma espécie/abaixo) → VENDER
5. NUNCA vender: Shinys, Míticos, Lendários, Stones de evolução
```

### 4. EVOLUÇÃO

```
1. Pokémon tem nível suficiente E stones necessárias? → EVOLUIR (prioridade máxima)
2. Tem nível mas não tem stones? → Caçar numa hunt que contribua para a Linked Task que dá a stone
   - Leaf Stone: Grass chain #2-4 (Oddish → Bellsprout → Ivysaur)
   - Fire Stone: Fire chain #2-3 (Vulpix → Growlithe)
   - Water Stone: Water chain (diversas)
3. Bulbasaur Lv 20+ precisa de Leaf Stone → Grass chain
4. Charmander Lv 20+ precisa de 7 Fire Stones → Fire chain
```

### 5. LINKED TASKS

```
- São AUTOMÁTICAS e REPETÍVEIS — não precisa ativar
- Task 2 só libera após completar Task 1 (sequencial por tipo)
- Bônus: XP + Gold extra por kill
- Prioridade: completar as primeiras tasks de cada cadeia para destravar as seguintes
- Já completas: Grass #1 (Bulbasaur), Rock #1 (Geodude)
- Ativas agora: Grass #2 (Oddish), Rock #2 (Graveler), Water #1 (Shellder), várias outras
```

### 6. MANUTENÇÃO

```
- Ultra Balls: Manter 50-200. Se < 50, comprar.
- Vender loot: A cada ciclo
- Auto-sell: Ultra Raro+ (nunca Shiny)
- Lure: 1 enquanto single-target (Lv 1-50), 2-3 depois de F3 (Lv 50+)
- NUNCA vender Stones de evolução
```

---

## 📊 Fases (apenas como referência de nível, não obrigatórias)

| Fase | Nível Pokémon | Hunt Máxima | Habilidades |
|------|--------------|-------------|-------------|
| **Inicial** | 1-19 | Lv 1 (Fácil) | F1 |
| **Intermediária** | 20-39 | Lv 20 (Fácil) | F1 + F2 |
| **Média** | 40-59 | Lv 40 (Médio) | F1 + F2 |
| **Avançada** | 60-79 | Lv 60 (Médio) | F3 (AoE) desbloqueia Lv 50 |
| **Difícil** | 80-99 | Lv 80 (Difícil) | F3 + F4 (AoE Lv 80) |
| **Endgame** | 100 | Lv 100 (Difícil) | Todas as skills |

### Milestones importantes

| Nível | Desbloqueio |
|-------|------------|
| 20 | F2 + hunts Lv 20 |
| 40 | Hunts Médio (Lv 40) |
| 50 | **F3 (AoE)** — muda o jogo! Lure 2-3 |
| 60 | Hunts Lv 60 |
| 80 | F4 (AoE) + hunts Difícil |
| 100 | Tudo liberado |

---

## 🎯 Estado Atual (19h30 BRT)

```
🌿 Bulbasaur (Grass) Lv 42 — Comum Pot 50
🎯 Hunt: Seadra (Water Lv 40) — type advantage ✅
💰 185k gold · 🔵 210 Ultra Balls
📖 Dex 2/151 · 👤 Treinador Lv 1
```

### Decisões Imediatas

- ✅ Hunt Seadra Lv 40 é a melhor escolha agora (maior nível com vantagem)
- 🔄 Subir até Lv 50 para desbloquear F3 (AoE + Lure 2-3 = +XP)
- ⏳ Capturar algo melhor que o Bulbasaur Comum Pot 50
- ⏳ Conseguir Leaf Stones para Bulbasaur → Ivysaur
- ⏳ Se capturar um Pokémon de categoria maior, trocar o ativo
