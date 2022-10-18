cd media/videos/1080p60
rm -f file_list.txt
for f in *.mp4 ; do echo file \'$f\' >> file_list.txt; done
ffmpeg -f concat -safe 0 -i file_list.txt -c copy ../../../final_cut.mp4