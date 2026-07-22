# PokeDream - Guia do Jogo

> Jogo Idle de Pokémon via navegador — https://pokedream.com.br/

---

## 1. Categorias de Raridade (Potencial 0–100)

Os Pokémon são classificados em 6 categorias. Quanto maior a categoria/potencial, mais forte o Pokémon:

| Categoria | Descrição |
|-----------|-----------|
| **Comum** | Pokémon básico, mais fácil de capturar |
| **Incomum** | Um pouco mais raro e forte |
| **Raro** | Difícil de encontrar, stats elevados |
| **Ultra raro** | Muito raro, stats bem altos |
| **Legendary** | Lendário, extremamente raro e poderoso |
| **Mythic** | Mítico, o mais raro de todos |

> O potencial vai de **0 a 100** e multiplica os atributos base do Pokémon.

---

## 2. Pokémon Shiny ✨

Shiny é uma variante **rara** de qualquer Pokémon. Características:

- Segue as mesmas categorias acima (Comum até Mítico)
- **Dobra ATK, DEF e HP** em relação à versão normal
- Muito mais difícil de capturar
- Visual diferenciado

> No Bot, é possível configurar uma pokébola separada exclusiva para Shinies.

---

## 3. Calculadora de Força 🧮

Acessível pelo ícone 🧮 na barra de ações.

Permite comparar **Pokémon A vs Pokémon B**:

- **Alvo de referência**: Selvagem comum (defensor padrão)
- **Pokémon A**: Escolha espécie, nível, raridade, potencial, bônus de runa
- **Pokémon B**: Opcional para comparação lado a lado
- **Shiny**: Checkbox que dobra ATK/DEF/HP
- **Golpe**: Seleciona o ataque usado no cálculo

Resultados exibidos:
- Dano normal
- Dano crítico (15% de chance)
- Dano médio esperado
- Golpes até derrubar o alvo

> **Dica**: Use sempre **nível 1 como base** para comparar Pokémon de forma justa.

---

## 4. Evolução ✨

Para ver os requisitos de evolução:

1. Abra o menu **Pokémon** (ícone de lupa na barra de ações)
2. Passe o mouse sobre o botão **✨** ao lado do Pokémon desejado
3. O tooltip mostrará:
   - Qual Pokémon ele evolui
   - **Nível necessário**
   - **Stone necessária** (ex: Fire Stone, Water Stone, etc.) e quantidade

Exemplo verificado no jogo:
- **Charmander → Charmeleon**: Nível 20 + 7 Fire Stones

---

## 5. Gerenciamento de Party (Time)

A Party comporta até **6 Pokémon**. O Pokémon **em campo** (ativo) é quem luta nas hunts.

### Adicionar Pokémon à Party

1. Abra a **Mochila de Pokémon** (segundo botão "Pokémon" na barra de ações)
2. Clique no Pokémon desejado na lista da Mochila
3. Clique no botão **"Pôr na party"** que aparece
4. Pokémon vai para o time (até 6 slots)

### Trocar Pokémon Ativo (em campo)

1. Abra o menu **Pokémon** (primeiro botão "Pokémon" na barra — ícone de lupa)
2. Na lista da party, clique no Pokémon que quer ativar
3. O Pokémon selecionado vai para o campo e o anterior volta pra reserva

> **Dica**: O botão do Pokémon ativo fica com borda diferente e marcado como "em campo".

### Remover Pokémon da Party

1. No menu **Pokémon**, clique no **✕** ao lado do Pokémon
2. Ele volta para a Mochila, liberando o slot

### Reordenar Party

- Arraste os Pokémon na lista do menu Pokémon para reordenar
- A ordem define quem entra em campo se o ativo morrer

### Dica Estratégica

> Antes de trocar de hunt, sempre verifique qual Pokémon está **em campo**. Usar o tipo errado (ex: Fire vs Water) faz você tomar mais dano e matar mais devagar.

---

## 6. Hunts (Caçadas)

Menu **Hunts** — onde você caça Pokémon selvagens.

### Níveis de Dificuldade

| Dificuldade | Descrição |
|-------------|-----------|
| **Fácil** | Pokémon iniciais e básicos, nível baixo |
| **Médio** | Pokémon médios, nível intermediário |
| **Difícil** | Pokémon evoluídos, nível alto |
| **Avançado** | Endgame, nível máximo |

