import os,glob,pdb

stars='bafgkm'
classes=['v','iii']

s={}
for i_s in stars:
  for i_c in classes:
    f=open('dat/uk'+i_s+'5'+i_c+'.dat','r')
    w=[];s[i_s+i_c]=[]
    for line in f:
      if line[0]!='#':
	w.append(line.split()[0])
	s[i_s+i_c].append(line.split()[1])
    f.close()
      
f=open('NES_pickles.tsv','w')
f.write('w\t'+'\t'.join(sorted(s.keys()))+'\n')
for i in range(len(w)):
  line=w[i]+'\t'
  line+='\t'.join([s[obj][i] for obj in sorted(s.keys())])
  f.write(line+'\n')

f.close()
