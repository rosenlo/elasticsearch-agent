#!/bin/bash

WORK_HOME="/opt/es-agent"
VENV_HOME="$WORK_HOME/.venv"


source $VENV_HOME/bin/activate

case $1 in
    start) $VENV_HOME/bin/python $WORK_HOME/es-agent start
        ;;
    stop) $VENV_HOME/bin/python $WORK_HOME/es-agent stop
        ;;
    restart) $VENV_HOME/bin/python $WORK_HOME/es-agent restart
        ;;
    *) $VENV_HOME/bin/python $WORK_HOME/es-agent
        ;;
esac
