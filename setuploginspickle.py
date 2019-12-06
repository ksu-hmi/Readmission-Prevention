import pickle

logins = { 'atest': 'atest', 'btest': 'btest'}

filename = 'logins'
outfile = open(filename,'wb')

pickle.dump(logins,outfile)
outfile.close()