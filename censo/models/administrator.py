from . import Region

class Administrator:
    '''Dummy class not mapped to database '''
    has_form = False
    
    @classmethod
    def hierarchical_child(self):
        return Region
        
    def referring_children(self):
        return Region.objects.all()
