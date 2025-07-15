"""
Data package for analytics app
Contains all content data for different languages
"""

from .HomeData import HOME_DATA
from .UploadData import UPLOAD_DATA
from .ZipUploadData import ZIP_UPLOAD_DATA
from .TextInputData import TEXT_INPUT_DATA
from .TutorialData import TUTORIAL_DATA
from .ResultsData import RESULTS_DATA
from .BaseData import BASE_DATA

__all__ = [
    'HOME_DATA',
    'UPLOAD_DATA', 
    'ZIP_UPLOAD_DATA',
    'TEXT_INPUT_DATA',
    'TUTORIAL_DATA',
    'get_results_data',
    'BASE_DATA'
]
