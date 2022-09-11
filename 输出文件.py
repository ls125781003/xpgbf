import os 
from pathlib import Path  # pathlib is recommended

'''
The following switch allows the program runs locally and in the Agit environment without modifications.
'''
if 'CLOUD_PROVIDER' in os.environ and os.environ['CLOUD_PROVIDER'] == 'Agit':
    result_path = Path('/root/.agit')  # this is the storage path in the Agit environment
else:
    result_path = Path('.')  # this is the path when the program runs in other environments

outputFile = result_path / 'output.txt'
outputFile.write_text('Hello Agit storage!')