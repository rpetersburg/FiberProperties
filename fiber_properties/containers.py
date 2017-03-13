"""Containers.py was written by Ryan Petersburg for use with fiber
characterization on the EXtreme PREcision Spectrograph

The classes in this module are used as containers for information (similar to
dictionaries) in the ImageAnalysis class and ImageConcerversion functions.
These are used instead of dictionaries due to the simplicity of attribute
instantiation so that the information is ALWAYS either a value or NONE rather
than an empty slot in a dictionary.
"""
#=============================================================================#
#===== Metadata Containers ===================================================#
#=============================================================================#

class ImageInfo(object):
    """Container for an image's meta information"""
    def __init__(self):
        self.pixel_size = None
        self.camera = None
        self.magnification = None
        self.height = None
        self.width = None
        self.subframe_x = None
        self.subframe_y = None
        self.exp_time = None
        self.bit_depth = None
        self.date_time = None
        self.temp = None
        self.num_images = None
        self.folder = None
        self.test = None
        self.fnum = None

class AnalysisInfo(object):
    """Container for meta information about ImageAnalysis."""
    def __init__(self, kernel_size, threshold):
        self.kernel_size = kernel_size
        self.threshold = threshold

class Edges(object):
    """Container for the fiber image edges."""
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

class FiberInfo(object):
    """Container for information concerning the fiber grouped by method."""
    def __init__(self, info=None):
        if info == 'pixel':
            self.edge = Pixel()
            self.radius = Pixel()
            self.circle = Pixel()
            self.gaussian = Pixel()
            self.full = Pixel()
        elif info == 'value':
            self.edge = None
            self.radius = None
            self.circle = None
            self.gaussian = None
            self.full = None

class Pixel(object):
    """Container for the x and y position of a pixel."""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

#=============================================================================#
#===== Fiber Property Containers =============================================#
#=============================================================================#

class FRDInfo(object):
    """Container for FRD information

    Attributes
    ----------
    input_fnum : float or list(float)
        list of the given input focal ratios
    encircled_energy : list(float) or list(list(float))
        list of encircled energies for each input_fnum
    encircled_energy_fnum : list(float) or list(list(float))
        independent variable (output f/#) corresponding to each
        encircled energy
    energy_loss : float or list(float)
        energy loss for each input focal ratio
    output_fnum : float or list(float)
        calculated output focal ratio for each input focal ratio
    """
    def __init__(self):
        self.input_fnum = []
        self.output_fnum = []
        self.encircled_energy_fnum = []
        self.encircled_energy = []
        self.energy_loss = []

class ScramblingInfo(object):
    """Container for scrambling gain information

    Attributes
    ----------
    in_x : list(float)
        List of the input centroid x positions
    in_y : list(float)
        List of the input centroid y positions
    out_x : list(float)
        List of the output centroid x positions
    out_y : list(float)
        List of the output centroid y positions
    scrambling_gain : list(float)
        List of the calculated scrambling gains
    in_d : list(float)
        List of all possible permutations of input shift distances
    out_d : list(float)
        List of the resultant output centroid shifts due to in_d
    """
    def __init__(self):
        self.in_x = []
        self.in_y = []
        self.out_x = []
        self.out_y = []
        self.scrambling_gain = []
        self.in_d = []
        self.out_d = []