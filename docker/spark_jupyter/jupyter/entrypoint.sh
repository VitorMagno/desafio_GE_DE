#!/usr/bin/env bash
set -e
if [ -f "$SPARK_HOME/conf/spark-defaults.conf.template" ]; then
  envsubst < "$SPARK_HOME/conf/spark-defaults.conf.template" \
           > "$SPARK_HOME/conf/spark-defaults.conf"
fi
exec "$@"
