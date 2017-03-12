##########
# Fixes:
#
# 1) Find ploidy for all chromosomes in the file, not just one that the user inputs
# 2) Make resizable bins, any fluctuation from normal can alert the user of CNV/ploidy change

import sys
import os
import time


def String_Parser(main_string, str_to_find):

    main_string_length = len(main_string)
    split_size         = len(str_to_find)
    index_list         = []

    i = 0

    while ( i + split_size ) <= main_string_length:

        main_string_split = main_string[ i : i+split_size ]

        if str_to_find in main_string_split:

            index_list.append( i )

        i += 1

    return index_list



def Parse_File( input_file, chr_name, start_pos, end_pos, ignore_cnv = 1 ):

    '''Looks at a specific location in a given .gff3-formatted text file for the CNV and/or ploidy data'''

    zero_count = 0
    data_list  = []

    for lines in input_file:

        lines_list = lines.split("\t")

        if len( line_list ) < 9: #Ignore the file header and other odd stuff
            continue

        if ( line_list[ 5 ] == "0.0" )  and ( ignore_cnv == 1 ): #Ignores sections that have no CNV data
            zero_count += 1
            continue

        if String_Parser( lines_list[0], chr_name ) != []:

            if ( int( lines_list[4] ) >= int( start_pos ) ) and \
               ( int( lines_list[3] ) <= int(  end_pos  ) ) :

                data_list.append( float( lines_list[5] ) )

    return data_list



def Grand_File_Parser( input_file, ignore_cnv = 1 ):

    '''Looks through all chromosomes in a given .gff3-formatted text file for the CNV and/or ploidy data'''

    zero_count      = 0
    chr_name_list   = [ "chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chrR" ]
    chr_ploidy_dict = { "chr1": [0, 0], "chr2": [0, 0], "chr3": [0, 0], "chr4": [0, 0], "chr5": [0, 0], "chr6": [0, 0], "chr7": [0, 0], "chrR": [0, 0] }

    for lines in input_file:

        line_list = lines.split() # Splits the line into a list on spaces

        if len( line_list ) < 9: #Ignore the file header and other odd stuff
            continue

        if ( line_list[ 5 ] == "0.0" )  and ( ignore_cnv == 1 ): #Ignores sections that have no CNV data, adds the number of 
            zero_count += 1 #can be added to "include" "missing data"
            continue

        i = 0 

        while ( i <= 7 ):

            if String_Parser( lines, chr_name_list[ i ] ) != []: #if the line contains information pertaining to the chromosome of choice
                
                chr_ploidy_dict[ chr_name_list[ i ] ][ 0 ] += float( line_list[ 5 ] ) #adds the current bin's cnv to the total
                chr_ploidy_dict[ chr_name_list[ i ] ][ 1 ] += 1                       #counts the number of bins

            i += 1 

    return chr_ploidy_dict # Format will be [ strain_name, chr_1_ploidy, chr_2_ploidy, ... , chrR_ploidy ] 



def Date_and_Time():

    time_list   = time.asctime( time.localtime( time.time() ) ).split()
    time_string = time_list[ 4 ] + "_" + time_list[ 1 ] + "_" + time_list[ 2 ] 

    return time_string



def Help_Message():

    print( "\n\nThis program is designed to give you an average CNV/ploidy from .gff3-formatted files from Ymap software.\n" \
           "There are two seperate options for obtaining average CNV/ploidies:\n\n" \
           "Specific average: this requires the file, chromosome name and base pair range the average is to be calculated from:\n" \
           "\t$ python3 ymap_mean_cnv.py input_file.gff3.txt chrR 867 5309\n\n"\
           "General average: requires that the ymap_mean_cnv.py file is placed in the same directory as all files that data is to be taken from:\n" \
           "\t$ python3 ymap_mean_cnv.py ")


def main():

    arg_list = []

    for arg in sys.argv:
        arg_list.append( arg )

    if ( "--Help" in arg_list ) or \
       ( "--help" in arg_list ) or \
       (  "-Help" in arg_list ) or \
       (  "-help" in arg_list ) or \
       (   "--H"  in arg_list ) or \
       (   "--h"  in arg_list ) or \
       (   "-H"   in arg_list ) or \
       (   "-h"   in arg_list ) :

        Help_Message()
        quit()

    if len( arg_list ) == 1 or ( len( arg_list ) == 2 ): # Average ploidy of everything


        if len( arg_list ) == 1:

            new_file_name = Date_and_Time() + ".csv"

        else: 

            new_file_name = arg_list[ 1 ]

        if new_file_name[ -4: ] != ".csv":

            new_file_name = new_file_name + ".csv"

        file_list     = os.listdir()
        chr_name_list = [ "chr1", "chr2", "chr3", "chr4", "chr5", "chr6", "chr7", "chrR" ]
        output_file   = open( new_file_name, "w" )

        print( "name, chr1, chr2, chr3, chr4, chr5, chr6, chr7, chrR", file = output_file )

        for files in file_list:

            file_string_list = files.split( "." )
            new_line         = file_string_list[ 1 ] + ", "

            if ( files[ -4: ] != ".txt" ):
                continue

            open_file      = open( files, "r" )
            indy_file_dict = Grand_File_Parser( open_file ) # Format will be [ strain_name, chr1_ploidy, ... , chrR_ploidy ] 

            i = 0 

            while ( i <= 7 ): #cycle through chromosomes in list and

                try: 

                    average_chr_ploidy = ( indy_file_dict[ chr_name_list[ i ] ][ 0 ] / indy_file_dict[ chr_name_list[ i ] ][ 1 ] )
                
                except ZeroDivisionError:

                    print( "ERROR: Incorrect format in file: ", files )
                    print( "\tSkipping this remaining data in this file." )
                    break

                new_line = new_line + str( round( average_chr_ploidy, 2 ) ) + ", "

                i += 1

            print( new_line[:-2], file = output_file ) # [:-2] clips off the ", " (comma delimiter) at the very end of the string


    elif len( arg_list ) == 5: # Takes average of a highly specified location

        try:

            input_file_name  = arg_list[ 1 ] 
            chromosome_name  = arg_list[ 2 ]
            start_pos        = arg_list[ 3 ]
            end_pos          = arg_list[ 4 ] 

        except IndexError: 

            print( "\nERROR: The command you've entered was not correct. Try the -help command.\n" )
            quit()

        input_file = open( input_file_name,  "r" )

        data_list  = Parse_File( input_file, chromosome_name, start_pos, end_pos )

        print( sum( data_list ) / len( data_list ) )


    else:

        print( "ERROR: There is something wrong with your command!" )
        Help_Message()
        quit()

    print( "Done!")

main()
