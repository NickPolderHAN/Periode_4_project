import Extract_excel_data
import re
import Blast_script
import SQL_connector_script as Scc

if __name__ == '__main__':
    excel_data_dictionary = Extract_excel_data.main()
    # Blast_script.main(excel_data_dictionary)
    # Scc.main()
