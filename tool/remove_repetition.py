

def main():
    with open('./input/html.txt', 'r', encoding='utf-8') as html:
        lines = []
        while True:
            line = html.readline()
            if line == '':
                break
            lines.append(line)

    data = set(lines)
    with open('./input/html_out.txt', 'w', encoding='utf-8') as html_out:
        lines = ''
        for item in data:
            lines = lines + item
        
        html_out.write(lines)



if __name__ == '__main__':
    main()