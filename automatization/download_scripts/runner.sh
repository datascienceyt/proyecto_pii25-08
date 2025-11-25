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
run "enemdu_descarga"          python -u enemdu_descarga.py
run "vdem_descarga"            python -u vdem_descarga.py
run "latinobarometro_descarga" python -u latinobarometro_descarga.py
run "limpieza_vdem"            python -u limpieza_vdem.py
run "limpieza_latinobarometro" python -u limpieza_latinobarometro.py
run "limpieza_persona"         python -u limpieza_persona.py
run "limpieza_vivienda"        python -u limpieza_vivienda.py

exit $fail
