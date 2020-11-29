# recipe-allocator
**Script that takes in:**
- a JSON file with default order totals split by vegetarian/ gourmet, the number of recipes and the number of portions 
- a JSON file with defaults stock positions for each recipe.

This script allocates stocks to the various order types (per `box_type` (vegetarian/ gourmet), `recipe_number` (two, three or four recipes), and `portion_number` (two or four portions), whilst
ensuring the following constraints are met:
1. Vegetarian orders will only receive vegetarian boxes, whilst gourmet boxes can receive either vegetarian or gourmet
2. All orders must have unique recipes (no duplicated recipes within 1 order)

Script returns:
1. True if all constraints are met, False otherwise 
2. a JSON output file of how the stocks have been allocated.


# How to set up the project
1. This project uses pyenv-virtualenv to manage python environments. More information in this github repo: https://github.com/pyenv/pyenv-virtualenv.
2. Once you have pyenv-virtuaenv installed, run the command `make pyenv` to setup the virtual environment.
3. Alternatively (*at your own risk*), you could install the following dependencies manually:
    ```
    pytest==6.1.2
    word2number==1.1
    num2word==1.0.1
    ```
    
# How to run the script
```
python run.py --orders $orders --stocks $stocks
```
- Add input files to the directory `bin\inputs` (see examples)
- `$orders` and $stocks refer to the `orders` and `stocks` input JSON file you wish to read (without the `.json` extension)
- script outputs stock allocations to `bin\outputs` folder with the name $orders_$stocks.json

# Project Organisation
⮑ bin/inputs : where input file goes   
⮑ bin/outputs: where output file goes   
⮑ bin/test_files: where test files for unit testing goes       
⮑ definitions: where global variables are declared   
⮑ src: where the main source code codes   
⮑ recipe_allocator.py: algorithm for recipe allocation   
⮑ constraints_checker.py: checking all constraints are met    
⮑ run.py: run file that takes in 2 inputs: $orders and $stocks   
