# Open / Close Principe
"""
    class֊ը պետք է բաց լինի ընդլայման համար և փակ լինի փոփոխությունների համար։
    Այլ կերպ ասած պատք է հնարավորություն ունենանք class֊ի նոր ֆունկցիոնալություն ապահովել
     առանց փոփոխելու հիմանկան կոդը։
"""


# Խախտում
class ReportGenerator:
    def generate_report(self, report_type):
        if report_type == "PDF":
            return "Generating PDF report."
        elif report_type == "Excel":
            return "Generating Excel report."


# ճիշտ իրականացում
class ReportGenerator:
    def generate_report(self, report):
        return report.generate()


class PDFReport:
    def generate(self):
        return "Generating PDF report."


class ExcelReport:
    def generate(self):
        return "Generating Excel report."

rp=ReportGenerator()
report=rp.generate_report(ExcelReport())
print(report)



