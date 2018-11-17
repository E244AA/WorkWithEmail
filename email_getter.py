class EmailGetter:
    def getEmails(self,path):
        file = open(path)
        all_emails = []

        for line in file:
            all_emails.append(line)

        file.close()
        return all_emails