> Uma hunt só fica disponível quando seu **Pokémon ativo atinge o nível mínimo** dela. Ex: hunt Lv 20 requer Pokémon nível 20+.

### Rotação Automática

1. Adicione hunts à lista clicando no **+** de cada uma
2. Ligue a **Rotação automática** (botão "Ligada")
3. Defina **minutos por hunt** (ex: 60)
4. O jogo alterna entre as hunts em loop, voltando ao início

Filtros disponíveis:
- Todas / Fácil / Médio / Difícil / Avançado
- "Só onde posso entrar" (filtra por nível do Pokémon ativo)

### Skills e Evolução do Combate

Os Pokémon ganham novas skills ao subir de nível:

| Tecla | Desbloqueio | Tipo de Dano |
|-------|-------------|--------------|
| F1 | Nível inicial | **Single-target** |
| F2 | ~Nível 20 | **Single-target** |
| F3 | ~Nível 50 | **Dano em área (AoE)** |
| F4 | ~Nível 80 | **Dano em área (AoE)** |

### Estratégia de Lure por Fase

**Fase 1 — Nível 1 a ~50 (apenas single-target)**:
- Lure = **1** (ataca na hora, sem agrupar)
- Pokémon só tem F1/F2, não faz sentido juntar bando

**Fase 2 — Nível 50+ (skills AoE liberadas)**:
- Lure = **3 a 5**, dependendo do respawn da hunt
- Coloque as **magias de área SEMPRE no topo** da ordem de combo
- Ajuste o número de inimigos para não perder tempo andando demais
- Se o respawn for baixo, use lure menor (2-3) para não ficar esperando

> **Dica**: Observe a hunt rodando. Se o Pokémon fica muito tempo andando sem atacar, reduza o lure. Se mata tudo rápido e fica ocioso, aumente o lure.

---

## 7. Linked Tasks (Missões Encadeadas)

Menu **Linked Tasks** — missões sequenciais por tipo elemental. Total: **146 tasks** em 12 categorias.

### Funcionamento

- Tasks são liberadas em **ordem sequencial** por tipo
- Cada task tem um **alvo específico** (Pokémon a derrotar)
- Ao concluir, recebe a **recompensa principal** e a próxima task é liberada
- Tasks podem ser **repetidas infinitamente** com recompensa reduzida
- Botão "Ir para a hunt →" leva direto à caçada do alvo

### Estrutura de uma Task

| Campo | Descrição |
|-------|-----------|
| Nome | Título da missão |
| Descrição | Lore/flavor text |
| Alvo | Pokémon a derrotar |
| Progresso | Ex: 0/80 kills |
| Recompensa | Itens + Gold (💰) + XP (⭐) |
| Repetição | Recompensa reduzida ao refazer |

### Categorias por Tipo

| Tipo | Tasks |
|------|-------|
| Fire | 11 |
| Water | 28 |
| Grass | 12 |
| Electric | 8 |
| Bug | 12 |
| Fighting | 7 |
| Flying | 11 |
| Ground | 10 |
| Normal | 16 |
| Poison | 15 |
| Psychic | 7 |
| Rock | 9 |

### Exemplo: Cadeia Fire

Ordem sequencial verificada no jogo:

1. **Faíscas de Kanto** (Charmander ×80) → 💰3.000 + ⭐8.000 + 10 Poké Balls
2. **Raposas Ardentes** (Vulpix) → 💰5.000 + ⭐15.000 + Fire Stone ×1
3. **Patrulha Canina** (Growlithe) → 💰5.000 + ⭐15.000 + Fire Stone ×1
4. **Chama Crescente** (Charmeleon) → 💰1.740 + ⭐5.500
5. **Lava das Ilhas** (Ponyta) → 💰1.740 + ⭐5.500 + 5 Ultra Balls
6. **Lorde do Fogo** (Charizard) → 💰3.420 + ⭐10.900 + Fire Stone ×1
7. **Raposa Mística** (Ninetales) → 💰3.420 + ⭐10.900 + Fire Stone ×1
8. **Fera Lendária** (Arcanine) → 💰3.420 + ⭐10.900 + Fire Stone ×1
9. **Cavalgada Flamejante** (Rapidash) → 💰3.420 + ⭐10.900 + Fire Stone ×1
10. **Conclave do Fogo** (Magmar) → 💰3.420 + ⭐10.900 + Fire Stone ×2
11. **Chama Eterna** (Flareon) → 💰3.420 + ⭐10.900 + Fire Stone ×1

