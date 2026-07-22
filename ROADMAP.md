# PokeDream — ROADMAP de Progressão

> Este arquivo é lido pelo Hermes Agent para decidir ações do bot.
> O bot escreve o estado atual em `STATE.json`.
> O Hermes lê `STATE.json` + este `ROADMAP.md` e escreve `ACTIONS.json` com comandos.

---

## Estrutura de Arquivos

| Arquivo        | Quem escreve           | Quem lê                     |
| -------------- | ---------------------- | --------------------------- |
| `ROADMAP.md`   | Humano (nós)           | Hermes                      |
| `STATE.json`   | Bot (a cada 60s)       | Hermes                      |
| `ACTIONS.json` | Hermes (quando decide) | Bot (a cada 30s)            |
| `GUIA.md`      | Humano (nós)           | Referência completa do jogo |
| `PROGRESS.md`  | Bot (diário)           | Humano + Hermes             |

---

## Fases de Progressão

### Fase 1 — Capital Inicial (Treinador Lv 1–10)
- **Pokémon ativo**: Charmander (Fire)
- **Hunt alvo**: Bulbasaur ou Oddish ou Bellsprout (Grass Lv 1)
- **Vantagem**: Fire > Grass (dano dobrado)
- **Bot config**:
  - Bola: Ultra Ball (assim que tiver gold)
  - Shiny: Premier Ball
  - Auto-cura: ON, ≤60% Small Potion
  - Auto-revive: ON
  - Lure: 1 (single-target only)
  - Venda auto: Ultra Raro+ (nunca vender shiny)
- **Metas**:
  - [ ] Juntar 1.000+ gold
  - [ ] Comprar 8+ Ultra Balls
  - [ ] Ativar Linked Task Fire #1 (Charmander ×80)
- **Próxima fase**: Quando Treinador Lv 10+ E Charmander Lv 20+ E 8+ Ultra Balls

### Fase 2 — Cadeia Elemental (Treinador Lv 10–20)
- **Pokémon ativo**: Trocar conforme vantagem (ver tabela)
- **Cadeia de hunts**:
  1. Charmander → Bulbasaur/Oddish (Grass) → capturar Gras
  2. Bulbasaur/Oddish → Squirtle/Poliwag (Water) → capturar Water
  3. Squirtle/Poliwag → Geodude/Diglett (Ground/Rock) → capturar Ground
  4. Geodude → Pikachu/Magnemite (Electric) → capturar Electric
- **Bot config**: Mesma da Fase 1, mas trocar Pokémon ativo conforme hunt
- **Metas**:
  - [ ] 1 Pokémon de cada tipo: Fire, Grass, Water, Ground, Electric
  - [ ] Completar Linked Tasks de cada tipo
  - [ ] Charmander Lv 20+ para evoluir
- **Próxima fase**: Quando Treinador Lv 20+ E 3+ tipos capturados

### Fase 3 — Evoluções e Stones (Treinador Lv 20–30)
- **Objetivo**: Evoluir Pokémon principais
- **Ações**:
  - Charmander Lv 20 → Charmeleon (precisa 7 Fire Stones)
  - Bulbasaur Lv 20+ → Ivysaur (precisa Leaf Stones)
  - Squirtle Lv 20+ → Wartortle (precisa Water Stones)
- **Hunts para Stones**:
  - Fire Stone: Linked Task "Raposas Ardentes" (Vulpix) + "Patrulha Canina" (Growlithe)
  - Leaf Stone: Linked Task Grass correspondente
  - Water Stone: Linked Task Water correspondente
- **Metas**:
  - [ ] 7 Fire Stones → Evoluir Charmander → Charmeleon
  - [ ] Leaf Stones → Evoluir Bulbasaur → Ivysaur
  - [ ] Water Stones → Evoluir Squirtle → Wartortle
- **Próxima fase**: Quando Charmander evoluído para Charmeleon E Lv 50+

### Fase 4 — Era Single-Target Avançada (Lv 30–50)
- **Bot config**:
  - Lure: 1 (sem AoE ainda)
  - Manter rotação de hunts com vantagem elemental
  - Avançar Linked Tasks por tipo (priorizar Stones)
  - Substituir Pokémon por raridade maior (Raro → Ultra Raro → Legendary)
- **Venda auto**: Ultra Raro+ (nunca vender shiny)
- **Depot**: Mover melhores de cada espécie para o Depot
- **Metas**:
  - [ ] 1 Pokémon forte de cada tipo no Depot
  - [ ] Charmeleon Lv 50+
  - [ ] Dex 20+
- **Próxima fase**: Quando Pokémon ativo Lv 50+ (F3 AoE desbloqueada)

### Fase 5 — Era AoE (Lv 50–80)
- **Mudança**: F3 (AoE) desbloqueada
- **Bot config**:
  - Lure: 2–3 (testar conforme respawn)
  - Ordem magias: F3 (AoE) primeiro, F1/F2 depois
  - Hunt: Preferir hunts com respawn denso
