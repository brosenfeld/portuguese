#! /bin/bash
# Path to weka
WEKA_PATH=/Applications/weka-3-6-10
# add mysql-connector (manually copied to weka path) and weka to classpath
export CLASSPATH="$CLASSPATH:/usr/share/java/:$WEKA_PATH/mysql-connector-java-5.0.5-bin.jar:$WEKA_PATH/weka.jar"
# use the connector of debian package libmysql-java
# CP="$CLASSPATH:/usr/share/java/:$WEKA_PATH/weka.jar"
# start Explorer