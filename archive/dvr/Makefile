
cat:
	cat Makefile

dirs:
	mkdir /home/tony/tempdata
	mkdir /home/tony/recordings

dvr:

	docker run -d --name dvr \
  	--restart=unless-stopped \
  	--network host \
  	-e DVRUI_PORT=8080 \
  	-e PUID=1000 \
  	-e PGID=1000 \
	-p 10080:10080\
  	-v /home/tony/tempdata:/dvrdata \
  	-v /home/tony/recordings:/dvrrec \
  	demonrik/hdhrdvr-docker
