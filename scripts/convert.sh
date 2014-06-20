cat > original

python preprocess/three.py < original > arff.arff

java weka.classifiers.trees.J48 -T arff.arff -l models/j48_3.model -p 0 > tmp

grep ':' < tmp > tmp2

awk '{print $1, $2, $3, $4, $5}' < tmp2 > output

python scripts/results.py arff.arff output

rm original arff.arff tmp tmp2 output