### Estratégia: Hunts + Linked Tasks

> **Ideal**: Combine a **rotação de Hunts** com as **Linked Tasks** do mesmo tipo. Enquanto farma XP/capturas na hunt, você progride nas tasks simultaneamente, ganhando Gold e XP extras como bônus.

---

## 8. Sistema de Bot / Automação

O jogo possui **bot nativo** (botão "Bot" na barra de ações) com 6 seções configuráveis.

---

### 7.1 Captura · Pokébolas

Bola usada pelo treinador em **selvagens comuns**.

| Bola | Catch Rate | Preço | Estratégia |
|------|-----------|-------|------------|
| **Poké Ball** | ×0.5 | 10 ◈ | **Fallback automático** — só usar se acabar Ultra |
| **Ultra Ball** | ×4 | 130 ◈ | **USAR SEMPRE** — se paga sozinha com a venda dos Pokémon |
| **Premier Ball** | ×4 + visual | 200 ◈ | **NUNCA em comuns** — reservar só para Shinies |

**Fallback automático**: Se a Ultra Ball acabar, o bot automaticamente usa Poké Ball do estoque. Não precisa marcar nada.

**Checkboxes**:
- `[ ] Só usar a bola preferida` — **DEIXAR DESMARCADO** para permitir fallback
- `[ ] Pausar captura de selvagens comuns` — só marcar se quiser farmar só XP

---

### 7.2 Captura de Shiny ✨ (Override)

Bola **exclusiva para Shinies**. Configuração separada que sobrescreve a bola normal quando um shiny aparece.

| Bola | Quando Usar |
|------|-------------|
| **Premier Ball** ×4 | ✅ **SEMPRE em Shinies** — o visual arco-íris combina, e o catch rate é o mesmo da Ultra |

- Se **nenhuma bola for selecionada** no override, o shiny usa a mesma bola preferida dos comuns
- `[ ] Pausar captura de shinies` — nunca marque isso!

---

### 7.3 Auto-Cura

Regras de quando usar poções automaticamente. Se múltiplas regras batem, vale a **mais crítica (menor %)**.

**Configuração recomendada**:

| Regra | HP ≤ | Poção |
|-------|------|-------|
| 1 | 60% | Small Potion (cura 14%, custa 5◈) |

- Ligar/desligar auto-cura: ✅ **LIGADO**
- **Apenas Small Potion é suficiente** — testado até Lv 83+ com lure 3-5
- A poção mais barata do jogo (5◈) segura o farm perfeitamente
- Não precisa de Great/Ultra/Ultimate Potion — gaste seu gold com Ultra Balls

> **Experiência real**: Contas Lv 83+ farmando com lure 3-5 usando **só Small Potion**. Nunca foi necessário upgrade de poção.

---

### 7.4 Auto-Revive

Usa Revive automaticamente quando o Pokémon desmaia (HP = 0).

- Ligar/desligar auto-revive: ✅ **LIGADO** (como segurança)
- Pokémon a reanimar: **"Sem preferência"** (padrão)
- ⚠️ Se ficar sem Revives (300 ◈ cada), o Pokémon fica caído e os selvagens batem em você

> **Experiência real**: Nunca precisou de Revive até Lv 83+. Se o farm está bem configurado (tipo certo contra hunt certa), o Pokémon não morre. Mantenha ligado apenas como rede de segurança.

---

### 7.5 Lure + Combo

Controla quantos inimigos o Pokémon junta antes de atacar.

| Lure | Comportamento |
|------|--------------|
| **1** | Ataca na hora — apenas o alvo mais próximo (sem lure) |
| **2–5** | Anda juntando o bando até bater N, depois para e dispara as magias |

**Estratégia por nível**:

| Fase | Nível | Lure |
|------|-------|------|
| Inicial | 1 ~ 50 | **1** (só single-target) |
| Intermediário | 50 ~ 80 | **2–3** (F3 AoE liberada) |
| Avançado | 80+ | **3–5** (F3+F4 AoE) |

