#! /home/rodrigo/yes/bin/python

import os, sys

os.environ['RAPHTORY_BUILD_SERVERS']="1"
os.environ['RAPHTORY_PARTITION_SERVERS']="1"
os.environ['RAPHTORY_BUILDERS_PER_SERVER']="1"
os.environ['RAPHTORY_PARTITIONS_PER_SERVER']="1"

os.environ["JAVA_OPTS"]="-XX:+UseShenandoahGC -XX:+UseStringDeduplication -Xms2G -Xmx2G -Xss128M"
