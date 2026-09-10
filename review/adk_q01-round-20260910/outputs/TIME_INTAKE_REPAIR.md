# Prefreeze time intake repair

VMD extracted all coordinates but exposed physical_time as zero in every frame. Initial monotonic-time check failed before any case freeze. Read native XTC frame headers, validate magic/atom counts/byte layout at every frame, and crosscheck frame count and box against VMD plus time spacing with installed gmx check. No coordinate data or scientific thresholds changed. Open2253 frames0–450.4ns; closed1678 frames0–335.4ns; spacing0.2ns. Native header arrays preserved.
