import k8s_exec
import s3_exec

def main():
    res = k8s_exec.exec_commands('loadlims', 'j2lab/minderadatatransfer:VD_Daily_0.2.1', '/java/datatransfer.sh lims 2022-12-16')
    print(res)
    f = open('/dags/mlops-pipeline-result/load_lims.txt','w')
    f.write(str(res))    
    f.close()

    f = open(snakemake.output[0],'w')
    f.write(str(res))
    f.close()
    #s3_exec.s3_save(snakemake.output[0], res)

if __name__ == '__main__':
    main()