rule all:
    input:
        "mlops-pipeline-result/tmp/load_lims.txt",
        "mlops-pipeline-result/tmp/load_match_1.txt"
        "mlops-pipeline-result/tmp/load_sample.txt"        
        

rule load_lims:
    input:
        "mlops-pipeline-result/tmp/export_lims.txt"
    output:
        "mlops-pipeline-result/tmp/load_lims.txt"
    script:
        "scripts/load_lims.py"

rule export_lims:
    output:
        "mlops-pipeline-result/tmp/export_lims.txt"
    script:
        "scripts/export_lims.py"

rule load_match_1:
    input:
        "mlops-pipeline-result/tmp/sftp_odm.txt"
    output:
        "mlops-pipeline-result/tmp/load_match_1.txt"
    script:
        "scripts/load_match_1.py"

rule sftp_odm:
    output:
        "mlops-pipeline-result/tmp/sftp_odm.txt"
    script:
        "scripts/sftp_odm.py"

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