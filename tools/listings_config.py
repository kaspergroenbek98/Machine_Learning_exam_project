# listings_config.py

"""
This script writes the preamble for listings configuration on LaTeX 
with the listings package. It will result in syntax-highlighting similar
to what is found on GitHub.com when reading python scripts.

Update the PATH variable with the absolute path of the file to read. Run the 
script, and preamble.txt will be created. Copy/paste the contents of the preamble.txt 
file into your LaTeX document preamble.
"""

PATH = '/Users/fh/Documents/GitHub/linear_algebra/tools/lin_alg_toolkit.py'

script_specific_identifiers = []
capital_identifiers = []

infile = open(PATH,'r')
for line in infile.readlines():
    tokens = line.split()
    if len(tokens) == 2 and tokens[0] == 'def':
        script_specific_identifiers.append(tokens[1].split('(')[0])
    elif len(tokens) >= 3 and tokens[1] == '=':
        if tokens[0][0].isupper():
            capital_identifiers.append(tokens[0])

out = []

out.append(r"\definecolor{codepurple}{rgb}{0.435,0.259,0.757}")
out.append(r"\definecolor{codeblue}{rgb}{0,0.361,0.773}")
out.append(r"\definecolor{codered}{rgb}{0.843,0.227,0.286}")
out.append(r"\definecolor{codeorange}{rgb}{0.89,0.384,0.035}")
out.append(r"\definecolor{codecomment}{rgb}{0.012,0.184,0.384}")
out.append(r"\definecolor{codecommentsingle}{rgb}{0.416,0.451,0.490}")
out.append("\n")

out.append(r"\lstdefinelanguage{fredcode}{")
out.append(r"    basicstyle=\ttfamily\footnotesize,")
out.append(r'    morecomment = [s][\color{codecomment}]{"""}{"""},')
out.append(r"    morecomment = [s][\color{codecomment}]{'}{'},")
out.append(r'    morecomment = [s][\color{codecomment}]{"}{"},')
out.append(r"    morecomment = [l][\color{codecommentsingle}]{\#},")
out.append(r"    keywordstyle = [2]{\color{codepurple}},")
out.append(r"    morekeywords = [2]{print,range,abs,len,append,open,list,map,split,readlines,sort,round},")
out.append(r"    keywordstyle = [3]{\color{codepurple}},")
out.append(r"    morekeywords = [3]{" + ','.join(script_specific_identifiers) + r'},')

out.append(r"    keywordstyle = [4]{\color{codered}},")
out.append(r"    morekeywords = [4]{from,import,def,class,for,while,return,if,elif,else,continue,and,or},")
out.append(r"    keywordstyle = [5]{\color{codeblue}},")
out.append(r"    morekeywords = [5]{in,not},")
out.append(r"    keywordstyle = [6]{\color{codeorange}},")
out.append(r"    morekeywords = [6]{" + ','.join(capital_identifiers) + r'},')

out.append(r"    alsoletter = {**,==,>=,<=,=,+,-,/,\%,*,*=,+=,-=,/,//,=,!=,0,1,2,3,4,5,6,7,8,9},")
out.append(r"    keywordstyle = [7]{\color{codeblue}},")
out.append(r"    morekeywords = [7]{**,==,=,+,-,/,\%,*,*=,+=,-=,/=,!=,0,1,2,3,4,5,6,7,8,9},")
out.append(r"    lineskip = 4pt")
out.append(r'}')

#print('\n'.join(out))

outfile = open('preamble.txt','w')
outfile.write('\n'.join(out))
outfile.close()
