import pandas as pd
import rich

import year_proc
import sunrisedata as sd






def forms_string(string1, string2, length_string=None, fill_char=' '):
    if length_string is None or length_string < (len(string1)+len(string2)):
        length_string = len(string1)+len(string2)
    num_fill_char = length_string - (len(string1)+len(string2))
    fill_str = fill_char * num_fill_char
    return string1 + fill_str + string2



if __name__ == '__main__':
    
    day = 20
    month = 2
    print()
    print(forms_string('first string', '11.11.11', 28, '.'))
    print(forms_string('first string', '22.22', 28, '.'))
    print(forms_string('first string', '11', 28, '.'))
    print(forms_string('first string', 'new string', 28, '.'))
    



