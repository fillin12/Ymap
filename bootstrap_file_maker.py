
import random

line_template_list = ["chr1_C_albicans_SC5314","Ymap","CNV"]

new_file = open( "bootstrap.gff3.txt", "w" )

print( "##gff-version 3\n\n[CNV]\nglyph = xyplot\ngraph_type = histogram\nfgcolor = black\nbgcolor = black\nheight = 50\nmin_score = 0\nmax_score = 4\nlabel = 1\nbump = 0\nscale = none\nballoon hover = Estimated CNV is $description\nkey = bootstrap_file_maker.py\n\n", file = new_file)

bin_size = 4555 #ymap generates 4555bp size bins where data is stored
max_size = 1000 #The number of lines to be included in the file
count    = 1 

while count < max_size:

	gaussian_num = random.gauss(2,0.4)
	random_flt   = round( gaussian_num, 2 )
	
	if ( random_flt < 1.0 ) and ( random_flt != 0 ):
		continue

	bin_start = ( count * bin_size ) - bin_size + 1
	bin_end   = ( count * bin_size )

	print( line_template_list[0] + "\t" + \
		   line_template_list[1] + "\t" + \
		   line_template_list[2] + "\t" + \
		   str( bin_start  )     + "\t" + \
		   str( bin_end    )     + "\t" + \
		   str( random_flt )     + "\t" + \
		   "."                   + "\t" + \
		   "."                   + "\t" + \
		   "Note=" + str( random_flt ),   \
		   file = new_file                  )

	count += 1 

new_file.close()