**Checkbox "Terminar o bando antes de lurar de novo"**:
- `ON`: Termina de matar o bando atual, depois junta N novos — mais organizado
- `OFF` (padrão): Fica recompletando o bando até N enquanto mata — mais rápido, mas misturado

> **Dica prática**: Observe o respawn da hunt. Se o Pokémon anda muito sem atacar, **reduza o lure**. Se mata tudo instantaneamente, **aumente**.

---

### 7.6 Ordem das Magias (Combo)

Define a sequência em que as magias são usadas no combo do lure. Salvo **por espécie** de Pokémon.

**Regra de ouro**:
- **Magias de área (F3, F4) SEMPRE no topo** da lista (↑)
- Magias single-target (F1, F2) depois
- Magias fora da lista entram no final automaticamente

**Exemplo — Charmander Lv 80+**:

| Prioridade | Magia | Tipo |
|------------|-------|------|
| 1º ↑ | F4 — Área | AoE |
| 2º | F3 — Área | AoE |
| 3º | F1 — Fire Punch | Single |
| 4º ↓ | F2 — Ember | Single |

> Ao trocar de Pokémon ativo, reordene as magias especificamente para ele.

---

### 7.7 Resumo Rápido da Configuração Ideal

| Seção | Config |
|-------|--------|
| Captura | Ultra Ball selecionada, fallback desmarcado |
| Shiny | Premier Ball selecionada |
| Auto-cura | ≤60% Small Potion (só isso basta) |
| Auto-revive | Ligado, sem preferência |
| Lure | 1 (até Lv 50), 3+ (após AoE) |
| Ordem magias | AoE primeiro, single-target depois |

---

## 9. Stamina Offline

- A cada **3 horas online**, ganha **+1 hora** de farm offline
- Teto máximo: **6 horas**
- O progresso é salvo no servidor continuamente

---

## 10. Vantagens Elementais (Tabela de Tipos)

Usar o **tipo certo contra a hunt certa** faz toda diferença — Pokémon com vantagem elemental causam mais dano e sofrem menos.

### Tabela de Ataque (seu Pokémon → selvagem)

| Seu Tipo | Forte contra (×2) | Fraco contra (×½) | Imune (×0) |
|----------|--------------------|--------------------|------------|
| **Fire** | Grass, Ice, Bug, Steel | Fire, Water, Rock, Dragon | — |
| **Water** | Fire, Ground, Rock | Water, Grass, Dragon | — |
| **Grass** | Water, Ground, Rock | Fire, Grass, Poison, Flying, Bug, Steel | — |
| **Electric** | Water, Flying | Electric, Grass, Dragon | Ground |
| **Ice** | Grass, Ground, Flying, Dragon | Fire, Water, Ice, Steel | — |
| **Fighting** | Normal, Ice, Rock, Steel | Poison, Flying, Psychic, Bug, Fairy | Ghost |
| **Poison** | Grass, Fairy | Poison, Ground, Rock, Ghost | Steel |
| **Ground** | Fire, Electric, Poison, Rock, Steel | Grass, Bug | Flying |
| **Flying** | Grass, Fighting, Bug | Electric, Rock, Steel | — |
| **Psychic** | Fighting, Poison | Psychic, Steel | — |
| **Bug** | Grass, Psychic | Fire, Fighting, Poison, Flying, Ghost, Steel, Fairy | — |
| **Rock** | Fire, Ice, Flying, Bug | Fighting, Ground, Steel | — |
| **Ghost** | Psychic, Ghost | — | Normal |
| **Dragon** | Dragon | Steel | Fairy |
| **Steel** | Ice, Rock, Fairy | Fire, Water, Electric, Steel | — |
| **Fairy** | Fighting, Dragon | Fire, Poison, Steel | — |
| **Normal** | — | Rock, Steel | Ghost |

### Exemplos Práticos

| Hunt (Tipo) | Use Pokémon do Tipo |
|-------------|---------------------|
| Bulbasaur (Grass/Poison) | Fire, Flying, Psychic, Ice |
| Charmander (Fire) | Water, Ground, Rock |
| Squirtle (Water) | Grass, Electric |
| Pikachu (Electric) | Ground |
| Geodude (Rock/Ground) | Water, Grass, Fighting, Ground, Ice, Steel |
| Gastly (Ghost/Poison) | Ghost, Psychic, Ground |
| Dratini (Dragon) | Ice, Dragon, Fairy |
| Magnemite (Steel/Electric) | Fire, Fighting, Ground |
| Clefairy (Fairy) | Poison, Steel |

