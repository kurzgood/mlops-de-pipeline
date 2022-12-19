import k8s_exec
import s3_exec

def main():    
    res = k8s_exec.exec_commands('sftpodm', 'j2lab/lambda-py:v1.0.21', 'python3 mlops-de-get-odm.py')
    print(res)
    f = open('/dags/mlops-pipeline-result/sftp_odm.txt','w')
    f.write(str(res))
    f.close()
    print(snakemake.output[0])
    f = open(snakemake.output[0],'w')
    f.write(str(res))
    f.close()

if __name__ == '__main__':
    main()