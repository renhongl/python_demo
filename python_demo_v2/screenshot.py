
import pyscreenshot as ImageGrab

if __name__ == "__main__":
    im=ImageGrab.grab()
    im.save('C:/Users/P1211678/Desktop/screenshot.png')
    im.show()