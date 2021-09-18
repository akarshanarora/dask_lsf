"""Main module."""

from dask.distributed import client
from dask_jobqueue import LSFCluster

def setuplsfcluster(queue:str, project_id:str, memory:int, ncores:int, job_extra:str=None) -> LSFCluster:
    '''
    Helper function to create LSF Client using DASK module.

    Parameters
    ----------
    queue : str
        LSF Queue
    project_id : str
        Project ID. Gets passed to -P argument.
    memory : int
        Memory per core in GB.
    ncores : int
        Number of cores per LSF job.
    job_extra : str
        LSF String Override argument.Default -- '-R "select[mem >= memory*1000 ] rusage [mem=mem*1000]"']

    Returns
    -------
    cluster : LSFCluster
    '''

    # User config
    processes = ncores
    cores = ncores

    # Defaults
    ncpus = 1
    header_skip = ['-M']
    death_timeout = 300
    nanny = True
    walltime = '2:00'

    # Build LSF string
    lsfmem = str( memory*1000)
    lsf_mem_string = [f'-R "select[mem >= {lsfmem} ] rusage [mem={lsfmem}]"']
    if job_extra:
        job_extra = [job_extra]
    else:
        job_extra = [lsf_mem_string]

    # Create LSF Cluster
    memory = str(memory)+'GB'
    use_stdin = True
    cluster = LSFCluster(
                queue=queue, project=ptag, memory=memory,
                use_stdin=use_stdin, processes=processes, walltime=walltime,
                cores=cores, ncpus=ncpus, death_timeout=death_timeout, nanny=nanny,
                header_skip=header_skip, job_extra = job_extra
              )

    return cluster
