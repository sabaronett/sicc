# Streaming Instability Code Comparison (SICC)

Project and source files related to the Streaming Instability Code Comparison ([SICC](https://www.ufos-project.eu/dust-gas-drag-instability-code-comparison)) led by [PFITS+](https://pfitsplus.github.io/) and the [UFOS Project](https://www.ufos-project.eu/).


## Directory structure

### Project files

Project-related files (e.g., Jupyter Notebooks to generate the manuscript figures) can be found in the [`/ipynb`](/tree/main/ipynb) directory.
To be consistent with the Streaming Instability Code Comparison Problem Set document (see Section 1.2), the subdirectories within are hierarchically organized by **model** (e.g., [`/unstratified`](/tree/main/ipynb/unstratified)), by **problem** (e.g., [`../BA`](/tree/main/ipynb/unstratified/BA)), then by **variation** (e.g., [`../../np1`](/tree/main/ipynb/unstratified)).


### Source files

Source and input files for some participating codes, as well as pseudo code for particular models (e.g., [`../unstratified/pseudo_code.py`](/tree/main/source_files/unstratified/pseudo_code.py)), can be found in the [`/source_files`](/tree/main/ipynb) directory.
To be consistent with the Streaming Instability Code Comparison Problem Set document (see Section 1.2), the subdirectories within are hierarchically organized by **model** (e.g., [`/unstratified`](/tree/main/ipynb/unstratified)), by **problem** (e.g., [`../BA`](/tree/main/ipynb/unstratified/BA)), by **variation** (e.g., [`../../np1`](/tree/main/ipynb/unstratified)), then by **code** (e.g., [`../../../Athena++`](/tree/main/ipynb/unstratified)).


### Tree view

```
/ipynb
  /[model]
    /[problem]
      /[figure notebooks]
/source_files
  /[model]
    /codes
      /[code]
        /[source files]
    /[problem]
      /[variation]
        /[code]
          /[input files]
    /pseudo_code.py
```
