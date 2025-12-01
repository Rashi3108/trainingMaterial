#!/bin/bash
echo "Disk Check Started at: $(date)" | tee -a disk.log
df -h | tee -a disk.log
echo "Completed at: $(date)" | tee -a disk.log