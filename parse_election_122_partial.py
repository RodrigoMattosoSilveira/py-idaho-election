# Python code to illustrate parsing of XML files
# importing the required modules
import sys
import xml.etree.ElementTree as Xet
import pandas as pd


def setup():
    # XML file
    # url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    xml_file = sys.argv[1]
    csv_file = sys.argv[2]

    arguments = {'xml': xml_file, 'csv': csv_file}

    # # creating HTTP response object from given url
    # resp = requests.get(url)
    #
    # # saving the xml file
    # with open('topnewsfeed.xml', 'wb') as f:
    #     f.write(resp.content)
    return arguments


def parseXML(xml_file):
    # create empty list for news items
    rows = []

    # Parsing the XML file
    xml_parse = Xet.parse(xml_file)
    root = xml_parse.getroot()
    for table in root.findall("Table"):
        election_id = table.find('ElectionID').text
        row = {
            "GroupName": table.find("GroupName").text,
            "ContestantName": table.find("ContestantName").text,
            "PartyName": table.find("PartyName").text,
            "TotalVotes": table.find("TotalVotes").text,
            "ContestantVotePercent": table.find("ContestantVotePercent").text
        }
        rows.append(row)

    # return news items list
    return rows


def save_to_CSV(rows, filename):
    # specifying the fields for csv file
    cols = [
            'GroupName',
            'ContestantName',
            "PartyName",
            'TotalVotes',
            'ContestantVotePercent'
            ]

    # writing to csv file
    df = pd.DataFrame(rows, columns=cols)

    # Writing dataframe to csv
    df.to_csv(filename)


def main():
    # load rss from web to update existing xml file
    arguments = setup()

    # parse xml file
    rows = parseXML(arguments['xml'])

    # store news items in a csv file
    save_to_CSV(rows, arguments['csv'])


if __name__ == "__main__":
    # calling main function
    main()
