this is a quickly banged up code that lets you compare the power meter data of one, two, three times a lady or more xml files (tcx, fit, whatever, just make sure it's xml) - useful when calibrating power meters, or comparing performance over the same segment or whatever you want

however: please curate your xml files first, any editor of your choice will do, just make sure that you're comparing two xml tags only.
For example if you're building your x-axis out of 'time', make sure you only have <time> xml tags and not <laptime>.


For vim users on linux: this is as easy as opening up **a copy** (if you fuck up your original file don't come crying back to me) in vim and grepping for watts and time:
	:%!grep -i "<watts>\|<time>"

by default the x-axis is set to time, and y axis to watts, feel free to change it to whatever you want by editing powercompare.py

#how to use
launch powercompare.py with filenames as arguments:
	$ powercompare.py ramp.tcx ramptest.tcx

that's it

do whatever you want to the code
