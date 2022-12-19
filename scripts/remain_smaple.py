import k8s_exec
# import s3_exec
import os

ODATE=snakemake.config["odate"]

def main():    
    res = k8s_exec.exec_commands('remainsample', 'j2lab/lambda-py:v1.0.21', 'python3 mlops-de-sample.py')
    # print(res)
    # f = open('/dags/mlops-pipeline-result/remain_sample.txt','w')
    # f.write(snakemake.output[0] + "\n")
    # f.write(str(res))
    # f.close()

    print(snakemake.output[0])
    f = open(snakemake.output[0],'w')    
    #print("###", os.path.dirname(os.path.abspath(snakemake.output[0])))
    #print("###", os.path.dirname(os.path.abspath(f)))
    f.write(str(res))
    f.close()

if __name__ == '__main__':
    main()