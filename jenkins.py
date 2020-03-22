import jenkins
from jenkinsapi.jenkins import Jenkins
import requests

requests.packages.urllib3.disable_warnings()

def login_to_jenkins(jserver, uname, password):
    #url = jenkins_url + pipeline + pr_details + reply_format + build_fields
    server = Jenkins(jserver, uname, password, timeout=40)

    return server

def get_jenkins_version(server):
    return server.version

def get_pipelines(server):
    pipelines = server.keys()
    return pipelines

    print(jobName)

def get_jobs_list(server):
     def get_jobs_list(self):
        return self.jobs.keys()


username='7000019067'
token='aea354330c7f431abddd742120aa552851dbbd6b'
jenkins_url= 'https://cyborg-sf-private.jenkins.tools.ce.playstation.net'
Cyborg = "/view/Cyborg/job/"
ppr_pipeline = "psctrlppr-tests-on-PR"
reply_format='/api/json'
pr_url = "https://cyborg-sf-private.jenkins.tools.ce.playstation.net/view/Cyborg/job/psctrlppr-tests-on-PR/job/PR-165/"
def main():
    pipeline = '/view/Cyborg/job/psctrlppr-tests-on-PR/view/change-requests/job/'
    build_fields='?tree=builds[number,status,timestamp,id,result]'

    jurl = jenkins_url + Cyborg + ppr_pipeline

    server = login_to_jenkins(jurl, username, token)

    jversion = get_jenkins_version(server)
    print(f"Jenkins version:{jversion}")

    pipelines = get_pipelines(server)
    #print(f"Jenkins pipelines:{pipelines}")

    if(ppr_pipeline in pipelines):
        print(f"{ppr_pipeline} is available")
    else:
        print(f"{ppr_pipeline} is NOT available")

    #print(server.get_jobs_list())
    job = server.get_job("PR-111")
    print(f"job :{job}")
    print(f"job :{type(job)}")
    print(f"job :{type(job)}")

    jobs_info = server.get_jobs_info()
    #print(list(jobs_info))

    job_obj = server.get_job_by_url(pr_url, "PR-165")
    print(f"job_obj :{job_obj}")
    print(f"job_obj url :{job_obj.url}")
    print(f"job_obj :{type(job_obj)}")
    print(f"job_obj :{dir(job_obj)}")

    firstjob = job_obj.get_first_buildnumber()
    print(f"firstjob :{firstjob}")
    print(f"firstjob :{type(firstjob)}")

    lastjob = job_obj.get_last_buildnumber()
    print(f"lastjob :{lastjob}")
    print(f"lastjob :{type(lastjob)}")

    print(job_obj.get_last_buildnumber())
    build_dict = job_obj.get_build_dict()
    print(f"Build dictionary :{build_dict}")

    build_ids = job_obj.get_build_ids()
    print(f"Build ids :{list(build_ids)}")

    bmeta_data = job_obj.get_build_metadata(1)
    print(f"bmeta_Data :{bmeta_data}")
    print(f"bmeta_Data :{type(bmeta_data)}")
    print(f"bmeta_Data :{dir(bmeta_data)}")
    bstatus  = bmeta_data.get_status()

    print(f"status :{bstatus}")
    build_ids = job_obj.get_build_ids()
    for i in build_ids:
        bmeta_data = job_obj.get_build_metadata(i)
        bstatus  = bmeta_data.get_status()
        print(f"Build{i} : {bstatus}")

if (__name__ == "__main__"):
    main()

"""
#user = server.get_whoami()
#version = server.get_version()
#print('Hello %s from Jenkins %s' % (user['fullName'], version))
print(server.version)
print(server.keys())
job = server['https:/matrix.ap.sony.com/job']
print (f"job :{job}")
print(server.get_plugins())

jobName = server.keys()[0]  # get the first job
print (f"jobName :{jobName}")
job_config = server[jobName].get_config()
job_config = server[jobName].get_config()
print (f"job config:{job_config}")

params = {'token':'iMNgwU0J2lGHo9fBXKKoCZe6GFF830nt'}
qi = job.invoke(build_params=params)
print(qi)


"""
