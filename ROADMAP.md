# PokeDream — ROADMAP de Progressão

> Este arquivo é lido pelo Hermes Agent para decidir ações do bot.
> Versão 2.0 — Baseada em níveis reais de hunts e estratégia de qualidade.

---

## 🎯 Objetivo Final

**Ter todos os Pokémon Shinys, ou no maior rank possível** (Ultra Raro, Legendary, Mythic), formando um time completo e forte.

### Estratégia Geral
1. Use o **melhor Pokémon atual** para caçar na **hunt mais difícil disponível** com **vantagem elemental**
2. Capture Pokémon durante as hunts — quando achar um **melhor que o atual**, troque o ativo
3. Guarde Pokémon bons no **Depot** para usar depois
4. Evolua SEMPRE que possível (nível + stones disponíveis)
5. O progresso é lento e baseado em **qualidade > velocidade**

---

## 📊 Sistema de Hunts (Referência Completa no GUIA.md)

### Regra de Acesso
- Pokémon ativo precisa ter **nível ≥ nível da hunt**
- Hunts 🔒 exigem **chave/item especial** para desbloquear (Lv 60+)

### Níveis por Dificuldade

| Dificuldade | Faixa de Nível | Acessível |
|-------------|---------------|-----------|
| Fácil | Lv 1–20 | Sempre |
| Médio | Lv 40–60 | Pokémon Lv 40+ |
| Difícil 🔒 | Lv 80–100 | Pokémon Lv 80+ + chave |

### Tomada de Decisão de Hunt (a cada ciclo)

1. **Qual o nível do Pokémon ativo?**
2. **Qual a hunt mais difícil disponível** (não 🔒) que dá **vantagem elemental**?
3. Se não houver vantagem, escolha a hunt mais difícil com dano neutro
4. Se estiver caçando um tipo específico para capturar (ex: Water), priorize a melhor hunt desse tipo no nível atual

### Tabela de Vantagem Elemental

| Seu Tipo | **Forte contra (×2)** | **Fraco contra (×½)** |
|----------|----------------------|----------------------|
| **Fire** | Grass, Ice, Bug, Steel | Fire, Water, Rock, Dragon |
| **Water** | Fire, Ground, Rock | Water, Grass, Dragon |
| **Grass** | Water, Ground, Rock | Fire, Grass, Poison, Flying, Bug, Steel |
| **Electric** | Water, Flying | Electric, Grass, Dragon (imune: Ground) |
| **Ground** | Fire, Electric, Poison, Rock, Steel | Grass, Bug (imune: Flying) |
| **Fighting** | Normal, Ice, Rock, Steel | Poison, Flying, Psychic, Bug, Fairy (imune: Ghost) |
| **Flying** | Grass, Fighting, Bug | Electric, Rock, Steel |
| **Psychic** | Fighting, Poison | Psychic, Steel (imune: Dark?) |
| **Ice** | Grass, Ground, Flying, Dragon | Fire, Water, Ice, Steel |
| **Bug** | Grass, Psychic | Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy |
| **Rock** | Fire, Ice, Flying, Bug | Fighting, Ground, Steel |
| **Ghost** | Psychic, Ghost | Dark? (imune: Normal) |
| **Dragon** | Dragon | Steel, Fairy |
| **Steel** | Ice, Rock, Fairy | Fire, Water, Electric, Steel |
| **Normal** | — | Rock, Steel (imune: Ghost) |
| **Poison** | Grass, Fairy | Poison, Ground, Rock, Ghost (imune: Steel) |
| **Fairy** | Fighting, Dragon | Fire, Poison, Steel |

---

## 🧭 Fases de Progressão

### ⚡ Fase 1 — Setup Inicial (Fácil Lv 1–20)

**Status:** Em andamento (Bulbasaur Lv 42 — pulou para Médio)

**O que fazer quando estiver aqui:**
- Pokémon ativo: Bulbasaur (Grass) — capturado do Charmander inicial
- Subir até Lv 40 para acessar hunts Médio
- Hunt recomendada: Water Lv 1 (Squirtle, Poliwag, etc.) com vantagem Grass > Water
- **Trocar para Médio** assim que Pokémon atingir Lv 40

**Metas:**
- [x] Capturar um Grass (Bulbasaur)
- [ ] Capturar um Water
- [ ] Pokémon ativo Lv 40+
- [ ] Treinador Lv 10+

---

### 🌊 Fase 2 — Médio (Lv 40–60)

**Status:** Atual (Bulbasaur Lv 42)

**Hunts disponíveis (Lv 40, sem 🔒):**

| Hunt | Tipo | Grass é... |
|------|------|-----------|
| **Seadra** ✅ | Water | Forte ✅ |
| **Seaking** ✅ | Water | Forte ✅ |
| **Marowak** ✅ | Ground | Forte ✅ |
| **Tangela** ⚖️ | Grass | Neutro |
| Fearow ⚖️ | Normal/Flying | Neutro |
| Haunter ❌ | Ghost/Poison | Fraco ❌ |
| Kadabra ⚖️ | Psychic | Neutro |
| Parasect ❌ | Bug/Grass | Fraco ❌ |
| Persian ⚖️ | Normal | Neutro |
| Primeape ⚖️ | Fighting | Neutro |

