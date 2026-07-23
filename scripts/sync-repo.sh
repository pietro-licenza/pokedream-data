#!/bin/bash
# sync-repo.sh — Sincronização bidirecional GitHub ↔ REPO ↔ LIVE
# Executado pelo cron a cada 5 minutos
#
# Fluxo:
#   1. git pull (GitHub → REPO)
#   2. Copia .md do REPO → LIVE (estratégia do usuário)
#   3. Verifica se LIVE tem .md mais novos → copia pro REPO e push

REPO="/opt/data/pokedream-data"
LIVE="/opt/data/pokedreams-data"
LOG="$REPO/scripts/sync.log"

log() { echo "[$(date '+%H:%M:%S')] $1" >> "$LOG"; }

log "=== Sync iniciado ==="

cd "$REPO"

# ── 1. PULL: GitHub → REPO ──
log "git pull..."
git pull origin main -q 2>> "$LOG" || log "⚠️ pull teve aviso (normal)"

# ── 2. SYNC: REPO → LIVE (estratégia do usuário) ──
for f in ROADMAP.md GUIA.md SOUL.md README.md "📊 Visão Geral.md"; do
  if [ -f "$REPO/$f" ]; then
    tmpf="/tmp/sync_$$_$(echo "$f" | tr ' ' '_')"
    cp "$REPO/$f" "$tmpf" 2>/dev/null
    mv "$tmpf" "$LIVE/$f" 2>/dev/null
  fi
done

# Copiar scripts .py
if [ -d "$REPO/scripts" ]; then
  mkdir -p "$LIVE/scripts"
  for sf in "$REPO/scripts/"*.py; do
    if [ -f "$sf" ]; then
      sfn="$(basename "$sf")"
      tmpf="/tmp/sync_$$_$sfn"
      cp "$sf" "$tmpf" 2>/dev/null
      mv "$tmpf" "$LIVE/scripts/$sfn" 2>/dev/null
    fi
  done
fi

# Manter .gitignore
tmpf="/tmp/sync_$$_.gitignore"
cp "$REPO/.gitignore" "$tmpf" 2>/dev/null
mv "$tmpf" "$LIVE/.gitignore" 2>/dev/null

log "📥 REPO → LIVE OK"

# ── 3. PUSH: LIVE → REPO → GitHub ──
#    Arquivos que HERMES pode ter atualizado (STATUS.md, etc.)
PUSH_NEEDED=false
for f in STATUS.md; do
  if [ -f "$LIVE/$f" ]; then
    # Só copia se LIVE for diferente do REPO
    if ! cmp -s "$LIVE/$f" "$REPO/$f" 2>/dev/null; then
      tmpf="/tmp/sync_$$_$f"
      cp "$LIVE/$f" "$tmpf" 2>/dev/null
      mv "$tmpf" "$REPO/$f" 2>/dev/null
      git add "$REPO/$f" 2>/dev/null
      log "📤 $f alterado por Hermes → vai pro GitHub"
      PUSH_NEEDED=true
    fi
  fi
done

# Também verifica se os .md principais foram alterados por Hermes
for f in ROADMAP.md GUIA.md; do
  if ! cmp -s "$LIVE/$f" "$REPO/$f" 2>/dev/null; then
    tmpf="/tmp/sync_$$_$f"
    cp "$LIVE/$f" "$tmpf" 2>/dev/null
    mv "$tmpf" "$REPO/$f" 2>/dev/null
    git add "$REPO/$f" 2>/dev/null
    log "📤 $f alterado por Hermes → vai pro GitHub"
    PUSH_NEEDED=true
  fi
done

if [ "$PUSH_NEEDED" = true ]; then
  git commit -m "🤖 sync: Hermes atualizou arquivos $(date '+%H:%M')" -q 2>> "$LOG" || true
  git push origin main -q 2>> "$LOG" && log "✅ Push pro GitHub OK" || log "❌ Push falhou"
else
  log "📤 Nada novo pra push"
fi

log "✅ Sync completo"
exit 0
