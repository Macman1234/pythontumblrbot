from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '

def Parse(name, depth, file_name):
	db = Db(sqlite3.connect(name + '.db'), Sql())
	db.setup(depth)

	txt = codecs.open(file_name, 'r', 'utf-8').read()
	Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)

def Gen(name, count):
	db = Db(sqlite3.connect(name + '.db'), Sql())
	generator = Generator(name, db, Rnd())
	for i in range(0, count):
		return generator.generate(WORD_SEPARATOR)
