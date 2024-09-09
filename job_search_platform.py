from validators import String,Integer,Email

class JobPosting:
    title = String()
    description = String()
    salary = Integer()
    def __init__(self,title:str,description:str,salary:int):
        self.title = title
        self.description = description
        self.salary = salary

    def __repr__(self):
        return f"Title:{self.title}, Description:{self.description},Salary:{self.salary}"



class FullTime(JobPosting):
    pass
class PartTime(JobPosting):
    pass

class Company:
    name = String()
    contact_info = Email()
    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info  = contact_info
        self.jobs = []
        self.resumes = {}

    def delete_postings(self,job:JobPosting):
        self.jobs.remove(job)

    def add_posting(self,job:JobPosting):
        self.jobs.append(job)


class JobSeeker:
    def __init__(self,name:str,contact_info:Email,resume:str):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    def search_job(self,job:JobPosting,company:Company):
        if job in company.jobs:
            print(f"searching this job {job}")
        else:
            print(f"there is no job like this")

    def apply_to_job(self,company:Company,job:JobPosting):
        company.resumes[self.name] = [job,self.resume]


jp = PartTime("developer","sql petqa imana",200000)
jf = FullTime("developeer","js,python petqa imana",400000)
company = Company("Picsarrt","picsartacademy@mail.ru")
jobseeker = JobSeeker("Alik","alik.0208@mail.ru","some about ALik")

company.add_posting(jp)
company.add_posting(jf)
jobseeker.search_job(jp,company)
jobseeker.apply_to_job(company,jf)
print(company.resumes)
for job in company.jobs:
    print(job)


