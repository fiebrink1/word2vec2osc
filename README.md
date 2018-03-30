# word2vec2osc
By Rebecca Fiebrink

This script sends word2vec data via OSC in a format compatible with Wekinator. 

Requires Python 3.x

You will have to install gensim and python-osc libraries if you don't already have them.

To run, type "python word2vec2osc.py" on command line, and run Wekinator with 25 inputs. After the word2vec data is loaded, type words on the command line. A word2vec vector will be sent for each word. To stop, type Ctrl+C. 

Enjoy!