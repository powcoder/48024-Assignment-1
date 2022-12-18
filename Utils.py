https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
class Utils:
    def check(prompt):
        s = input(f"{prompt}: ")
        if s!="2022AUT":
            return False
        else:
            return True

    def membershipFormat(name, email, phone, mmsType):
        return "| %-*s | %-*s | %-*s | %-*s |" % (20, name, 25, email, 10, phone, 10, mmsType)
    def slipFormat(name, expense, totalCredits, DollarAvailable, type):
        return "| %-*s | %-*s | %-*s | %-*s | %-*s|" % (15, name, 13,"{:.2f}".format(expense), 13, "{:.2f}".format(totalCredits), 13, "{:d}".format(DollarAvailable),9,type)

    def totalsFormat(header, amount):
        return "| %-*s |  %-*s |" % (26, header, 10, "{:.2f}".format(amount))
    
    def logFormat(record, recordId):
        return "| %-*s |  %-*s |" % (12, record, 13, recordId)

    def membershipHeader():
        print("+----------------------+---------------------------+------------+------------+")
        print("| Membership Name      | Email                     | Phone      | Type       |")
        print("+----------------------+---------------------------+------------+------------+")

    def slipHeader():
        print("+-----------------+---------------+---------------+---------------+----------+")
        print("| Membership Name | Expense       | Credit        | Dollars       | Type     |")
        print("+-----------------+---------------+---------------+---------------+----------+")


    def logHeader():
        print("+--------------+----------------+")
        print("| MMS Record   |  RecordID      |")
        print("+--------------+----------------+")

    def membershipTableEnd():
        print("+----------------------+---------------------------+------------+------------+")

    def slipTableEnd():
        print("+-----------------+---------------+---------------+---------------+----------+")

    def totalsTableHeaderAndEnd():
        print("+----------------------------+-------------+")

    def logTableEnd():
        print("+--------------+----------------+")