**Estratégia para esta fase:**
1. Priorizar **Seadra** (Water Lv 40) — vantagem Grass + capturar Water para o time
2. Alternativa: **Marowak** (Ground Lv 40) ou **Seaking** (Water Lv 40)
3. Subir até Lv 50 para desbloquear F3 (AoE)
4. Subir até Lv 60 para acessar Médio 🔒 ou Difícil

**Metas:**
- [ ] Capturar 1 Water de qualidade
- [ ] Pokémon ativo Lv 50 (F3 AoE)
- [ ] Pokémon ativo Lv 60
- [ ] Capturar 1 Ground (Geodude, Diglett, etc.)

---

### 🔥 Fase 3 — Médio/Difícil (Lv 60–80)

**Quando chegar aqui:**
- Lure: 2–3 (F3 AoE disponível)
- Priorizar captura dos tipos que faltam no time
- Desbloquear 🔒 hunts conforme conseguir chaves

**Metas:**
- [ ] 1 Pokémon forte de cada tipo elemental
- [ ] Pokémon ativo Lv 80 (F4 AoE)
- [ ] Dex 20+

---

### 💎 Fase 4 — Difícil (Lv 80–100)

**Quando chegar aqui:**
- Lure: 3–5
- F3 + F4 AoE disponíveis
- Caçar as hunts Difícil 🔒 para capturar Pokémon evoluídos

**Metas:**
- [ ] Dex 50+
- [ ] Pelo menos 1 Legendary ou Mythic
- [ ] Time completo de tipos

---

### 🏆 Fase 5 — Endgame (Lv 100)

- Hunt mais difícil disponível
- Focar em Shinys e Pokémon de alto potencial
- Completar Pokédex 151/151

---

## 📋 Tomada de Decisão Automática (a cada 30 min)

### 1. Verificar Estado do Bot
- STATE.json atualizado nos últimos 5 min? Se não, alertar.
- Bot status = running? Se não, restart_bot.
- Erros? Reportar.

### 2. Gerenciar Ultra Balls
- Se < 50: comprar até 200 (130 gold cada)
- Se gold insuficiente: alertar

### 3. Escolher a Hunt Ideal
- Baseado no **nível do Pokémon ativo** e **tipo do Pokémon ativo**:
  1. Liste todas as hunts com nível ≤ Pokémon ativo (não 🔒)
  2. Filtre por vantagem elemental (×2)
  3. Escolha a de **maior nível** entre as com vantagem
  4. Se nenhuma com vantagem, escolha a de maior nível com dano neutro
  5. Se estamos seguindo a cadeia elemental, priorize o tipo atual da cadeia

### 4. Gerenciar Vendas
- Auto-sell: Ultra Raro+ (nunca vender Shinys)
- Vender loot acumulado a cada ciclo
- **NUNCA vender Stones de evolução**

### 5. Verificar Evolução
- Se Pokémon atingiu nível para evoluir E tem stones → priorizar evolução
- Se não tem stones → mudar estratégia para conseguir (Linked Tasks ou hunt específica)

### 6. Estratégia de Troca de Pokémon
- Comparar por: **Categoria → Potencial → Shiny**
- Se capturou um Pokémon **de categoria maior** (ex: Ultra Raro > Raro) → trocar o ativo
- Se **mesma categoria** mas **potencial +20 maior** → trocar
- Se **Shiny** → sempre priorizar (a menos que categoria muito inferior)
- Se capturou um Pokémon **do tipo que falta no time** → guardar no Depot
- **Vender**: sempre o pior da mochila (menor categoria → menor potencial)

### 7. Linked Tasks (automáticas)
- **São automáticas**: não precisa ativar nada — basta caçar o alvo
- **Sequenciais**: Task 2 libera após Task 1 completa (ex: para fazer Oddish, precisa completar Bulbasaur)
- **Qualquer Pokémon pode caçar qualquer hunt** — mas o bônus da linked task só vale se a task estiver desbloqueada
- **Repetíveis**: depois de completar 1x, pode refazer para bônus menor
- **Bônus**: XP + Gold extra por kill do alvo
- **Estratégia**: Priorizar completar as primeiras tasks de cada cadeia para destravar as seguintes
- Completamos ✅ Grass #1 (Bulbasaur) e ✅ Rock #1 (Geodude) — então Grass #2 (Oddish) e Rock #2 (Graveler) estão ativas

---

## 📈 Metas de Curto Prazo

1. ✅ Bulbasaur Lv 42 — trocar para hunt **Seadra** (Water Lv 40)
2. 🔄 Subir Bulbasaur até Lv 50 (F3 AoE)
3. ⏳ Capturar Water de qualidade
4. ⏳ Conseguir Leaf Stones para evoluir Bulbasaur → Ivysaur
5. ⏳ Evoluir para Ivysaur
6. ⏳ Capturar Ground/Rock
7. ⏳ Capturar Electric
