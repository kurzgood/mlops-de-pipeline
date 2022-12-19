import k8s_exec
# import s3_exec

ODATE=snakemake.config["odate"]

def main():
    res = k8s_exec.exec_commands('exportlims', 'j2lab/lambda-py:v1.0.21', 'python3 mlops-de-get-lims.py')
    # f = open('/dags/mlops-pipeline-result/export_lims.txt','w')
    # f.write(str(res))
    # f.close()
    # print(snakemake.output[0])
    f = open(snakemake.output[0],'w')
    f.write(str(res))
    f.close()
    print(res)
if __name__ == '__main__':
    main()