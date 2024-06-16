# Setup

```pip install pytype```


# Generate type stubs

```pytype 1_Merging_stubs_back_into_code/before.py```

# Copy type annotations from a PEP484 stub file into python source.

```merge-pyi -i path/to/python/file.py path/to/stubs/file.pyi```