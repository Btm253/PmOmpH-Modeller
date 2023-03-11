from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='6ehd', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6ehdA', atom_files='6ehd.pdb')
aln.append(file='PmOmpH.ali', align_codes='PmOmpH')
aln.align2d(max_gap_length=50)
aln.write(file='PmOmpH-6ehdA.ali', alignment_format='PIR')
aln.write(file='PmOmpH-6ehdA.pap', alignment_format='PAP')
