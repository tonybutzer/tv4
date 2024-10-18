#! /bin/bash

# /data/miniconda3/envs/tv/bin/python

source /data/miniconda3/etc/profile.d/conda.sh \
	&& conda activate tv \
	&& conda env list \
	&& (cd /home/tony/opt/tv4/favorites; python3 cron_weekly_favorites.py)
