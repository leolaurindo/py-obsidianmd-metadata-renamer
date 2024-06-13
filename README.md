# MetadataRenamer

`MetadataRenouncer` is a versatile Python tool designed to rename metadata keys within notes managed by the `py-obsidianmd` library. It receives either a `Path` object or the `Notes` object built inside the original `py-obsidianmd`.

This tool is a simple prototype developed to extend the functionality of an existing project, offering an easy way to rename metadata fields.

It was designed as a class because I wanted it to heritage the `Notes` methods.

I intent to add the possibility to produce the same outcome with a `Note` object.

## Prototype status

This project is a prototype. It is intended to showcase a potential feature for the `py-obsidianmd` library and it is part of my studies on Objected-Oriented Programming in python. As such, it may undergo significant changes based on tests and further development needs.

In the future, this can be refactored to be integrated in a pull request for the original library.

# Installation

To use MetadataRenamer, clone this repository and ensure you have the `py-obsidianmd` library installed. You can assure this by installing the `conda` environment or importing the `requirements.txt` with `pip`.

First, clone this repo:

```
git clone https://github.com/leolaurindo/py-obsidianmd-metadata-renamer.git
```

**- Option 1**

Create your python environment as you'd like and import the requirements with `pip`:

```
pip install -r requirements.txt
```

**- Option 2**

Import the whole python environment with `conda`:

```
conda env create -f environment.yml
```

**- Option 3**

Install the `py-obsidianmd` with `pip` and you are ready to use the `rename_metadata.py` module. Just assure you are using a compatible python version.

```
pip install py-obsidianmd`
```

# Usage

To use `MetadataRenamer`, you can import and instantiate it with either a `Path` object pointing to your notes directory or directly with a Notes object from the `py-obsidianmd` library.

```python
from pathlib import Path
from pyomd import Notes
from metadata_renamer import MetadataRenamer

# Initialize with a Path
path = Path('/path/to/your/notes')
renamer = MetadataRenamer(path)
```

Or

```python
notes = Notes(path)
renamer = MetadataRenamer(notes)
```

Then, adjust the parameters as you wish to stage the changes:
```python
renamer.rename_metadata_key(old_key='old_key',new_key='new_key', meta_type=MetadataType.DEFAULT)
```

You can then apply those changes with the `apply()` method or set as a parameter for `rename_metadata_key()`

```python
renamer.apply()
# OR

renamer.rename_metadata_key(old_key='old_key',new_key='new_key', meta_type=MetadataType.DEFAULT)
```

# Conclusion

This is a work in progress and it is part on my studies on OOP with python. Suggestion and criticism are welcomed.