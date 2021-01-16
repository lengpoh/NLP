from textgenrnn import textgenrnn


textgen2 = textgenrnn('textgenrnn_weights.hdf5')
## Depending on the version of python environment, you may get warning messages on deprecation of some utilities


print("\n\n")
print ("** for testing only")
textgen2.generate(1, prefix="My team mates uses Google")
print("\n\n")


