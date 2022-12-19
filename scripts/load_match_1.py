import k8s_exec
import s3_exec

def main():
    res = k8s_exec.exec_commands('loadmatch1', 'j2lab/minderadatatransfer:VD_Daily_0.2.1', '/java/datatransfer.sh odm 2022-12-16 odm1.3_fullMATCH_ODM_Export.xml MATCH-1')
    print(res)
    f = open('/dags/mlops-pipeline-result/load_match_1.txt','w')
    f.write(str(res))    
    f.close()

    f = open(snakemake.output[0],'w')
    f.write(str(res))
    f.close()

if __name__ == '__main__':
    main()