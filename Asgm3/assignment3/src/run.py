import sys
import os
import glob
import subprocess
import unittest
import shutil
import platform
from antlr4 import *

for path in ['./test/', './main/zcode/parser/', './main/zcode/utils/', './main/zcode/astgen/', './main/zcode/checker/', './main/zcode/codegen/']:
    sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = '../target'
GENERATE_DIR = 'main/zcode/parser'


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "../target",
                       "-no-listener", "-visitor", "main/zcode/parser/ZCode.g4"])

    elif argv[0] == 'clean':
        shutil.rmtree(TARGET_DIR)
        os.mkdir(TARGET_DIR)
        for root, dirs, files in os.walk("..", topdown=False):
            for name in dirs:
                if name[0] in ['.', '_']:
                    shutil.rmtree(os.path.join(root, name))
            for name in files:
                if name == '.DS_Store':
                    os.remove(os.path.join(root, name))

    elif argv[0] == 'gui':
        seperator = ';' if platform.system() == "Windows" else ":"
        process1 = subprocess.Popen(
            ["java", "-jar", ANTLR_JAR,
             "ZCode.g4", "-Dlanguage=Java"], cwd="{}/test/gui".format(os.getcwd()))
        process1.wait()

        process2 = subprocess.Popen(
            "javac -classpath {} ZCode*.java".format(ANTLR_JAR), cwd="{}/test/gui".format(os.getcwd()), shell=True)
        process2.wait()

        process3 = subprocess.run('java -cp ".{}{}" org.antlr.v4.gui.TestRig ZCode program -gui code.txt'.format(
            seperator, ANTLR_JAR), cwd="{}/test/gui".format(os.getcwd()), shell=True)

        for filename in glob.glob("./test/gui/ZCode*"):
            _, extname = os.path.splitext(filename)
            if extname == '.g4':
                continue
            os.remove(filename)

    elif argv[0] == 'test':
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", GENERATE_DIR,
                           "-no-listener", "-visitor", "main/zcode/parser/ZCode.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'LexerSuite':
            from LexerSuite import LexerSuite
            getAndTest(LexerSuite)
        elif argv[1] == 'ParserSuite':
            from ParserSuite import ParserSuite
            getAndTest(ParserSuite)
        elif argv[1] == 'ASTGenSuite':
            from ASTGenSuite import ASTGenSuite
            getAndTest(ASTGenSuite)
        elif argv[1] == 'CheckerSuite':
            from CheckerSuite import CheckerSuite
            getAndTest(CheckerSuite)
        elif argv[1] == 'CodeGenSuite':
            from CodeGenSuite import CheckCodeGenSuite
            getAndTest(CheckCodeGenSuite)
        else:
            printUsage()
    else:
        printUsage()


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")
    print("python3 run.py test CheckerSuite")
    print("python3 run.py test CodeGenSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
