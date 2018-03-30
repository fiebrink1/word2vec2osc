# word2vec2osc
# By Rebecca Fiebrink, 2018
# 
# Requires pythonosc and gensim libraries
# Install (just once) on command line with following commands:
#   easy_install -U gensim
#   pip install python-osc

from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder
from pythonosc import udp_client
from gensim.models import Word2Vec
import gensim.downloader as api
import gensim


#send OSC messages to port 6448 on localhost
client = udp_client.SimpleUDPClient("127.0.0.1", 6448)

print("Sends 25 word2vec coordinates to Wekinator (or somewhere else) via OSC")
print("Sends to port 6448 with OSC message name /wek/inputs")
print("A message is sent for each word you enter below.")

# Download model if necessary:
print("Downloading model if necessary...")
model_location = api.load("glove-twitter-25", return_path=True)

#Load model into variable:
print("Loading model from ", model_location, "...")
wv_model = gensim.models.KeyedVectors.load_word2vec_format(model_location)

try :    
  while 1: # endless loop

        #keyboard prompt (or accept via stdin)
        new_word = input('Enter a word: ')

        try:
          #the word2vec coordinates
          v = wv_model.get_vector(new_word);

          #make the OSC message
          bundle = osc_bundle_builder.OscBundleBuilder(
            osc_bundle_builder.IMMEDIATELY)
          msg = osc_message_builder.OscMessageBuilder(address="/wek/inputs")
          for val in v:
              msg.add_arg(val, msg.ARG_TYPE_FLOAT)
          bundle.add_content(msg.build())

          #send the OSC message
          client.send(bundle.build())

        except KeyError:
          print("Ignoring: not a word")

except KeyboardInterrupt:
  print("Goodbye")