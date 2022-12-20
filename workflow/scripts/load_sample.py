import k8s_exec
import s3_exec
import boto3
import os

ODATE=snakemake.config["odate"]

def main():
    os_aws_access_key_id = os.getenv("aws_access_key_id","AKIA4BQN736FKFAWLMOF")
    os_aws_secret_access_key = os.getenv("aws_secret_access_key","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")
    os_s3_region_name = os.getenv("s3_region_name","us-west-2")
    os_bucket_name = os.getenv("access_bucket_snakemake_name", "mlops-pipeline-result")

    file = 'not_exist_pipeline_'+ODATE+'.txt'

    bucket_file = "output_folders/" + file
    local_file = file

    #s3 connect
    try:        
        s3 = boto3.client(
            service_name = "s3",
            region_name = os_s3_region_name,
            aws_access_key_id = os_aws_access_key_id,
            aws_secret_access_key = os_aws_secret_access_key
        )
    except Exception as e:
        print(e)

    obj_list = s3.list_objects(Bucket=os_bucket_name)
    contents_list = obj_list['Contents']

    file_list=[]
    check_exist_file = False
    
    for content in contents_list:
        #print("content : %s" % content)
        key = content['Key']
        if key == bucket_file:
            check_exist_file = True
            break
        else:
            check_exist_file = False

    if check_exist_file == True:
        print("file exist, file download!!")
        s3.download_file(os_bucket_name, bucket_file, local_file)
    

    f = open(local_file, 'r')    
    line = f.readline()
    print("line",line)
    
    f.close()    
    
    cnt = 0
    dict_line = eval(line)
    result = ""
    for i in dict_line:
        batch = i['batch']
        sample = i['sample']
        res = k8s_exec.exec_commands('loadsample', 'j2lab/minderadatatransfer:VD_Daily_0.2.1', '/java/datatransfer.sh rnaseq ' + str(batch) + ' ' + str(sample))
        if "" == result:
            result = res
        else:
            result = result + res
        cnt = cnt + 1

    print(result)

    # f = open('/dags/mlops-pipeline-result/load_sample.txt','w')
    # f.write(snakemake.output[0] + "\n")
    # f.write(str(result))    
    # f.close()

    f = open(snakemake.output[0],'w')    
    #print("###", os.path.dirname(os.path.abspath(f)))
    f.write(str(result))
    f.close()
    s3.close()

if __name__ == '__main__':
    main()

