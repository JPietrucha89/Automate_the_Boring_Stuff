import f_readDocx
import os
from pathlib import Path

# main
print(f_readDocx.getText(Path(os.getcwd(), 'working_with_Word', 'demo.docx')))
