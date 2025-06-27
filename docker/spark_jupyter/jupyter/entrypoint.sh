#!/usr/bin/env bash
set -e

NOTEBOOK_DIR="/notebooks"
if [ -d "$NOTEBOOK_DIR" ]; then
  echo "🔧 Ajustando permissões de $NOTEBOOK_DIR para UID 1000..."
  chown -R 1000:100 "$NOTEBOOK_DIR"
fi

# Gera spark-defaults.conf a partir do template
if [ -f "$SPARK_HOME/conf/spark-defaults.conf.template" ]; then
  envsubst < "$SPARK_HOME/conf/spark-defaults.conf.template" \
           > "$SPARK_HOME/conf/spark-defaults.conf"
fi

# Troca para o usuário jovyan (UID 1000)
exec gosu ${NB_UID}:${NB_GID} "$@"