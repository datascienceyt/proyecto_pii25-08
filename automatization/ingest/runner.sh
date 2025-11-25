#!/usr/bin/env bash
set -uo pipefail

fail=0
run() {
  name="$1"; shift
  echo "▶ $name"
  if "$@"; then
    echo "✔ $name OK"
  else
    echo "✖ $name FAILED"
    fail=1
  fi
}

# Usa python -u para logs en tiempo real
run "ingest_codigos"          python -u ingest_codigos.py
run "ingest_geojson"          python -u ingest_geojson.py
run "ingest_latinobarometro"  python -u ingest_latinobarometro.py
run "ingest_vdem"             python -u ingest_vdem.py
run "ingest_vivienda"         python -u ingest_vivienda.py
run "ingest_persona"          python -u ingest_persona.py

exit $fail
