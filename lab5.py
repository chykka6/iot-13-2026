import datetime


class Bug:

    def __init__(self, desc: str = "", severity: str = "",
                  deadline: datetime.date = None, status: str = "",
                    assignee: str = ""):
        self.desc = desc
        self.severity = severity
        self.deadline = deadline if deadline is not None else datetime.date.today()
        self.status = status
        self.assignee = assignee

    def __str__ (self):
        return(f"desc = {self.desc}, deadline = {self.deadline}")

    def __repr__ (self):
        return(f"desc = {self.desc}, deadline = {self.deadline}")
    
    def getDesc(self):
        return self.desc

    def setDesc(self, desc: str):
        self.desc = desc

    def getSeverity(self):
        return self.severity

    def setSeverity(self, severity: str):
        self.severity = severity

    def getDeadline(self):
        return self.deadline

    def setDeadline(self, deadline: datetime.date):
        self.deadline = deadline

    def getStatus(self):
        return self.status

    def setStatus(self, status: str):
        self.status = status

class Backlog():

    def __init__(self, bugs: list[Bug] = None, name: str = ""):
        self.bugs = bugs if bugs is not None else []
        self.name = name

    def __str__ (self):
            return(f"{self.name}")

    def getBugs(self):
        return self.bugs

    def setBugs(self, bugs: list[Bug]):
        self.bugs = bugs

    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name

def main(): 
   assignee = input('Введіть імя користувача для пошуку: ')

   backlog = Backlog(name = "mybacklog")

   bug = Bug(desc = "bug1", assignee = "Taras", status = "open", severity = 1)
   
   bug2 = Bug(desc = "bug2", assignee = "Alex", status = "resolved", severity = 2, deadline = datetime.date(2026, 6, 1))
   
   bug3 = Bug(desc = "bug3", assignee = "Alex", status = "resolved", severity = 3, deadline = datetime.date(2026, 5, 15))
   
   bug4 = Bug(desc = "bug4", assignee = "Taras", status = "resolved", severity = 1, deadline = datetime.date(2026, 5, 17))
   
   backlog.setBugs([bug, bug2, bug3, bug4])

   assignee_bugs = [bug for bug in backlog.getBugs() if bug.assignee == assignee and bug.status == "resolved"]
   assignee_bugs.sort(key=lambda bug: bug.severity)

   print(f"Назва беклогу: {backlog}")

   print(f"all Bugs: {backlog.getBugs()}")
   print(f"Bug assignee: {assignee}")
   print(f"assignee bugs: {assignee_bugs}")

   print(f"All bugs severity: {[bug.severity for bug in backlog.getBugs()]}")


if __name__ == "__main__":
  main()