'''
*** ROSIE File Preparer v2.1
*** Author: Colin Welsh
*** Date Created: 14 June 2017
'''

def matchChain(line,chain):
    if line[21] == chain:
        return True
    else:
        return False

    
def writeRecChains(recChains,infile,outfile):
    for item in recChains:
        for line in infile:
            if line.startswith('ATOM') and matchChain(line,item):
                    outfile.write(line[:55])
                    outfile.write('\n')
        infile.seek(0)
    outfile.write('TER\n')


def writeBindChains(bindChain,infile,outfile):
    for line in infile:
        if line.startswith('ATOM') and matchChain(line,bindChain):
            outfile.write(line[:55])
            outfile.write('\n')
    infile.seek(0)
    outfile.write('TER\n')


def enterChains():
    numRecChains = int(input("Enter number of receptor chains: "))
    print('Enter chain names one at a time, sepearated by hitting "enter"')
    recChains = []
    for i in range(0,numRecChains,1):
        chainName = input('Enter chain name: ')
        recChains.append(chainName)
    return recChains


def main():
    filename = input("Enter filename to be prepared: ")
    infile = open(filename,'r')
    outfile = open("proteins.pdb",'w')
    multRecChains = input('Are there multiple receptor chains? (y/n) ')
    if multRecChains == 'y' or multRecChains == 'Y':
        recChains = enterChains()
        bindChain = input('Enter name of binding chain: ')
        writeRecChains(recChains,infile,outfile)
        writeBindChains(bindChain,infile,outfile) 
    else:
        for line in infile:
            if line.startswith('ATOM'):
                outfile.write(line[:55])
                outfile.write('\n')
            elif line.startswith('TER'):
                outfile.write(line[:3])
                outfile.write('\n')
            elif line.startswith('ENDMDL'):
                outfile.write('TER\n')
    outfile.write('END')
    infile.close()
    outfile.close()

main()
