# song-similarity

This is an implementation of [Using Word2vec for Music Recommendations](https://towardsdatascience.com/using-word2vec-for-music-recommendations-bb9649ac2484).

We use fastText and the [LastFm DataSet](http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-1K.tar.gz).

## Steps
Make sure you have fastText installed.
* Clone the repo.
* Run start.sh fasttext-dir/fasttext

You will get <strong>songs-model.bin</strong> when the training finishes.
Use it to predict nearest neigbors.

`fasttext nn songs-model.bin`
