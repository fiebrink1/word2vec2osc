# word2vec2osc
# By Rebecca Fiebrink, 2018
# 
# Requires pythonosc and gensim libraries
# Install (just once) on command line with following commands:
#   easy_install -U gensim
#   pip install python-osc

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import osc_bundle_builder
from pythonosc import udp_client
import gensim.downloader as api

#send OSC messages to port 6448 on localhost
client = udp_client.SimpleUDPClient("127.0.0.1", 6448)

print("Sends 25 word2vec coordinates to Wekinator (or somewhere else) via OSC")
print("Sends to port 6448 with OSC message name /wek/inputs")
print("A message is sent for each word you enter below.")
print("Loading word model; please wait...")
wv_model = api.load("glove-twitter-25")  # download the model and return as object ready for use
print("Word model loaded!")

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