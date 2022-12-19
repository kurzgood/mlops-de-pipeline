import k8s_exec
#import s3_exec
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
    #schedule.sh mlops-de-get-lims.py
    res = k8s_exec.exec_commands('exportlims', 
                                'j2lab/lambda-py:v1.0.7', 
                                'python3 mlops-de-get-lims.py', 
                                core_v1)
    print(res)
if __name__ == '__main__':
    main()