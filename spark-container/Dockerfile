FROM continuumio/miniconda3:4.7.10

ENV HADOOP_VERSION 2.8.5
ENV SPARK_VERSION 2.4.4
ENV AWS_JAVA_SDK 1.11.682

RUN conda install --yes openjdk==8.0.152

RUN apt update && \
    apt install -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt && \
    cd /opt && \
    curl http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz | \
        tar -zx && \
    ln -s hadoop-$HADOOP_VERSION hadoop && \
    echo Hadoop $HADOOP_VERSION installed in /opt

RUN mkdir -p /opt && \
    cd /opt && \
    curl http://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-without-hadoop.tgz | \
        tar -zx && \
    ln -s spark-$SPARK_VERSION-bin-without-hadoop spark && \
    echo Spark $SPARK_VERSION installed in /opt

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV LD_LIBRARY_PATH=$HADOOP_HOME/lib/native

RUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/$HADOOP_VERSION/hadoop-aws-$HADOOP_VERSION.jar -o /opt/spark/jars/hadoop-aws-$HADOOP_VERSION.jar
RUN curl https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.3/httpclient-4.5.3.jar -o /opt/spark/jars/httpclient-4.5.3.jar
RUN curl https://repo1.maven.org/maven2/joda-time/joda-time/2.9.9/joda-time-2.9.9.jar -o /opt/spark/jars/joda-time-2.9.9.jar

RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/$AWS_JAVA_SDK/aws-java-sdk-core-$AWS_JAVA_SDK.jar -o /opt/spark/jars/aws-java-sdk-core-$AWS_JAVA_SDK.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/$AWS_JAVA_SDK/aws-java-sdk-$AWS_JAVA_SDK.jar -o /opt/spark/jars/aws-java-sdk-$AWS_JAVA_SDK.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-kms/$AWS_JAVA_SDK/aws-java-sdk-kms-$AWS_JAVA_SDK.jar -o /opt/spark/jars/aws-java-sdk-kms-$AWS_JAVA_SDK.jar
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/$AWS_JAVA_SDK/aws-java-sdk-s3-$AWS_JAVA_SDK.jar -o /opt/spark/jars/aws-java-sdk-s3-$AWS_JAVA_SDK.jar

ADD spark-container/start-common.sh /
ADD spark-container/start-worker /
ADD spark-container/start-master /
ADD spark-container/core-site.xml /opt/spark/conf/core-site.xml
ADD spark-container/spark-defaults.conf /opt/spark/conf/spark-defaults.conf
ENV PATH $PATH:/opt/spark/bin
