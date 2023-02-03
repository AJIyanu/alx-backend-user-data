#!/usr/bin/env python3
"""Log oit files modules"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        patt = field + "=" + r".*?" + separator
        rep = field + "=" + redaction + separator
        message = (re.sub(patt, rep, message))
    return message
