import random

from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run


REPO_URL = 'https://github.com/hjwp/book-example.git'