> **Dica**: Sempre cheque o tipo do Pokémon na hunt antes de ir. Levar vantagem elemental faz você matar mais rápido, sofrer menos dano, e farmar com mais eficiência.

---

## 11. Status da Conta

| Atributo | Valor Inicial |
|----------|---------------|
| Treinador | Lv 1, HP 400/400 |
| Pokémon Ativo | Charmander Lv 1 (Fire, Comum, Pot 50, Atk 58, Def 60, HP 185) |
| Gold | 0 |
| Pokédex | 1/151 |
| Party | 1/6 |

---

## 12. Depot (Armazém/Cofre)

O **Depot** é o cofre de Pokémon — um armazém separado da Mochila onde você guarda Pokémon valiosos que não quer vender por acidente.

### Características

- **Nada entra sozinho** — só o que você move manualmente da Mochila (ou compra no Market)
- Tem sistema de **cadeado (lock)** que protege contra venda acidental
- Para **vender um Pokémon do Depot**, é preciso movê-lo de volta para a Mochila primeiro
- A venda de Pokémon **só acontece na Mochila**

### Ordenação

| Critério | Uso |
|----------|-----|
| Valor | Ordena por preço de venda |
| Raridade | Comum → Mythic |
| Potencial | 0% → 100% |
| Nível | Menor → Maior |
| Espécie | Agrupa por nome |

### Estratégia de Uso

**Fluxo de trabalho por hunt**:

1. **Durante o farm** da hunt X: Os Pokémon capturados vão para a **Mochila**
2. A **Venda Automática** filtra/vende os fracos automaticamente
3. Entre as capturas que sobraram (Ultra Raro+), use a **Calculadora** para identificar o mais forte
4. **Guarde só o melhor** na Mochila, venda o resto manualmente

**Ao trocar de hunt** (ex: sair do Charmander e ir pro Bulbasaur):

1. Pegue o **melhor Pokémon da hunt anterior** que está na Mochila
2. **Mova para o Depot** (clicando nele e transferindo)
3. Assim a Mochila fica limpa para a nova hunt, sem risco de vender o Pokémon errado

**Ao retornar para uma hunt já farmada**:

1. **Verifique o Depot primeiro** — procure o Pokémon daquela espécie
2. Se já tiver um no Depot, use-o como **referência de comparação** na Calculadora
3. Só substitua o do Depot se o novo for **comprovadamente mais forte**

### Regra de Ouro do Depot

> **1 Pokémon de cada espécie no Depot** = sua coleção permanente. O restante é moeda de troca.

---

## 13. Farm de Gold (Dinheiro)

O Gold vem de **duas fontes principais**:

### Fonte 1: Drop de Itens (Baixo Lucro)

Pokémon derrotados dropam itens e Stones de evolução. Vá até a **Loja** > aba "Vender loot" para vender os itens acumulados.

### Fonte 2: Captura e Venda de Pokémon (Lucro Principal)

#### Pokébolas e Preços

| Bola | Preço | Catch Rate | Quando Usar |
|------|-------|------------|-------------|
| **Poké Ball** | 10 ◈ | ×0.5 | Nunca (obsoleta) |
| **Ultra Ball** | 130 ◈ | ×4 | **Sempre** (uso padrão) |
| **Premier Ball** | 200 ◈ | ×4 + efeito visual | **Apenas Shinies** |

> **Regra de ouro**: Ultra Ball **sempre se paga**. O valor de venda dos Pokémon capturados supera o custo de 130 ◈ por bola. Só é preciso um capital inicial para comprar o primeiro estoque, depois o sistema se retroalimenta.

> **Premier Ball**: Mesmo catch rate da Ultra, custa 70 ◈ a mais, diferença é **apenas visual** (aura arco-íris). Reserve para Shinies.

#### Loja — Preços de Suprimentos

