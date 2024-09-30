import requests
import selenium
import scrapy
from bs4 import BeautifulSoup

class DataIngestion():
    def __init__(self, nameOfWebsite = None, urlOfWebsite = None):
        self.name = nameOfWebsite
        self.url = urlOfWebsite

    def job_portals(self):
        """This function creates a dictornies of name of comapny and its url"""
        job_portals_list = {
            "Indeed USA": "https://www.indeed.com",
            "Glassdoor USA": "https://www.glassdoor.com",
            "LinkedIn": "https://www.linkedin.com/jobs",
            "Monster USA": "https://www.monster.com",
            "ZipRecruiter": "https://www.ziprecruiter.com",
            "CareerBuilder USA": "https://www.careerbuilder.com",
            "SimplyHired USA": "https://www.simplyhired.com",
            "USAJobs": "https://www.usajobs.gov",
            "Daijob (Japan)": "https://www.daijob.com",
            "GaijinPot Jobs (Japan)": "https://jobs.gaijinpot.com",
            "CareerCross (Japan)": "https://www.careercross.com/en",
            "51job (China)": "https://www.51job.com",
            "Zhaopin (China)": "https://www.zhaopin.com",
            "ChinaJob (China)": "https://www.chinajob.com",
            "Totaljobs (UK)": "https://www.totaljobs.com",
            "Reed (UK)": "https://www.reed.co.uk",
            "Indeed UK": "https://www.indeed.co.uk",
            "IrishJobs (Ireland)": "https://www.irishjobs.ie",
            "Jobs.ie (Ireland)": "https://www.jobs.ie",
            "Indeed Ireland": "https://ie.indeed.com",
            "Workopolis (Canada)": "https://www.workopolis.com",
            "JobBank (Canada)": "https://www.jobbank.gc.ca",
            "Indeed Canada": "https://ca.indeed.com",
            "Pôle Emploi (France)": "https://www.pole-emploi.fr",
            "Cadremploi (France)": "https://www.cadremploi.fr",
            "Indeed France": "https://fr.indeed.com",
            "StepStone (Germany)": "https://www.stepstone.de",
            "Xing Jobs (Germany)": "https://www.xing.com/jobs",
            "Indeed Germany": "https://de.indeed.com",
            "We Work Remotely": "https://www.weworkremotely.com",
            "FlexJobs": "https://www.flexjobs.com",
            "Upwork": "https://www.upwork.com",
            "Dice": "https://www.dice.com",
            "Stack Overflow Jobs": "https://stackoverflow.com/jobs",
            "eFinancialCareers": "https://www.efinancialcareers.com",
            "Behance Jobs": "https://www.behance.net/joblist",
            "Idealist (Nonprofit)": "https://www.idealist.org",
            "Internships.com": "https://www.internships.com",
            "ErasmusIntern": "https://www.erasmusintern.org",
            "Wellfound (AngelList Talent)": "https://www.wellfound.com",
            "Dribbble": "https://dribbble.com/jobs",
            "ProBlogger (Marketing)": "https://problogger.com/jobs",
            "Hired": "https://hired.com",
            "Mashable Jobs": "https://jobs.mashable.com",
            "SalesGravy": "https://www.salesgravy.com",
            "JobsInSports": "https://www.jobsinsports.com",
            "Remote.co": "https://remote.co",
            "AngelList": "https://angel.co/jobs",
            "JobisJob": "https://www.jobisjob.com",
            "CollegeRecruiter": "https://www.collegerecruiter.com",
            "TalentZoo": "https://www.talentzoo.com"
        }

        return job_portals_list

    def send_request(self, url):
        """This function sends a request to the website and fetches its content."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                return soup
            else:
                print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


if __name__ == "__main__":
    data_ingestion = DataIngestion()
    portals = data_ingestion.job_portals()
    
    for name, url in portals.items():
        print(f"Fetching data from {name}: {url}")
        soup = data_ingestion.send_request(url)
        if soup:
            print(f"Page Title: {soup.title.string}")
        break