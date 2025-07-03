#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
   """Run the StockPicker crew"""

   input   = {
      'sector' : 'technology'
   }

   result = StockPicker().crew().kickoff(inputs=input)  
   print("Final Result:______________")
   print(result.raw)

if __name__ == "__main__":
   run()