| Item | Preço | Efeito |
|------|-------|--------|
| Poké Ball | 10 ◈ | Catch ×0.5 |
| Ultra Ball | 130 ◈ | Catch ×4 |
| Premier Ball | 200 ◈ | Catch ×4 + visual |
| Small Potion | 5 ◈ | Cura 14% HP |
| Great Potion | 10 ◈ | Cura 25% HP |
| Hyper Potion | 50 ◈ | Cura 23% HP |
| Ultra Potion | 20 ◈ | Cura 28% HP |
| Ultimate Potion | 100 ◈ | Cura 50% HP |
| Revive | 300 ◈ | Cura 100% (reanima) |

### Venda Automática de Pokémon

No menu **Mochila de Pokémon** (segundo botão Pokémon na barra) > **Venda automática**:

| Config | Valor Recomendado |
|--------|--------------------|
| **Nunca vender shiny** | ✅ MARCADO |
| **Essência pior que** | Ultra raro |
| **Potencial abaixo de** | ❌ DEIXAR DESMARCADO |

> **Resultado**: Apenas Pokémon **Ultra Raro, Legendary** e **Mythic** (além de todos os **Shinies**) permanecem na mochila. Todo o resto é vendido automaticamente no momento da captura.

### Regra de "Keep Best"

Quando estiver farmando uma espécie específica e já tiver múltiplos Lendários/Míticos dela:

1. Use a **Calculadora de Força** 🧮 para comparar no **mesmo nível**
2. Mantenha **apenas o mais forte** — venda o restante manualmente
3. Objetivo: ter sempre **1 Pokémon de cada espécie** na categoria mais forte possível

### Shiny vs Não-Shiny

- Um Shiny **Comum** pode ser mais forte que um **Legendary** normal da mesma espécie
- **Sempre use a calculadora** para decidir qual manter
- Shiny dobra ATK/DEF/HP, então um Shiny Ultra Raro pode superar um Mythic normal

### Estratégia Completa de Farm

1. Farm inicial com Poké Balls (já tem 250) para juntar capital
2. Compre **Ultra Balls** (130 ◈ cada)
3. Ative **Venda Automática**: Nunca vender shiny ✅ + Essência pior que Ultra Raro ✅
4. Deixe o bot rodando com rotação de hunts + linked tasks
5. Venda loot na Loja periodicamente
6. Apenas Ultra Raro+, Legendaries, Mythics e Shinies ficam na bag

---

## 14. Lista de Tipos Elementais

Fire, Water, Grass, Electric, Psychic, Fighting, Ground, Rock, Flying, Bug, Poison, Normal, Ghost, Ice, Dragon, Fairy, Steel

---

## 15. Atalhos Rápidos

| Tecla | Ação |
|-------|------|
| F1 | Golpe 1 (Fire Punch) |
| F2 | Golpe 2 (Ember - desbloqueia Lv 20) |

---

## 16. Roadmap de Progressão

Estratégia de evolução automática usando cadeia de vantagens elementais. Partindo do **Charmander (Fire Lv 1)**.

---

### Fase 1: Capital Inicial (Gold para Ultra Balls)

**Objetivo**: Juntar ~1.000 ◈ para comprar o primeiro estoque de Ultra Balls.

| # | Ação | Pokémon Ativo | Hunt Alvo | Por quê |
|---|------|---------------|-----------|---------|
| 1.1 | Farm inicial | Charmander (Fire) | **Bulbasaur/Oddish/Bellsprout** (Grass Lv 1) | Fire > Grass — dano máximo |
| 1.2 | Capturar com Poké Ball | — | — | Usar as 250 Poké Balls grátis iniciais |
| 1.3 | Vender loot/comuns | — | Loja > Vender loot | Acumular gold inicial |
| 1.4 | Ativar Linked Task Fire | Charmander | **Faíscas de Kanto** (Charmander ×80) | Recompensa: 10 Poké Balls + 3.000 ◈ + 8.000 XP |

> **Checkpoint**: ~1.000 ◈ → Comprar **8+ Ultra Balls** na Loja. Daqui pra frente, **nunca mais use Poké Ball**.

---

### Fase 2: Cadeia de Vantagens Elementais

Monte um time com cobertura de tipos, sempre usando o Pokémon com vantagem:

