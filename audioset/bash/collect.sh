#!/bin/bash

CWD=$(pwd)

sbatch  --time=7-0 --mem=10g -c6 --job-name=AS --wrap "source /cs/labs/adiyoss/roysheffer/audiosetdl/activate; bash /cs/labs/adiyoss/roysheffer/audiosetdl/audioset/bash/collect_audioset.sh"