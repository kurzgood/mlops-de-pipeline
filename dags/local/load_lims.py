import k8s_exec
import s3_exec
from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api

def main():

    config.load_kube_config()
    try:
        c = Configuration().get_default_copy()
    except AttributeError:
        c = Configuration()
        c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()
    res = k8s_exec.exec_commands('loadlims', 'j2lab/minderadatatransfer:VD_Daily_0.2.0', '/java/datatransfer.sh lims 2022-12-15', core_v1)
    print(res)
    s3_exec.s3_save('mlops-pipeline-result/lims.txt', res)

if __name__ == '__main__':
    main()