| # | Pokémon Ativo | Hunt Alvo | Elemento Obtido | Vantagem |
|---|---------------|-----------|-----------------|----------|
| 2.1 | Charmander (Fire) | Bulbasaur/Oddish | **Grass** | Fire > Grass |
| 2.2 | Bulbasaur/Oddish (Grass) | Squirtle/Poliwag | **Water** | Grass > Water |
| 2.3 | Squirtle/Poliwag (Water) | Geodude/Diglett | **Ground/Rock** | Water > Ground/Rock |
| 2.4 | Geodude (Ground) | Pikachu/Magnemite | **Electric** | Ground > Electric |
| 2.5 | Water/Ground | Growlithe/Vulpix | **Fire (melhor)** | Water/Ground > Fire |
| 2.6 | Qualquer | Machop/Mankey | **Fighting** | — (dano neutro) |
| 2.7 | Fighting | Rattata/Meowth | **Normal** | Fighting > Normal |

Lógica: **Use o Pokémon que você acabou de capturar para farmar o próximo da cadeia**. Cada novo tipo desbloqueia novas hunts com vantagem.

---

### Fase 3: Farm de Stones e Evoluções (Lv 20+)

**Objetivo**: Evoluir o Charmander → Charmeleon e todos os principais.

| # | Ação | Detalhe |
|---|------|---------|
| 3.1 | Subir Charmander ao Lv 20 | Farmar hunts Grass com ele |
| 3.2 | Completar Linked Tasks Fire | Raposas Ardentes (Vulpix) → Fire Stone ×1 |
| 3.3 | Repetir Patrulha Canina | Growlithe → Fire Stone ×1 (repetível) |
| 3.4 | Juntar 7 Fire Stones | Via linked tasks + drops |
| 3.5 | **Evoluir Charmander → Charmeleon** | ✨ no menu Pokémon |

Repetir a mesma lógica para outros Pokémon:
- Bulbasaur → Ivysaur (Leaf Stone)
- Squirtle → Wartortle (Water Stone)

---

### Fase 4: Era Single-Target (Lv 20–50)

**Config do Bot**: Lure = 1, Ultra Ball normal, Premier p/ shiny

| Prioridade | Ação |
|------------|------|
| 1 | Manter rotação de hunts com vantagem elemental |
| 2 | Avançar Linked Tasks por tipo (priorizar as que dão Stones) |
| 3 | Farmar gold para manter estoque de Ultra Balls |
| 4 | Substituir Pokémon por versões de raridade maior (Raro → Ultra Raro → Legendary) |
| 5 | Mover os melhores de cada espécie para o Depot |

> **Checkpoint**: 1 Pokémon forte de cada tipo no Depot. Charmeleon Lv 50+.

---

### Fase 5: Era AoE (Lv 50+)

**Mudança de estratégia**: F3 (AoE) desbloqueado.

| Config | Valor |
|--------|-------|
| Lure | 2–3 (testar conforme respawn) |
| Ordem magias | F3 (AoE) ↑ primeiro, F1/F2 depois |
| Hunt | Preferir hunts com respawn denso (muitos inimigos próximos) |

---

### Fase 6: Endgame (Lv 80+)

F4 (AoE) desbloqueado — **eficiência máxima**.

| Config | Valor |
|--------|-------|
| Lure | 3–5 |
| Ordem magias | F4 ↑, F3 ↑, F1, F2 |
| Objetivo | Coleção completa 151/151, todos Legendary/Mythic/Shiny |

---

### Resumo do Loop de Progressão

```
FARMAR COM VANTAGEM → CAPTURAR TIPO NOVO → USAR NOVO TIPO NA PRÓXIMA HUNT
     ↓                                                    ↓
  UPAR NÍVEL → COMPLETAR LINKED TASKS → JUNTAR STONES → EVOLUIR
     ↓                                                    ↓
  VENDER FRACOS (Venda Automática) → GUARDAR FORTES (Depot)
     ↓
  REPETIR COM LURE MAIOR (quando AoE liberar)
```

---

### Status Atual da Jornada

| Atributo | Estado |
|----------|--------|
| Treinador | Lv 1 |
| Pokémon Ativo | Charmander Lv 1 (Fire, Comum, Pot 50) |
| Gold | 0 ◈ |
| Dex | 1 / 151 |
| Depot | 0 Pokémon |
| Ultra Balls | 50 |
| Progresso Linked Tasks | 0 / 146 |

> **Próximo passo**: Fase 1 — Farmar Bulbasaur/Oddish com Charmander para fazer gold inicial.
