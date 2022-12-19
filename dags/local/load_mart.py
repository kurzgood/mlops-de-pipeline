import k8s_exec
import s3_exec

def main():
    res = k8s_exec.exec_commands('load_mart', 'ls')
    s3_exec.s3_save(snakemake.output[0], res)

if __name__ == '__main__':
    main()