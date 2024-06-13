from pyomd import Notes
from pyomd.metadata import MetadataType
from pathlib import Path

class MetadataRenamer:
    def __init__(self, notes_or_path):
        """Initializes the MetadataRenamer with either a Notes object or a Path.

        Args:
            notes_or_path (Notes | Path): The Notes object or the Path object
                                          to the notes directory.
        """
        if isinstance(notes_or_path, Notes):
            self.notes = notes_or_path
        elif isinstance(notes_or_path, Path):
            self.notes = Notes(notes_or_path)
        else:
            raise ValueError("Input must be a Notes object or a Path")

    def rename_metadata_key(self, 
                            old_key: str, 
                            new_key: str, 
                            meta_type: MetadataType = MetadataType.DEFAULT,
                            apply: bool = False):
        """Renames a metadata key for all notes within the Notes object.

        Args:
            old_key (str): The metadata key to rename and from which the values 
                           will be retrieved.
            new_key (str): The new name for the new metadata key that will be
                           created and receive the values retrieved from the
                           older key to be renamed.
            meta_type (MetadataType): The type of metadata to rename, with default
                                      Check the original lib for more information.
            apply (bool): If True, the changes will be applied to the notes. If 
                          False, changes are staged but not saved until
                          `apply()` is called.
        """
        for note in self.notes.notes:
            if note.metadata.has(old_key, meta_type=meta_type):
                value = note.metadata.get(old_key, meta_type=meta_type)
                note.metadata.add(k=new_key, l=value, meta_type=meta_type)
                note.metadata.remove(old_key)
        
        if apply == True:
           self.apply()
    
    def apply(self):
        self.notes.update_content()
        self.notes.write()