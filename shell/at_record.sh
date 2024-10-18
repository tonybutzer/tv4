#! /bin/bash

# /data/miniconda3/envs/tv/bin/python

# sets the python environment
# calls titan_record.pl to babysit the recoding for the duration

echo at_record $1 >> /tmp/atlog.log

source /data/miniconda3/etc/profile.d/conda.sh \
	&& conda activate tv \
	&& conda env list \
	&& (cd /home/tony/opt/tv4/gui; python3 titan_record.py $1)
