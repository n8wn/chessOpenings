import csv
import re


def readTSV():
    tsvs = ['a.tsv', 'b.tsv', 'c.tsv', 'd.tsv', 'e.tsv']
    openings = []
    for filename in tsvs:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                openings.append({'pgn': row['pgn'], 'name': row['name']})
    return openings


def parseName(name):
    # "Sicilian Defense: Najdorf Variation, English Attack"
    # -> "Sicilian Defense, Najdorf Variation, English Attack"
    return name.replace(':', ',')


def parsePGN(pgn):
    # "1. e4 e5 2. Nf3 Nc6 3. Bb5" -> "e4 e5 Nf3 Nc6 Bb5"
    cleaned = re.sub(r'\d+\.', '', pgn)
    return ' '.join(cleaned.split())


def createNewCSV(openings, filename='openings_clean.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['pgn', 'name'])
        for o in openings:
            writer.writerow([o['pgn'], o['name']])
    print(f"new csv created: {filename}")


def main():
    openings = readTSV()
    for o in openings:
        o['name'] = parseName(o['name'])
        o['pgn'] = parsePGN(o['pgn'])

    createNewCSV(openings)
    print(f"Loaded {len(openings)} openings")


if __name__ == '__main__':
    main()