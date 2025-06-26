FROM jupyter/pyspark-notebook:latest

USER root

RUN apt-get update && apt-get install -y gettext-base wget && \
    pip install --no-cache-dir minio boto3

COPY spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf.template
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Remove CRLF se existir (arquivos criados no Windows)
RUN sed -i 's/\r$//' /usr/local/bin/entrypoint.sh && \
    sed -i 's/\r$//' $SPARK_HOME/conf/spark-defaults.conf.template && \
    chmod +x /usr/local/bin/entrypoint.sh && \
    chown -R ${NB_UID}:${NB_GID} $SPARK_HOME/conf && \
    chmod -R u+w $SPARK_HOME/conf

# Baixa dependências Hadoop/AWS
RUN wget -qO $SPARK_HOME/jars/hadoop-aws-3.3.4.jar \
      https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    wget -qO $SPARK_HOME/jars/aws-java-sdk-bundle-1.12.298.jar \
      https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.298/aws-java-sdk-bundle-1.12.298.jar

USER ${NB_UID}

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["start-notebook.sh", "--NotebookApp.token=''"]
