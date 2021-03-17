#!/bin/bash

if java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 -no-listener Exp.g4; then
    # java -cp .:antlr-4.9.1-complete.jar compiler.py Exp*.java
    # python3 compiler.py <Tests/test-03-variables.exp >Test.j
    echo "OK"
else
    rm -f Exp*.py Exp.tokens
fi

