import re

from ..datasources import revision_metadata
from ..dependencies import depends_on

SECTION_COMMENT_RE = re.compile(r"\/\*([^\*]|\*[^\/])+\*\/")

@depends_on(revision_metadata)
def is_section_comment(revision_metadata):
    
    if revision_metadata.comment is not None:
        return SECTION_COMMENT_RE.match(revision_metadata.comment) is not None
    else:
        return False
