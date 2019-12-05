from textgenrnn import textgenrnn
t = textgenrnn('procesados/preproceso.hdf5')
t.generate(20, temperature=1.15)
