#!/usr/bin/env python3
"""Update PROGRESS.md from STATE.json and push to GitHub."""
import json
import sys
import os
import subprocess
from pathlib import Path

REPO_DIR = Path("/opt/data/pokedream-data")
STATE_FILE = Path("/opt/data/profiles/pokedreams/STATE.json")

def main():
    if not STATE_FILE.exists():
        print("STATE.json not found, skipping")
        return

    with open(STATE_FILE) as f:
        s = json.load(f)

    progress = f"""# 🎮 PokeDream — Progresso

> Atualizado em: {s['last_update']}

## 📊 Status Geral

| Indicador | Valor |
|-----------|-------|
| **Fase** | {s['phase']} — Capital Inicial |
| **Treinador** | Lv {s['trainer']['level']} ({s['trainer']['xp_percent']}% XP) |
| **Gold** | 💰 {s['gold']:,} |
| **Pokédex** | {s['dex']}/151 |
| **Party** | {s['party_count']}/6 |
| **Stamina** | {s['stamina_minutes']} min |
| **Bot Status** | {'✅ Rodando' if s['bot_status'] == 'running' else '❌ ' + s['bot_status']} |
| **Uptime** | {s['uptime_seconds'] // 60}m {s['uptime_seconds'] % 60}s |

## 🐉 Pokémon Ativo

| Atributo | Valor |
|----------|-------|
| **Nome** | {s['pokemon_active']['name']} |
| **Nível** | Lv {s['pokemon_active']['level']} ({s['pokemon_active']['xp_percent']}% XP) |
| **Tipo** | {s['pokemon_active']['type']} |
| **Raridade** | {s['pokemon_active']['rarity']} |
| **Potencial** | {s['pokemon_active']['potential']}/100 |
| **HP** | {s['pokemon_active']['hp']}/{s['pokemon_active']['hp_max']} |

## 🔫 Hunt & Balls

- **Caçada atual:** {s['current_hunt']}
- **Ultra Balls:** {s['ultra_balls']} | **Premier:** {s['premier_balls']} | **Poké:** {s['poke_balls']}

## ✅ Linked Tasks

- **Completas:** {s['linked_tasks_complete']}/{s['linked_tasks_total']}

## 🎯 Metas da Fase Atual

| Meta | Status |
|------|--------|
| 💰 Juntar 1.000+ gold | {'✅' if s['gold'] >= 1000 else '❌'} **{s['gold']:,} gold** |
| 🏀 Comprar 8+ Ultra Balls | {'✅' if s['ultra_balls'] >= 8 else '⏳'} **{s['ultra_balls']} Ultra Balls** |
| 🔥 Ativar Linked Task Fire #1 | ⏳ Pendente |

## ✨ Shinies

{'🚨 **SHINY DETECTADO!** 🚨' if s.get('shiny_alert') else 'Nenhum shiny detectado.'}

## ⚠️ Erros

{', '.join(s.get('errors', [])) if s.get('errors') else 'Nenhum erro.'}
"""

    progress_file = REPO_DIR / "PROGRESS.md"
    old_content = progress_file.read_text() if progress_file.exists() else ""

    if old_content == progress:
        print("No changes in progress, skipping commit")
        return

    progress_file.write_text(progress)
    print(f"PROGRESS.md updated: {len(progress)} bytes")

    # Git commit and push
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", "PROGRESS.md"], capture_output=True)
    result = subprocess.run(
        ["git", "commit", "-m", f"📊 sync: progress update {s['last_update']}"],
        capture_output=True, text=True
    )
    if result.returncode == 0 and "nothing to commit" not in result.stdout:
        push = subprocess.run(["git", "push"], capture_output=True, text=True)
        print(f"Push: {push.returncode} — {push.stdout.strip()[:100]}")
    else:
        print("Nothing new to commit")

if __name__ == "__main__":
    main()
