programy=[4,6,0]
jezyki = ['python', 'javascript','c++']

for id in range( len(jezyki)):
    print("id: {0} {1}".format(id, jezyki[id]))
    print("W folderze jest {0} programow w jezyku {1}".format(programy[id],jezyki[id]))
