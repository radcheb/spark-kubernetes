#!/bin/sh
unset SPARK_MASTER_PORT
export PYTHONPATH="${PYTHONPATH}:/opt/spark/python/"
export SPARK_DIST_CLASSPATH=$(hadoop classpath)
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/hadoop/lib/native