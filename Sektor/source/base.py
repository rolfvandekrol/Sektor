
class BaseSource:
    def get_base_tree(self):
        return Tree(self, '')


class Node:
    """Base class for Tree and Node.
    """
    def __init__(self, source, path):
        self.source, self.path = source, path

class Tree(Node):
    """Abstracts directories out of the source to make them easily accessible.
    
    This class provides a simple interface for directories from the source. It
    is not very much more than a set of methods that call the source object to 
    get its information. These methods allow you to use the Tree object as if it
    is a dictionary.
    """
    def _get_dict(self):
        return self.source.get_tree_items(self.path)
    
    def items(self):
        return self._get_dict().items()
    def iteritems(self):
        return self._get_dict().iteritems()
    def __getitem__(self, key):
        return self._get_dict()[key]
    def __iter__(self):
        return self._get_dict().iterkeys()
    def __contains___(self, key):
        return key in self._get_dict()
    

class File(Node):
    """Abstracts files out of the source to make the easily accessible.
    
    This class provides a simple interface for files from the source. It is not
    very much more than a set of methods that call the source object to get its
    information.
    """
    def get_data(self):
        return self.source.get_file_data(path)
    
    def __unicode__(self):
        return self.get_data()
    def __str__(self):
        return str(unicode(self))
    def __len__(self):
        return len(unicode(self))
    
    def __repr__(self):
        return 'Sektor.base.File(' + repr(self.source) + ', ' + repr(self.path) + ')'
