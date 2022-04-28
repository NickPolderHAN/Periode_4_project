import Extract_excel_data
import Blast_script

if __name__ == '__main__':
    excel_data_dictionary = Extract_excel_data.main()
    Blast_script.main(excel_data_dictionary)