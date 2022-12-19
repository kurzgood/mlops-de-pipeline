rule all:
    input:      
        "mlops-pipeline-result/tmp/load_sample.txt"        

rule load_sample:
    input:
        "mlops-pipeline-result/tmp/remain_sample.txt"
    output:
        "mlops-pipeline-result/tmp/load_sample.txt"
    script:
        "scripts/load_sample.py"

rule export_sample:
    output:
        "mlops-pipeline-result/tmp/remain_sample.txt"
    script:
        "scripts/remain_sample.py"