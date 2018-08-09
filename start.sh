#!/bin/sh
if [ -z "$1" ]
  then
    echo "ERROR: Need path for fasttext";
    exit 1;
fi
wget http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz;
tar xvf lastfm-dataset-1K.tar.gz;
python3 preprocess_dataset.py;
echo "Using FastText at $1";
$1 skipgram -input lastfm-dataset-1K/processed.txt -output songs-model;
#echo "Test:"
#echo "Songs Similar to: ";
#$1 nn songs-model.bin