- **Metas**:
  - [ ] Dex 50+
  - [ ] Todos os tipos cobertos no Depot
  - [ ] Pokémon ativo Legendary ou Mythic
- **Próxima fase**: Quando Pokémon ativo Lv 80+ (F4 AoE desbloqueada)

### Fase 6 — Endgame (Lv 80+)
- **Bot config**:
  - Lure: 3–5
  - Ordem magias: F4 ↑, F3 ↑, F1, F2
  - Venda auto: Legendary+ (nunca vender shiny)
- **Metas**:
  - [ ] Dex 151/151
  - [ ] Todos Legendary/Mythic no Depot
  - [ ] Pelo menos 1 Shiny no Depot

---

## Regras de Decisão do Hermes

### Prioridades Gerais (sempre aplicar):
1. **Sempre evoluir quando possível** — Se Pokémon atingiu nível E tem stones → priorizar evolução imediatamente
2. **Manter vantagem elemental** — Nunca caçar sem type advantage
3. **Sempre manter 50+ Ultra Balls** — Se cair abaixo, comprar na próxima ação
4. **Vender loot periodicamente** — Manter gold fluindo (⚠️ NUNCA vender Stones de evolução)
5. **Venda de Pokémon** — Seguir ordem de raridade do GUIA (vender Comum, Incomum, Raro; manter Ultra Raro+ e Shinies)

### Verificar a cada ciclo (cron 30–60min):

1. **Estado do bot**: 
   - Se `STATE.json.last_update` > 5min atrás → ALERTAR no Slack (bot pode ter travado)
   - Se `STATE.json.bot_status` = "error" → ALERTAR e sugerir reinício

2. **Gold**:
   - Se gold < 200 E Ultra Balls < 5 → ALERTAR (precisa comprar mais)
   - Se gold > 1.000 E Ultra Balls < 20 → Sugerir comprar Ultra Balls na loja

3. **Ultra Balls**:
   - Se Ultra Balls = 0 → ALERTAR CRÍTICO (bot sem bolas não captura)
   - Se < 10 → Sugerir comprar mais

4. **HP do Pokémon**:
   - Se HP < 50% E auto-cura desligada → Verificar config do bot
   - Se HP = 0 E auto-revive desligado → ALERTAR CRÍTICO

5. **Level up**:
   - Se Pokémon subiu de nível → NOTIFICAR no Slack (milestone)
   - Se Treinador subiu de nível → NOTIFICAR no Slack
   - Se desbloqueou F3 ou F4 → NOTIFICAR e ajustar lure/magias

6. **Shiny capturado**:
   - Se `STATE.json.shiny_alert` = true → NOTIFICAR CRÍTICO no Slack

7. **Mudança de fase**:
   - Se atingiu condição de próxima fase → NOTIFICAR e atualizar `STATE.json.phase`
   - Aplicar nova configuração (lure, hunt, etc.)

8. **Evolução disponível**:
   - Se Pokémon atingiu nível E tem stones → NOTIFICAR e sugerir evolução

9. **Stamina offline**:
   - Se stamina > 4h acumulada → Sugerir usar modo offline

10. **Troca de hunt**:
    - SeLinked Task da hunt atual completa → Sugerir próxima hunt da cadeia
    - Se Pokémon atual sem vantagem contra hunt → Sugerir trocar Pokémon

---

## Tabela de Vantagens Elementais (Referência)

| Seu Tipo | Forte contra (×2) |
|----------|--------------------|
| Fire | Grass, Ice, Bug, Steel |
| Water | Fire, Ground, Rock |
| Grass | Water, Ground, Rock |
| Electric | Water, Flying |
| Ground | Fire, Electric, Poison, Rock, Steel |
| Fighting | Normal, Ice, Rock, Steel |
| Flying | Grass, Fighting, Bug |
| Psychic | Fighting, Poison |
| Ice | Grass, Ground, Flying, Dragon |
| Bug | Grass, Psychic |
| Rock | Fire, Ice, Flying, Bug |
| Ghost | Psychic, Ghost |
| Dragon | Dragon |
| Steel | Ice, Rock, Fairy |
| Fairy | Fighting, Dragon |
| Poison | Grass, Fairy |

---

## Configuração Padrão do Bot

| Seção | Config |
|-------|--------|
| Bola comum | Ultra Ball |
| Bola shiny | Premier Ball |
| Auto-cura | ON, ≤60% Small Potion |
| Auto-revive | ON, sem preferência |
| Venda auto | Nunca shiny ✅, Essência pior que Ultra Raro |
| Lure | 1 (Lv 1-50), 2-3 (Lv 50-80), 3-5 (Lv 80+) |
| Magias | AoE (F3/F4) primeiro, single-target depois |