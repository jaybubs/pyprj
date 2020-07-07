### Calibration

This script can be used to check whether your power meter is calibrated or just how off it is.

For best results, record your ride on a trainer/with a power meter that you know is definitely calibrated. Make sure to record the ride on a separate device to track the second power meter you're trying to assess. When your ride is done, unless your device directly allows you to export csv, you might want to use a converter or something like Golden Cheetah that allows for csv export.

The next step is to prepare the csvs for processing. Make sure both files have identical number of time points and that they start and end at the same time (This can be made easier with a helper column such as heart rate). By default the script will be looking for column header 'secs' for time and 'watts' for power.

At this point you're ready to go. Simply run _calibrateMe.py_ with the csv filenames as arguments, eg:
`python calibrateMe.py file1 file2`
