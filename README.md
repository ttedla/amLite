================
amLite
===============

amLite is an amharic translitration program. You might find
it most useful for tasks involving mapping ascii key chars
into respective amharic chars. Typical usage often looks like this:

%python amLite.py 

It will ask you to input the ascii_inputFile(better to put it in the same dir)
After finishing it will ask you the Name of the output file to write into 

(Note if you put a space after outputFileName it will recoginise it as part of the file name)

There is a bug which needs fixing. As amLite takes random input texts and converts them to their Amharic letter representation, it does the tokenization of the input text using key length, that is longer keys are mapped first as a result of which creeps the bug.  
