#!/bin/bash

CWD=$(pwd)

sbatch  --time=7-0 --mem=10g -c6 --job-name=AC_tr --wrap "source /cs/labs/adiyoss/roysheffer/audiosetdl/activate; bash /cs/labs/adiyoss/roysheffer/audiosetdl/audiocaps/bash/collect_audiocaps_train.sh"
sbatch  --time=7-0 --mem=10g -c6 --job-name=AC_va --wrap "source /cs/labs/adiyoss/roysheffer/audiosetdl/activate; bash /cs/labs/adiyoss/roysheffer/audiosetdl/audiocaps/bash/collect_audiocaps_val.sh"
sbatch  --time=7-0 --mem=10g -c6 --job-name=AC_te --wrap "source /cs/labs/adiyoss/roysheffer/audiosetdl/activate; bash /cs/labs/adiyoss/roysheffer/audiosetdl/audiocaps/bash/collect_audiocaps_test.sh"
