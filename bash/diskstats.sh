mediaDataperc=$(/usr/bin/df -h | /usr/bin/grep /dev/sda1 | /usr/bin/awk '{print $5}')
/usr/bin/df -h | /usr/bin/grep /dev/sda1 | /usr/bin/awk '{print $5}' > data/mediaData_perc
/usr/bin/df -h | /usr/bin/grep /dev/sda1 | /usr/bin/awk '{print $4}' > data/mediaData_free
/usr/bin/rrdtool update data/mediaData.rrd N:${mediaDataperc%?}

mediaData2perc=$(/usr/bin/df -h | /usr/bin/grep /dev/sdc1 | /usr/bin/awk '{print $5}')
/usr/bin/df -h | /usr/bin/grep /dev/sdc1 | /usr/bin/awk '{print $5}' > data/mediaData2_perc
/usr/bin/df -h | /usr/bin/grep /dev/sdc1 | /usr/bin/awk '{print $4}' > data/mediaData2_free
/usr/bin/rrdtool update data/mediaData2.rrd N:${mediaData2perc%?}

mediaMultimediaperc=$(/usr/bin/df -h | /usr/bin/grep /dev/sdd1 | /usr/bin/awk '{print $5}')
/usr/bin/df -h | /usr/bin/grep /dev/sdd1 | /usr/bin/awk '{print $5}' > data/mediaMultimedia_perc
/usr/bin/df -h | /usr/bin/grep /dev/sdd1 | /usr/bin/awk '{print $4}' > data/mediaMultimedia_free
/usr/bin/rrdtool update data/mediaMultimedia.rrd N:${mediaMultimediaperc%?}
