

from selenium import webdriver
import time
import json

def run():
    show_browser = False
    chrome_options = webdriver.ChromeOptions()

    if show_browser:
        browser = webdriver.Chrome()
    else:
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        

    try:
        browser.get('http://www.htmleaf.com/ziliaoku/qianduanjiaocheng/20141225979.html')
        time.sleep(3)
        trs = browser.find_elements_by_css_selector('.table-striped tr');
        codeObjArr = []
        codeLine = ''
        codeHtml = ''
        for tr in trs:
            content = tr.text
            strArr = content.split(' ')
            if len(strArr) > 3:
                code = strArr.pop()
                display = strArr.pop()
                strArr.pop()
                temp = {
                    'name': ' '.join(strArr).lower(),
                    'display': display,
                    'code': code
                }
                line = '.mr-' + '-'.join(strArr).lower() + '::before{content: "' + code.replace('&#x', '\\').replace(';', '') + '";}\n'
                codeLine = codeLine + line
                html_line = '<i class="mr-icon mr-'+ '-'.join(strArr).lower() +'"></i>\n'
                codeHtml = codeHtml + html_line
                codeObjArr.append(temp)
        with open('../output/icon/icon.json','w', encoding='utf-8') as icon_json:
            json.dump(codeObjArr, icon_json, ensure_ascii=False)
            print('save json finish')

        with open('../output/icon/icon.txt', 'w', encoding='utf-8') as icon_txt:
            icon_txt.write(codeLine);
            print('save txt finish')

        with open('../output/icon/icon.html', 'w', encoding='utf-8') as icon_html:
            icon_html.write(codeHtml)
            print('save html finish')

    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    run()