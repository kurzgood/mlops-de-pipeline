from snakemake.remote.S3 import RemoteProvider as S3RemoteProvider

S3 = S3RemoteProvider()

rule all:
    input:
        S3.remote("mlops-pipeline-result/mart.txt")

rule load_mart:
    input:
        S3.remote("mlops-pipeline-result/fs.txt")
    output:
        S3.remote("mlops-pipeline-result/mart.txt")
    script:
        "scripts/load_mart.py"

rule load_fs:
    input:
        S3.remote("mlops-pipeline-result/lims.txt")
        S3.remote("mlops-pipeline-result/stamp_2.txt")
        S3.remote("mlops-pipeline-result/match_1.txt")
        S3.remote("mlops-pipeline-result/samples.txt")
    output:
        S3.remote("mlops-pipeline-result/fs.txt")
    script:
        "scripts/load_fs.py"

rule load_lims:
    input:
        S3.remote("mlops-lims-dump/2022-10-14/patient.csv")
        S3.remote("mlops-lims-dump/2022-10-14/rna_amplification_sample_list.csv")
    output:
        S3.remote("mlops-pipeline-result/lims.txt")
    script:
        "scripts/load_lims.py"

rule export_lims:
    output:
        S3.remote("mlops-lims-dump/2022-10-14/patient.csv")
        S3.remote("mlops-lims-dump/2022-10-14/rna_amplification_sample_list.csv")
    script:
        "scripts/export_lims.py"

rule load_stamp_2:
    input:
        S3.remote("mlops-odm-dump/2022-10-14/odm1.3_fullSTAMP2_ODM_Export.xml")
    output:
        S3.remote("mlops-pipeline-result/stamp_2.txt")
    script:
        "scripts/load_stamp_2.py"

rule load_match_1:
    input:
        S3.remote("mlops-odm-dump/2022-10-14/odm1.3_fullMATCH_ODM_Export.xml")
    output:
        S3.remote("mlops-pipeline-result/match_1.txt")
    script:
        "scripts/load_match_1.py"

rule sftp_odm:
    output:
        S3.remote("mlops-odm-dump/2022-10-14/odm1.3_fullSTAMP2_ODM_Export.xml")
        S3.remote("mlops-odm-dump/2022-10-14/odm1.3_fullMATCH_ODM_Export.xml")
    script:
        "scripts/sftp_odm.py"

rule load_samples:
    output:
        S3.remote("mlops-pipeline-result/samples.txt")
    script:
        "scripts/load_sample.py"
