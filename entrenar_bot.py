from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file('procesados/texto.txt', num_epochs=1)
t.save('procesados/preproceso.hdf5')