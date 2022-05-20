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
            "ElectionID": table.find('ElectionID').text,
            "RaceID": table.find("RaceID").text,
            "GroupID": table.find("GroupID").text,
            "GroupName": table.find("GroupName").text,
            "GroupSequence": table.find("GroupSequence").text,
            "RaceName": table.find("RaceName").text,
            "VoteFor": table.find("VoteFor").text,
            "NumPositions": table.find("NumPositions").text,
            "NonPartisanRace": table.find("NonPartisanRace").text,
            "ContestWithdrawn": table.find("ContestWithdrawn").text,
            "RunOff": table.find("RunOff").text,
            "MajorPercent": table.find("MajorPercent").text,
            "MinimumVotes": table.find("MinimumVotes").text,
            "ContestantID": table.find("ContestantID").text,
            "ContestantName": table.find("ContestantName").text,
            "Party": table.find("Party").text,
            "PartyName": table.find("PartyName").text,
            "EarlyVotingVotes": table.find("EarlyVotingVotes").text,
            "MailBallotsVotes": table.find("MailBallotsVotes").text,
            "ElectionDayVotes": table.find("ElectionDayVotes").text,
            "ProvisionalVotes": table.find("ProvisionalVotes").text,
            "TotalVotes": table.find("TotalVotes").text,
            "TimesCounted": table.find("TimesCounted").text,
            "BlankVoted": table.find("BlankVoted").text,
            "OverVotes": table.find("OverVotes").text,
            "UnderVotes": table.find("UnderVotes").text,
            "ContestantColor": table.find("ContestantColor").text,
            "ContestantWithdrawn": table.find("ContestantWithdrawn").text,
            "ContestantVotePercent": table.find("ContestantVotePercent").text,
            "StateRace": table.find("StateRace").text
        }
        rows.append(row)

    # return news items list
    return rows


def save_to_CSV(rows, filename):
    # specifying the fields for csv file
    cols = ['ElectionID',
            'RaceID',
            'GroupID',
            'GroupName',
            'GroupSequence',
            'RaceName',
            'VoteFor',
            'NumPositions',
            'NonPartisanRace',
            'ContestWithdrawn',
            'RunOff',
            'MajorPercent',
            'MinimumVotes',
            'ContestantID',
            'ContestantName',
            'Party',
            'PartyName',
            'EarlyVotingVotes',
            'MailBallotsVotes',
            'ElectionDayVotes',
            'ProvisionalVotes',
            'TotalVotes',
            'TimesCounted',
            'BlankVoted',
            'OverVotes',
            'UnderVotes',
            'ContestantColor',
            'ContestantWithdrawn',
            'ContestantVotePercent',
            'StateRace',
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
