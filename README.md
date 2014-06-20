
### I have implemented a model for restoring capitalization and diacritics to plain Portuguese text.

My data comes from the March 31, 2014 Portuguese Wikipedia dump. I have included the original text and the preprocessed versions in **\data**.

I have included the Python preprocessing scripts in **\preprocess**. Each script reads from stdin and writes to stdout. These scripts depended on the *unidecode* module.

I have included my Weka models and output result buffers in **\models** and **\results** respectively.

I have included general purpose scripts in **\scripts**. Within this folder, **confusion.sh** can be used to turn Weka’s text-based confusion matrices into csv files to be used with Excel. **start.sh** adds the appropriate Weka sources to the user's CLASSPATH (the user will need to modify the WEKA_PATH variable in the script). Afterwards, a user can use **convert.sh** to restore capitalization and diacritics to a text or to see what would have been the classifier's predictions for a plain-text version. Input is provided through stdin and output will be printed to stdout. This pipeline uses the J48 N=3 classifier. This is neither an efficient pipeline nor is it robust, but it can be used to demonstrate the classifier's basics capabilities.

#### To run:
. scripts\start.sh
sh scripts\convert.sh < your_file_name


#### Diacritic Key For .arff Files

accent | lower | upper
------ | ----- | -----
none   | (0)   | (6)
`      | (1)   | (7)
´      | (2)   | (8)
^      | (3)   | (9)
~      | (4)   | (10)
ç      | (5)   | (11)


