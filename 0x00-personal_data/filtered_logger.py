#!/usr/bin/env python3
"""Log oit files modules"""

from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("ssn", "password", "ip", "phone", "user_agent")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        patt = field + "=" + r".*?" + separator
        rep = field + "=" + redaction + separator
        message = (re.sub(patt, rep, message))
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initializes the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """log me in that format"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return logging.Formatter(self.FORMAT).format(record)


def get_logger() -> logging.Logger:
    """takes nothing returns logging.Logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    logger.format(formatter)
    return logging


def get_db() -> mysql.connector.connection.MySQLConnection:
    """refurns a database"""
    config = {
              'user': os.getenv('PERSONAL_DATA_DB_USERNAME'),
              'password': os.getenv('PERSONAL_DATA_DB_PASSWORD')
              'host': os.getenv('PERSONAL_DATA_DB_HOST'),
              'database': os.getenv('PERSONAL_DATA_DB_NAME')
              }
    db = mysql.connector.connect(**config)
    return db
