"""
Proszę stworzyć interfejs ReportFormatter.format(data).
Implementacje: CSVFormatter, JSONFormatter, HTMLFormatter.
Klasa Report przyjmuje strategię i wywołuje formatter.format(data).
"""

class ReportFormatter:
    def format(self, data):
        raise NotImplementedError("To jest metoda abstrakcyjna")
    
class CSVFormatter(ReportFormatter):
        def format(self, data):
            print(f"CSVFormatter:  + {data}")

class JSONFormatter(ReportFormatter):
        def format(self, data):
            print(f"JSONFormatter:  + {data}")

class HTMLFormatter(ReportFormatter):
        def format(self, data):
            print(f"HTMLFormatter:  + {data}")

class Report:
    def __init__(self, formatter: ReportFormatter):
        self.formatter = formatter

    def generate(self, data):
        self.formatter.format(data)

report1 = Report(CSVFormatter())
report1.generate("dane do raportu1")

report2 = Report(JSONFormatter())
report2.generate("dane do raportu2")

report3 = Report(HTMLFormatter())
report3.generate("dane do raportu3")